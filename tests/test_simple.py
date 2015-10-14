#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
# from selenium import webdriver
__author__ = 'acidroed'

# driver = webdriver.Firefox()

GOOGLE_LOGO = (By.XPATH, "//div[@id='hplogo']/div")
ukr = "u'Україна"
btn_ukr = "u'Увійти"
GOOGLE_BUTTON = (By.XPATH, "//a[@id='gb_70']")

def test_google_logo(app):
    # app.driver.maximize_window()
    el = app.driver.find_element(*GOOGLE_LOGO)
    assert el.text

def test_google_btn(app):
    # app.driver.maximize_window()
    el = app.driver.find_element(*GOOGLE_BUTTON)
    assert el.text == btn_ukr