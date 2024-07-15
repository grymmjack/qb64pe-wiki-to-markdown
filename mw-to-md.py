import urllib
import requests
import markdownify
import re
import os
from bs4 import BeautifulSoup

def fetch_html(url):
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
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None    

def convert_to_markdown(html):
    soup = BeautifulSoup(html, 'html.parser')

    remove_css_classes = [
        'noprint',
        'mw-indicators',
        'mw-jump-link',
        'printfooter'
    ]
    remove_css_ids = [
        'toc',
        'siteSub',
        'contentSub',
        'contentSub2',
        'siteNotice',
        'jump-to-nav',
        'catlinks',
        'mw-navigation',
        'mw-panel'
    ]
    
    for css_class in remove_css_classes:
        for rem in soup.find_all(attrs={"class": css_class}, recursive=True):
            rem.decompose()

    for css_id in remove_css_ids:
        for rem in soup.find_all(attrs={"id": css_id}, recursive=True):
            rem.decompose()

    # Remove MediaWiki-specific tags and content
    remove_tags = [
        'script', 
        'style', 
        'meta', 
        'link', 
        'nav', 
        'header', 
        'footer', 
        'center'
    ]    
    for tag in soup(remove_tags):
        tag.decompose()

    # for code in soup.find_all('pre', attrs={"class": "codeide"}):
    #     for link in code.find_all('a'):
    #         link.unwrap()
    #     for span in code.find_all('span'):
    #         span.unwrap()
    
    for table in soup.find_all('table', attrs={"style": "max-width:25%;"}):
        table.decompose()

    for hr in soup.find_all('hr'):
        hr.decompose()

    # Convert to markdown
    options = {
        # "strip": [
        #     'script', 
        #     'style', 
        #     'meta', 
        #     'link', 
        #     'nav', 
        #     'header', 
        #     'footer', 
        #     'center'
        # ],
        "autolinks": False,
        "heading_style": "ATX",
        "bullets": [
            "*",
            "+",
            "-"
        ],
        "wrap": False,
        "wrap_width": 80,
        "newline_style": "BACKSLASH",
        "strong_em_symbol": "*",
        "code_language": "",
        "escape_asterisks": True,
        "escape_underscores": True,
        "escape_misc": True,
        "keep_inline_images_in": [
            "li"
        ]
    }
    # markdown_content = markdownify.MarkdownConverter(**options).convert_soup(soup)
    # markdown_content = markdownify.markdownify(str(soup), **options)
    markdown_content = str(soup)

    # Additional cleaning to remove any remaining MediaWiki-specific markup
    markdown_content = re.sub('\\\\n', '\\n', markdown_content)
    markdown_content = re.sub(r'\| ```', '```vb\n', markdown_content)
    markdown_content = re.sub(r'``` \|', '\\n```', markdown_content)
    markdown_content = re.sub(r'\| --- \|', '', markdown_content)
    markdown_content = re.sub(r'\[\[Category:[^\]]+\]\]', '', markdown_content)
    markdown_content = re.sub(r'\[\[File:[^\]]+\]\]', '', markdown_content)
    markdown_content = re.sub(r'\[\[.*?\|', '', markdown_content)  # Remove links but keep text
    markdown_content = re.sub(r'\]\]', '', markdown_content)
    markdown_content = re.sub(r'/qb64wiki/index\.php/', '', markdown_content)
    markdown_content = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'[\1](\1.md)', markdown_content)
    markdown_content = re.sub('\[Jump to navigation\]\(Jump to navigation\.md\)', '', markdown_content)
    markdown_content = re.sub('\[Jump to search\]\(Jump to search\.md\)', '', markdown_content)
    markdown_content = re.sub('From QB64 Phoenix Edition Wiki', '', markdown_content)
    markdown_content = re.sub('\|  \|', '', markdown_content)
    markdown_content = re.sub('</p><p>', '', markdown_content)
    markdown_content = re.sub('<br/>', '', markdown_content)

    # Replace more than two newlines with two newlines
    reduced_content = markdown_content.replace('\n\n', '\n')
    
    # It's possible that after the first replacement there are still places with more than two newlines
    # Keep reducing until no more than two consecutive newlines exist
    while '\n\n' in reduced_content:
        reduced_content = reduced_content.replace('\n\n', '\n')

    # remove top 4 lines    
    # reduced_content = "\n".join(reduced_content.split("\n")[4:])
    # remove last 3 lines
    # reduced_content = "\n".join(reduced_content.split("\n")[:-3])

    reduced_content = "<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style>" + reduced_content
    return reduced_content

def save_markdown(markdown, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(markdown)

def escape_dollar_signs(filename: str) -> str:
    return filename.replace('$', r'\$')        

def process_keyword(keyword, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Correctly encode the keyword for URL use
    encoded_keyword = urllib.parse.quote_plus(keyword)

    # from wiki
    url = f'https://qb64phoenix.com/qb64wiki/index.php/{encoded_keyword}'
    print(url)
    html_content = fetch_html(url)
    if html_content:
        markdown_content = convert_to_markdown(html_content)
        file_path = os.path.join(output_dir, f"{keyword}.md")
        save_markdown(markdown_content, file_path)
        print(f"Processed and saved: {file_path}")

output_directory = 'markdown_files'

# Read keywords from file
current_directory = os.path.dirname(os.path.abspath(__file__))
keywords_file_path = os.path.join(current_directory, 'keywords.txt')
with open('keywords.txt', 'r') as file:
    keywords = [line.strip() for line in file.readlines()]

# Process each keyword
for keyword in keywords:
    if keyword == "**EOF**":
        break
    else:
        process_keyword(keyword, output_directory)

