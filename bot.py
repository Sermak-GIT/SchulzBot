#!/usr/bin/env python3

import logging

import bs4
import requests
from selenium import webdriver

import time
import whats_app_helper
import os

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
chat_name = "Gottkanzler Schulz"
logging.debug('SchulzBot v0.1')


def sleep(secs):
    print("Waiting for %i seconds..." % (secs))


reddit_req = requests.get("https://www.reddit.com/r/the_schulz/", headers={'User-agent': 'SchulzBot'})
reddit_req.raise_for_status()

reddit = bs4.BeautifulSoup(reddit_req.text, "html.parser", from_encoding="utf-8")
logging.debug(type(reddit))

titles = reddit.select('a[data-event-action="title"]')
img_links = reddit.select('a[data-event-action="thumbnail"]')
things = reddit.select('.thing')

logging.debug(len(things))
logging.debug(len(titles))
logging.debug(len(img_links))


def abs_url(rel_url):
    if rel_url.startswith("/r/"):
        return "https://www.reddit.com" + rel_url
    else:
        return rel_url


def img_link(url):
    url = abs_url(url)
    if url.startswith("http://i.imgur.com" or "https://i.imgur.com"):
        return url
    elif url.startswith("https://www.reddit.com/r/the_schulz"):
        page_req = requests.get(url, headers={'User-agent': 'SchulzBot'})
        page_req.raise_for_status()
        page = bs4.BeautifulSoup(page_req.text, "html.parser", from_encoding="utf-8")
        # logging.debug(type(page))
        prev = page.select(".preview")
        if len(prev) > 0:
            return prev[0].get("src")
        else:
            logging.warning("Unable to handle: " + url)
            return None
    elif url.startswith("https://youtu.be"):
        return url
    elif url.startswith("http://imgur.com" or "https://imgur.com"):
        page_req = requests.get(url, headers={'User-agent': 'SchulzBot'})
        page_req.raise_for_status()
        page = bs4.BeautifulSoup(page_req.text, "html.parser", from_encoding="utf-8")
        prev = page.select(".post-image-placeholder")
        logging.info(type(prev))
        logging.info(len(prev))
        return prev[0].get("src")
    else:
        logging.warning("Unable to handle: " + url)
        return None


posts = []

for titleN in range(len(titles)):
    logging.debug(titles[titleN].getText())
    # if (len(things[titleN].select("img")) > 0):
    #     logging.debug(things[titleN].select("img")[0].get("src"))
    # else:
    #     logging.debug(img_links[titleN].get("href"))
    p = [titles[titleN].getText(), img_link(img_links[titleN].get("data-href-url"))]
    posts.append(p)
    logging.debug(img_link(img_links[titleN].get("data-href-url")))

ff = webdriver.Firefox()
ff.get("https://web.whatsapp.com/")

# importlib.reload(whats_app_helper)

whats_app_helper.login(ff)
sleep(10)


def save_img(url, file_name):
    img = requests.get(url)
    img.raise_for_status()
    file = open(file_name.encode("utf-8"), 'wb')
    for chunk in img.iter_content(100000):
        file.write(chunk)
    file.close()


post_num = 0
logging.debug(open("titles.txt", "r", encoding="utf-8").read())

for title, img in posts:
    title = title.encode("ascii", 'xmlcharrefreplace').decode("utf-8")
    # title = title.encode("utf-8").decode("utf-8")
    logging.debug(open("titles.txt", "r", encoding="utf-8").read())

    if img is not None and title not in open("titles.txt", "r", encoding="utf-8").read():
        if img.startswith("//"):
            img = "http://" + img[2:]
        logging.info(title + ": " + img)
        img_path = os.path.join('', '/home', 'sermak', 'Desktop', "Schulz", title + ".png")
        save_img(img, img_path)
        open("titles.txt", "a", encoding="utf-8").write(title + "\n")
        time.sleep(10)
        whats_app_helper.send_text(ff, chat_name, "<--------------------")
        time.sleep(10)
        whats_app_helper.send_text(ff, chat_name, title)
        time.sleep(5)
        whats_app_helper.send_img(ff, chat_name, img_path)
        time.sleep(10)
        whats_app_helper.send_text(ff, chat_name, "-------------------->")
        sleep(10)
        post_num += 1
    else:
        logging.info(title + " already send")

if post_num == 0:
    logging.info("Nothing to send today :(")
else:
    logging.info("Send %i posts!   Schulz-Bot out" % post_num)
