from selenium import webdriver
from browser import Browser
from pages.herolo_page import HeroloPage

def before_all(context):
    context.browser = Browser()
    context.home_page = HeroloPage()

def after_all(context):
    context.browser.close()
