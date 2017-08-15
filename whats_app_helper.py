#!/usr/bin/env python3

from selenium.webdriver.common.keys import Keys
import logging
import time

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')


def login(ff):
    while True:
        try:
            ff.find_element_by_class_name("qr-wrapper-container")
            logging.info("Please log in")
            time.sleep(10)
        except Exception:
            logging.info("Logged in")
            break


def click(ff, chat_name):
    chat_titles = ff.find_elements_by_css_selector(".chat .chat-title span")
    for title in chat_titles:
        if title.text == chat_name:
            title.click()
            break


def send_text(ff, chat_name, message):
    while True:
        click(ff, chat_name)
        try:
            input_field = ff.find_element_by_css_selector(".input")
            input_field.send_keys(message + Keys.ENTER)
            break
        except Exception:
            pass


def send_img(ff, chat_name, img_path):
    click(ff, chat_name)
    ff.find_element_by_css_selector(".icon-clip").click()
    # ff.find_element_by_css_selector(".icon-image").click()
    ff.find_element_by_css_selector("input[type='file']").send_keys(img_path)
    time.sleep(10)
    ff.find_element_by_css_selector(".icon-send-light").click()
