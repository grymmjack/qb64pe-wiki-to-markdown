"""
=====================================================
mw-to-md.py - MediaWiki(mw) to Markdown(md) Converter
-----------------------------------------------------
This script fetches HTML content from the QB64PE wiki 
using a list of keywords (keywords.txt) and converts
the content to Markdown format. The Markdown content is
then saved to individual .md files in a specified directory.

Author:  Rick Christy
Email:   grymmjack@gmail.com
Website: https://grymmjack.github.io
=====================================================
"""
import copy
import lxml
import urllib
import requests
import re
import os
import requests
from bs4 import BeautifulSoup
from bs4 import Tag

# HELP_DIR = '/home/grymmjack/git/QB64pe/internal/help'
HELP_DIR = '.'


def fetch_html(url):
    """
    Fetches the HTML content from the specified URL.

    Args:
        url (str): The URL to fetch the HTML content from.

    Returns:
        str: The fetched HTML content, or None if an error occurred.
    """
    headers = {
        "Host": "qb64phoenix.com",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://qb64phoenix.com/qb64wiki/index.php?search=%24CHECKING&title=Special%3ASearch&profile=default&fulltext=1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = str(BeautifulSoup(response.text, 'html.parser').prettify())
        return soup
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def fetch_html_offline(path):
    """
    Fetches the HTML content from the specified file.

    Args:
        path (str): The path to fetch the HTML content from.

    Returns:
        str: The fetched HTML content, or None if an error occurred.
    """

    try:
        with open(path, 'r') as file:
            html_content = '\n'.join([line.strip() for line in file.readlines()])
            file.close()
            soup = str(BeautifulSoup(html_content, 'html.parser').prettify())
            return soup
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return None


def link_keywords(line, use_file=True):
    """
    Replaces keywords in a line with markdown links to corresponding .md files.

    Args:
        line (str): The line of text to process.

    Returns:
        str: The processed line with keywords replaced by markdown links.
    """
    ret = line
    processed_keywords = []
    word_boundary_open =  '\\s*\\b'
    word_boundary_close = '(\\b|$)'
    neg_lookahead = '(?![\(|\)])'
    for keyword in keywords_sorted:
        if keyword in line:
            keyword_esc = keyword.replace('$', '\$')
            find = neg_lookahead + word_boundary_open + keyword_esc + word_boundary_close
            keyword_esc = keyword_esc.replace('/', '-')
            if len(re.findall(find, ' '.join(processed_keywords))) == 0:
                keyword_no_prefix = re.sub('^_', '', keyword_esc) # remove leading underscore
                if use_file:
                    # ret = ret.replace(keyword, f'[{keyword}](file:{HELP_DIR}/{keyword}.md)')
                    repl = f' [{keyword_esc}](file:{HELP_DIR}/{keyword_no_prefix}.md) '
                else:
                    # ret = ret.replace(keyword, f'[{keyword}]({HELP_DIR}/{keyword}.md)')
                    repl = f' [{keyword_esc}]({keyword_no_prefix}.md) '

                ret = re.sub(find, repl, ret, flags=re.IGNORECASE | re.DOTALL | re.MULTILINE)
                processed_keywords.append(keyword)
    ret = re.sub('^\*', '* ', ret)
    return ret


def get_list_items(tag, keyword, linked=False, indent_level=0):
    """
    Recursively extracts list items from HTML tags and returns them as a formatted string.

    Args:
        tag (Tag): The HTML tag to extract list items from.
        keyword (str): The keyword to search for in the list items.
        linked (bool, optional): Determines whether the list items should be formatted as linked or not. Defaults to False.
        indent_level (int, optional): The indentation level of the list items. Defaults to 0.

    Returns:
        str: The formatted list items as a string.
    """
    ret = ''
    if tag.name == 'li':
        if tag.ul:
            # Remove the inner ul element if it exists to get the text from the inside one.
            work_li = copy.copy(tag)
            work_li.ul.decompose()
            line = work_li.get_text(strip=True, separator=' ')
        else:
            # If no inside ul, get the text from the current li.
            line = tag.get_text(strip=True, separator=' ')

        # line = tag.get_text(strip=True, separator=' ')
        if linked:
            ret = link_keywords('\t' * indent_level + '* ' + line + '\n', False)
        else:
            ret = '\t' * indent_level + '* ' + line + '\n'
    for child in tag.children:
        if isinstance(child, Tag) and child.name == 'ul':
            for li in child.find_all('li', recursive=False):
                ret += get_list_items(li, keyword, linked, indent_level + 1)

    return ret


def convert_to_markdown(html, keyword):
    """
    Converts HTML content to Markdown format.

    Args:
        html (str): The HTML content to be converted.
        keyword (str): The keyword used for parsing the HTML content.

    Returns:
        str: The converted Markdown content.
    """
    ret_content = ''

    soup = BeautifulSoup(html, 'lxml')
    if soup:
        #TITLE
        h1_tag = soup.find('h1', class_="firstHeading mw-first-heading")
        if h1_tag:
            h1_keyword = h1_tag.text.strip().replace('$', '\$')
            h1_keyword = h1_keyword.replace(' ', '_')
            h1_keyword = h1_keyword.replace('/', '-')
            h1_page = re.sub('^_', '', h1_keyword) # remove leading underscore
            wiki_link = ' [📖](https://qb64phoenix.com/qb64wiki/index.php/' + h1_tag.text.strip() + ')'
            ret_content += '## [' +  h1_keyword + '](' + h1_page + '.md)' + wiki_link + '\n---\n'

        #SUMMARY
        try:
            summary = soup.find('div', class_='mw-parser-output').find('p')
            ret_content += '<blockquote>\n\n### ' + summary.get_text(strip=True, separator=' ') + '\n\n</blockquote>\n'
        except:
            pass

        #SYNTAX
        try:
            syntax = soup.select('h2 + dl dd:first-child')[0]
            ret_content += '\n#### SYNTAX\n\n<blockquote>\n\n'
            ret_content += '`' + syntax.get_text(strip=True, separator=' ') + '`\n\n</blockquote>\n'
        except:
            pass

        #SAMPLES
        sample_text = ''
        h3_tag = soup.select('span#Sample_usage')
        list_items = []
        if h3_tag:
            h3_tag = h3_tag[0].parent
            for sibling in h3_tag.next_siblings:
                if isinstance(sibling, Tag):
                    if sibling.name == 'p':
                        break
                    if sibling.name == 'dl':
                        dd = sibling.find('dd')
                        list_items.append('  \n  \n---\n```vb\n' + dd.get_text(strip=True, separator=' ') + '\n```\n---\n  \n  \n')

            sample_text = ''.join(list_items)
            ret_content += '  \n#### SAMPLES\n\n<blockquote>\n\n'
            ret_content += sample_text + '\n</blockquote>\n'

        #PARAMETERS
        h2_tag = soup.select('span#Parameters')
        list_items = []
        if h2_tag:
            h2_tag = h2_tag[0].parent
            for sibling in h2_tag.next_siblings:
                if isinstance(sibling, Tag):
                    if sibling.name == 'p':
                        break
                    if sibling.name == 'center':
                        list_items.append(sibling.get_text(strip=True, separator=' ') + '\n')
                    if sibling.name == 'ul':
                        for li in sibling.find_all('li', recursive=False):
                            list_items.append(get_list_items(li, keyword, True))
                    if sibling.name != 'ul':
                        break

            parameters_text = ''.join(list_items)
            ret_content += '\n#### PARAMETERS\n\n<blockquote>\n\n'
            ret_content += parameters_text + '\n</blockquote>\n'

        #DESCRIPTION
        h2_tag = soup.select('span#Description')
        list_items = []
        if h2_tag:
            h2_tag = h2_tag[0].parent
            for sibling in h2_tag.next_siblings:
                if isinstance(sibling, Tag):
                    if sibling.name == 'p':
                        break
                    if sibling.name == 'center':
                        list_items.append(sibling.get_text(strip=True, separator=' ') + '\n')
                    if sibling.name == 'ul':
                        for li in sibling.find_all('li', recursive=False):
                            list_items.append(get_list_items(li, keyword, True))
                    if sibling.name != 'ul':
                        break

            description_text = ''.join(list_items)
            ret_content += '\n#### DESCRIPTION\n\n<blockquote>\n\n'
            ret_content += description_text + '\n\n</blockquote>\n'

        #EXAMPLES
        h2_tag = soup.select('span#Examples')
        list_items = []
        if h2_tag: # officially in page
            h2_tag = h2_tag[0].parent
            for sibling in h2_tag.next_siblings:
                if isinstance(sibling, Tag):
                    if sibling.name == 'p':
                        temp = ' '
                        temp = sibling.get_text(strip=True, separator=' ')
                        if temp:
                            list_items.append("\n\n##### " + temp + '\n')
                    codeblock = sibling.find('pre', recursive=True)
                    if codeblock:
                        code = re.sub(r'\n ', '\n', codeblock.text)
                        list_items.append("```vb" + '\n' + code.strip() + "\n```\n  \n<br>")
        else: # unofficially in page
            codeblocks  = soup.find_all('pre')
            for codeblock in codeblocks:
                for parent in codeblock.parents:
                    if parent.name == 'table':
                        p = parent.find_previous_sibling('p')
                        temp = p.get_text(strip=True, separator=' ')
                        if 'Example' in temp:
                            list_items.append("\n\n##### " + temp + '\n')
                            break
                code = re.sub(r'\n ', '\n', codeblock.text)
                list_items.append("```vb" + '\n' + code.strip() + "\n```\n  \n<br>")
            examples_text = ''.join(list_items)
            ret_content += '\n#### EXAMPLES\n\n<blockquote>\n\n'
            ret_content += examples_text + '\n</blockquote>\n'

        #MORE EXAMPLES
        h3_tag = soup.select('span#More_examples')
        list_items = []
        if h3_tag:
            h3_tag = h3_tag[0].parent
            for sibling in h3_tag.next_siblings:
                if isinstance(sibling, Tag):
                    if sibling.name == 'p':
                        break
                    if sibling.name == 'center':
                        list_items.append(sibling.get_text(strip=True, separator=' ') + '\n')
                    if sibling.name == 'ul':
                        for li in sibling.find_all('li', recursive=True):
                            list_items.append(get_list_items(li, keyword, True))
                    if sibling.name != 'ul':
                        break

            more_text = ''.join(list_items)
            ret_content += '\n#### MORE EXAMPLES\n\n<blockquote>\n\n'
            ret_content += more_text + '\n</blockquote>\n'

        #SEE ALSO
        h2_tag = soup.select('span#See_also')
        list_items = []
        if h2_tag:
            h2_tag = h2_tag[0].parent
            for sibling in h2_tag.next_siblings:
                if isinstance(sibling, Tag):
                    if sibling.name == 'p':
                        break
                    if sibling.name == 'center':
                        list_items.append(sibling.get_text(strip=True, separator=' ') + '\n')
                    if sibling.name == 'ul':
                        for li in sibling.find_all('li', recursive=True):
                            list_items.append(get_list_items(li, keyword, True))
                    if sibling.name != 'ul':
                        break

            see_also_text = ''.join(list_items)
            ret_content += '\n#### SEE ALSO\n\n<blockquote>\n\n'
            ret_content += see_also_text + '\n</blockquote>\n'

    return ret_content


def save_markdown(markdown, filename, use_css=True):
    """
    Saves the given markdown content to a file.

    Args:
        markdown (str): The markdown content to be saved.
        filename (str): The name of the file to save the markdown content to.

    Returns:
        None
    """
    if use_css:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(css + markdown)
    else: 
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(css + markdown)


def replace_backtick_with_grave(matchobj) -> str:
    """
    Replaces backticks with the HTML entity for grave accent.

    Args:
        matchobj (re.Match): The match object representing the matched backtick.

    Returns:
        str: The replacement string with the HTML entity for grave accent.
    """
    if matchobj.group(0) == '`':
        return '&grave;'


def backticks_to_graves(text:str) -> str:
    """
    Converts backticks (`) in the given text by replacing them with '&grave;'.

    Args:
        text (str): The text to convert backticks in.

    Returns:
        str: The text with backticks converted to html entity &grave;.
    """
    return re.sub(r'`', replace_backtick_with_grave, text)


def escape_dollar_signs(text: str) -> str:
    """
    Escapes dollar signs ($) in the given text by replacing them with '\$'.

    Args:
        text (str): The text to escape dollar signs in.

    Returns:
        str: The text with dollar signs escaped.
    """
    return text.replace('$', r'&dollar;')


def process_page(keyword, output_dir):
    """
    Process a keyword by fetching its HTML content from the QB64PE wiki,
    converting it to Markdown, and saving the Markdown content to a file.

    Args:
        keyword (str): The keyword to process.
        output_dir (str): The directory where the Markdown file will be saved.

    Returns:
        None
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Correctly encode the keyword for URL use
    encoded_keyword = urllib.parse.quote_plus(keyword)
    encoded_keyword = encoded_keyword.replace('+', '_')


    # from wiki
    url = f'https://qb64phoenix.com/qb64wiki/index.php/{encoded_keyword}'
    print(f'\nProcessing: {url}...')
    html_content = fetch_html(url)
    if html_content:
        safe_filename = re.sub('/', '-', keyword)
        safe_filename = re.sub(' ', '_', safe_filename)
        with open(f'html_files/{safe_filename}.html', 'w') as f:
            f.write(html_content)
            f.close()
            print(f'Requested and Saved HTML: html_files/{keyword}')

    if html_content:
        if '`' in html_content:
            html = backticks_to_graves(html_content)
            html_content = html
        markdown_content = convert_to_markdown(html_content, safe_filename)
        file_path = os.path.join(output_dir, f"{safe_filename}.md")
        save_markdown(markdown_content, file_path)
        print(f"Converted HTML and Saved Markdown: {file_path}\n")

output_directory = 'markdown_files'

css = ''
with open('style.css', 'r') as file:
    css = '<style type="text/css">\n' + file.read() + '\n</style>\n\n'
    file.close()

# Read keywords from file
current_directory = os.path.dirname(os.path.abspath(__file__))
keywords_file_path = os.path.join(current_directory, 'keywords.txt')
with open('keywords.txt', 'r') as file:
    keywords = [line.strip() for line in file.readlines()]
    file.close()
keywords_sorted = copy.deepcopy(keywords)
keywords_sorted.sort()
keywords_sorted.sort(key=len)
keywords_sorted.sort(key=len, reverse=True)

# Read wiki pages from file
with open('wikipages.txt', 'r') as file:
    pages = [line.strip() for line in file.readlines()]
    file.close()

# Process each keyword
for page in pages:
    if page != '**EOF**':
        process_page(page, output_directory)
    else:
        break

