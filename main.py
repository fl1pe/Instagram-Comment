import getpass
from instagram import Instagram
from selenium import webdriver
from time import sleep
from comment_list import COMMENT_LIST

URL = "https://www.instagram.com/p/CCZfJc9jbFz/"
USERNAME = "f_lipesousa"
PASSWORD = getpass.getpass("Digite sua senha: ")
COMMENT_NUMBER = 1000

COMMENT_LIST = COMMENT_LIST

USER_NUMBER_PER_COMMENT = 2

DRIVER = webdriver.Chrome('chromedriver_linux64/chromedriver')

INSTAGRAM = Instagram(DRIVER, URL)
INSTAGRAM.navigate()
INSTAGRAM.login(USERNAME, PASSWORD)
#INSTAGRAM.comment(COMMENT_LIST, USER_NUMBER_PER_COMMENT, COMMENT_NUMBER)
INSTAGRAM.comment(COMMENT_LIST)
