import traceback

import requests

from requests.auth import HTTPDigestAuth

from selenium.webdriver.common.by import By

from easyselenium.browser import Browser

from utils.web import test_url_exists

from requests.packages.urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


USERNAME = 'strelkov'
PASSWORD = 'D2h3mtHhWdWU8boE?'


def __get_links(url):
    links = []
    browser = None
    try:
        browser = Browser('gc')
        browser.get(url)
        e_username = (By.ID, 'os_username')
        e_password = (By.ID, 'os_password')
        e_login_btn = (By.ID, 'loginButton')

        if browser.is_visible(e_username) and browser.is_visible(e_password):
            browser.type(e_username, USERNAME)
            browser.type(e_password, PASSWORD)
            browser.click(e_login_btn)
            browser.wait_for_not_visible(e_login_btn)

        for link in browser.find_elements((By.TAG_NAME, 'a')):
            if browser.is_visible(link):
                link_url = browser.get_attribute(link, 'href')
                if link_url and link_url.startswith('http'):
                    text = browser.get_text(link)
                    links.append({'text': text, 'url': link_url})
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
    url = 'https://confluence.in.here.com/display/MMA3/Test+strategy'
    # url = 'https://confluence.in.here.com/display/MMA3/Non+functional+testing'

    for link in __get_links(url):
        text = link['text']
        link_url = link['url']
        if link and link_url.startswith('http'):
            # print("Link '{}'".format(link))
            is_alive_link = test_url_exists(link_url, auth=HTTPDigestAuth(USERNAME, PASSWORD))
            if not is_alive_link:
                print("Link '{}' with url: '{}' alive?: {}".format(text, link_url, is_alive_link))
