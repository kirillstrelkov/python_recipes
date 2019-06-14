import traceback

import requests

from selenium.webdriver.common.by import By

from easyselenium.browser import Browser

from utils.web import test_url_exists

from requests.packages.urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def __get_frames(browser):
    return browser.find_elements((By.TAG_NAME, 'frame')) + \
           browser.find_elements((By.TAG_NAME, 'iframe'))


def __get_links_from_current_page(browser):
    links = []

    for link in browser.find_elements((By.TAG_NAME, 'a')):
        if browser.is_visible(link):
            link_url = browser.get_attribute(link, 'href')
            if link_url and link_url.startswith('http'):
                text = browser.get_text(link)
                links.append({'text': text, 'url': link_url})

    return links


def __get_links_from_frames(browser, frames=None):
    links = []

    if not frames:
        frames = __get_frames(browser)

    for frame in frames:
        browser.switch_to_frame(frame)

        links += __get_links_from_current_page(browser)

        inner_frames = __get_frames(browser)
        if inner_frames:
            links += __get_links_from_frames(browser, inner_frames)

    browser.switch_to_default_content()

    return links


def __get_links(url):
    links = []
    browser = None
    try:
        browser = Browser('gc')
        browser.get(url)

        links += __get_links_from_current_page(browser)
        links += __get_links_from_frames(browser)
    except:
        try:
            browser.save_screenshot()
        except:
            pass
        traceback.print_exc()
    finally:
        if browser:
            browser.quit()
    return links


if __name__ == '__main__':
    url = 'https://sites.google.com/site/kirillstrelkov/home/portfolio'

    for link in __get_links(url):
        text = link['text']
        link_url = link['url']
        if link and link_url.startswith('http'):
            is_alive_link = test_url_exists(link_url)

            if not is_alive_link:
                print("Link '{}' with url: '{}' alive?: {}".format(text, link_url, is_alive_link))
