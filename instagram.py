from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import random


class Instagram:
    def __init__(self, driver, url_instagram_post):

        self.__driver = driver
        self.__url_instagram = 'https://www.instagram.com/'
        self.__url_intagram_post = url_instagram_post

        # Elements of the intagram login page #xPath
        self.__input_user_name = 'username'  # name
        self.__input_user_password = 'password'  # name
        # xPath
        self.__btn_login = '//*[@id="loginForm"]/div/div[3]/button'

        # Elements of the intagram post page #xPath

        self.__input_comment = 'Ypffh'  # class
        self.__btn_post_comment = '#react-root > section > main > div > div.ltEKP > article > div > div.eo2As > section.sH9wk._JgwE > div > form > button'

    def navigate(self):
        self.__driver.get(self.__url_instagram)
        sleep(2)

    def login(self, user_name, password):
        
        print("Login Intagram")
        self.__driver.find_element_by_name(
            self.__input_user_name).send_keys(user_name)
        self.__driver.find_element_by_name(
            self.__input_user_password).send_keys(password)
        self.__driver.find_element_by_xpath(self.__btn_login).click()
        sleep(5)
        #Fecha o 1º pop-up depois do login realizado.
        self.__driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        sleep(6)
        #Fecha o 2º pop-up depois do login realizado.
        self.__driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm').click()
        sleep(3)
        self.__driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]/div').click()
        sleep(3)
        self.__driver.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.QY4Ed > input').send_keys('rickellmyc' + Keys.ENTER)
        sleep(3)
        self.__driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div').click()
        sleep(6)
        self.__driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]/article/div/div/div[1]/div[1]/a/div[1]/div[2]').click()
        sleep(5)
    def navigate_to_post(self):
        self.__driver.get(self.__url_intagram_post)
        sleep(2)

    '''def comment(self, comments_list, user_number_per_comment, comment_number=1):
        print("Comment")
        comments_list_copy = comments_list [:]

        for i in range(comment_number):

            if len(comments_list_copy) == 0:
                comments_list_copy = comments_list[:]
            choiceusers_name_post = self.__choice_users_name_post(
                comments_list_copy, user_number_per_comment)
            
            self.__driver.find_element_by_class_name(
                self.__input_comment).click()
            for element in choiceusers_name_post:

                self.__driver.find_element_by_class_name(
                    self.__input_comment).send_keys(f'{element} ')
            sleep(2)
            self.__driver.find_element_by_css_selector(
                self.__btn_post_comment).click()
            print(f'Comentario de numero {i+1} => {choiceusers_name_post}')
            sleep(8)
            self.__driver.refresh()
            sleep(60+randrange(0, 9))'''

    def comment(self, comments_list, user_number_per_comment=False, comment_number=False):
        comments_list_copy = comments_list [:]
        self.__driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea').click()
        
        contador = 0
        while contador < 5:
            for i in comments_list_copy:
                i = random.choice(comments_list_copy)
                self.__driver.refresh()
                sleep(2)
                self.__driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[2]/button').click()
                self.__driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea').send_keys(f'@{i}')
                sleep(3)
                self.__driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button[2]').click() 
                sleep(20)
                
            contador + 1
            