"""
wget -q -O - 'https://qb64phoenix.com/qb64wiki/api.php?action=query&list=allpages&aplimit=500&apcontinue=GlPointSize&format=json' | jq -cr '.query.allpages[].title'

https://www.mediawiki.org/w/api.php?action=help&modules=query%2Ballpages
https://www.mediawiki.org/w/api.php?action=help&modules=query
https://www.mediawiki.org/w/api.php?action=help&modules=parse
https://www.mediawiki.org/wiki/API:Continue
https://qb64phoenix.com/qb64wiki/api.php?action=parse&page=ABS&prop=sections

"""


WIKI_API_URL = 'https://qb64phoenix.com/qb64wiki/api.php'
WIKI_BASE_QUERY = '?action=query&list=allpages&aplimit=500&format=json'

import requests
import json

def get_wiki_pages():
    # Get all wiki pages
    wiki_pages = []
    wiki_url = WIKI_API_URL + WIKI_BASE_QUERY
    while True:
        response = requests.get(wiki_url)
        data = response.json()
        wiki_pages.extend(data['query']['allpages'])
        if 'continue' in data:
            wiki_url = WIKI_API_URL + WIKI_BASE_QUERY + '&apcontinue=' + data['continue']['apcontinue']
        else:
            break
    return wiki_pages

def get_all_wiki_pages():
    # Get all wiki pages
    wiki_pages = []
    for page in wiki.pages:
        wiki_pages.append(page)
    return wiki_pages

wiki_pages = get_wiki_pages()
print(len(wiki_pages))
print(wiki_pages[0])
