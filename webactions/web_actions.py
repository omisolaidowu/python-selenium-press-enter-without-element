from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains

import time

class todoLocator:
    agree_yes = ".//*[contains(text(), 'I have read and agree to the')]"
    website_header = "header"

class registerWebActions(todoLocator):
    def __init__(self, driver) -> None:
        self.driver = driver
        self.action = ActionChains(self.driver, duration=2500)
        
    def getWeb(self, URL):
        self.driver.get(URL)

    def getTitle(self):
        return self.driver.title
    
    def navigatetoForm(self):
        header = self.driver.find_element(By.TAG_NAME, self.website_header)
        return self.action.move_to_element(header)\
        .click()\
        .send_keys(Keys.TAB)\
        .send_keys(Keys.TAB)\
        .send_keys(Keys.TAB)\
        .send_keys(Keys.TAB)\
        .send_keys(Keys.TAB)\
        .send_keys(Keys.TAB)
    
    def presstabOnce(self):
        return self.action.send_keys(Keys.TAB)
    
    def presstabTwice(self):
        return self.action.send_keys(Keys.TAB)\
        .send_keys(Keys.TAB)
        
    def inputfirstName(self, firstName):
        return self.action.send_keys(firstName)
        
    def inputlastName(self, lastName):
        return self.action.send_keys(lastName)
        
    def inputEmail(self, email):
        return self.action.send_keys(email)
    
    def inputPhone(self, phone):
        return self.action.send_keys(phone)
    
    def inputPassword(self, password):
        return self.action.send_keys(password)
    
    def inputpasswordConfirm(self, password_confirm):
        return self.action.send_keys(password_confirm)
        
    def agreetoTerms(self):
        agree = self.driver.find_element(By.XPATH, self.agree_yes)
        return self.action.click(on_element = agree)

    def submit(self):
        self.action.send_keys(Keys.ENTER)

    def executeactionChain(self):
        self.action.perform()
        time.sleep(10)

