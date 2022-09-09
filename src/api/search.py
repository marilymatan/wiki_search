import json
import logging
import os
import wikipediaapi
from error_mapping import unknown_exception
from utils.logger_utils import log_endpoint
from flask import jsonify, make_response


def add_page_to_list(list_of_pages: list, title: str, summary: str):
    '''
    :param list_of_pages: List of pages
    :param title: page title
    :param summary: page summary
    :return: None, but work on list_of_pages mutable param
    '''
    list_of_pages.append(dict({
        "title": title,
        "summary": summary
    }))


@log_endpoint('GET /search')
def search(search_phrase: str, k: int = 1) -> tuple:
    '''
    :param search_phrase: Search phrase in Wikipedia
    :param k: Top k result if necessary
    :return: List of data found, and status response
    '''

    try:
        lang = os.environ['language']
        wiki = wikipediaapi.Wikipedia(lang)
        wiki_result = wiki.page(search_phrase)

        if not wiki_result.exists():
            return dict(result='Page does not exist'), 200

        ret = []
        key_wiki_pages = os.environ['key_wiki_pages']

        if key_wiki_pages in wiki_result.categories.keys():
            wiki_links = wiki_result.links
            wiki_links_items = wiki_links.items()
            for count, (key, val) in enumerate(wiki_links_items):
                if count == k:
                    break
                add_page_to_list(ret, title=key, summary=val.summary)
        else:
            add_page_to_list(ret, title=wiki_result.title, summary=wiki_result.summary)
    except Exception as err:
        logging.error(f'ERROR: {err}')
        return dict(error_desc=unknown_exception), 500
    return ret, 200
