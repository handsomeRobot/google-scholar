#coding=utf-8
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8')

from splinter.browser import Browser

url = "https://scholar.google.com.hk/"
browser = Browser(driver_name = "chrome")

key_a = ["ion-implantation", "ferroelectric", "negative capacitance", "doping"]
key_b = ["2D materials", "MoS2"]
items = []
for keya in key_a:
    for keyb in key_b:
        items.append(keya + " " + keyb)

browser.visit(url)

for item in items:
    browser.fill("q", item + "\n")
    sleep(60)

    




