from selenium import webdriver
from time import sleep

class GitAuto():
    def __init__(self):
        self.username = input("Quel est votre username Github :")
        self.password = input("Quel est votre mot de passe Github :")
        self.repository = input("Quel est le nom du nouveau repository ? :")
        self.driver = webdriver.Chrome("/Users/guillaume/venv/bin/chromedriver")

    def login(self):
        self.driver.get("https://github.com/")

        connect_btn = self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]')
        connect_btn.click()

        user_in = self.driver.find_element_by_xpath('//*[@id="login_field"]')
        user_in.send_keys(self.username)

        pass_in = self.driver.find_element_by_xpath('//*[@id="password"]')
        pass_in.send_keys(self.password)

        log_btn = self.driver.find_element_by_xpath('//*[@id="login"]/form/div[3]/input[8]')
        log_btn.click()

        new_repository_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a')
        new_repository_btn.click()

        
        name_repository = self.driver.find_element_by_xpath('//*[@id="repository_name"]')
        name_repository.send_keys(self.repository)

        sleep(2)

        validate_btn = self.driver.find_element_by_xpath('//*[@id="new_repository"]/div[3]/button')
        validate_btn.click()


connect = GitAuto()
connect.login()