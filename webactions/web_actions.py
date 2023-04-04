from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains

from dataclasses import dataclass

import time



class todoLocator:
    agree_yes = ".//*[contains(text(), 'I have read and agree to the')]"
    website_header = "header"

    
    
@dataclass
class registerWebActions(todoLocator):
    driver: any

    def getWeb(self, URL):
        self.driver.get(URL)

    def getTitle(self):
        return self.driver.title
    
    def addTask(self, 
                firstName, 
                lastName,
                email,
                telephone,
                password,
                password_confirm,
                ):

        action = ActionChains(self.driver)

       

        

        agree = self.driver.find_element(By.XPATH, self.agree_yes)

        header = self.driver.find_element(By.TAG_NAME, self.website_header)


        action.move_to_element(header)\
        .click()\
        .send_keys(Keys.TAB)\
        .send_keys(Keys.TAB)\
        .send_keys(Keys.TAB)\
        .send_keys(Keys.TAB)\
        .send_keys(Keys.TAB)\
        .send_keys(Keys.TAB)\
        .send_keys(firstName)\
        .send_keys(Keys.TAB)\
        .send_keys(lastName)\
        .send_keys(Keys.TAB)\
        .send_keys(email)\
        .send_keys(Keys.TAB)\
        .send_keys(telephone)\
        .send_keys(Keys.TAB)\
        .send_keys(password)\
        .send_keys(Keys.TAB)\
        .send_keys(password_confirm)\
        .send_keys(Keys.TAB)\
        .send_keys(Keys.TAB)\
        .click(on_element = agree)\
        .send_keys(Keys.TAB)\
        .send_keys(Keys.TAB)\
        .send_keys(Keys.ENTER)\
        .perform()

        time.sleep(10)