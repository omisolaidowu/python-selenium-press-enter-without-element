from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains

import time



# class todoLocator:
#     First_Name = "//input[@placeholder='First Name']"
#     Last_Name = "//input[@placeholder='Last Name']"
#     Email = "//input[@placeholder='E-Mail']"
#     Phone = "//input[@placeholder='Telephone']"
#     Password = "//input[@placeholder='Password']"
#     Password_Confirm = "//input[@placeholder='Password Confirm']"
#     Subscribe_yes = ".//*[contains(text(), 'Yes')]"
#     Agree_Yes = ".//*[contains(text(), 'I have read and agree to the')]"
#     Submit_Button ="//input[@value='Continue']"

class todoLocator:
    First_Name = 'input[placeholder=\"First Name\"]'
    Last_Name = 'input[placeholder=\"Last Name\"]'
    Email = 'input[placeholder=\"E-Mail\"]'
    Phone = 'input[placeholder=\"Telephone\"]'
    Password = 'input[placeholder=\"Password\"]'
    Password_Confirm = 'input[placeholder=\"Password Confirm\"]'
    Subscribe_yes = ".//*[contains(text(), 'Yes')]"
    Agree_Yes = ".//*[contains(text(), 'I have read and agree to the')]"
    Submit_Button ='input[value=\"Continue\"]'



class registerWebActions(todoLocator):
    def __init__(self, driver) -> None:
        self.driver = driver
        
    def getWeb(self, URL):
        self.driver.get(URL)

    def getTitle(self):
        return self.driver.title
   
        
    def inputfirstName(self, firstName):     
        first_name_field = self.driver.execute_script(
            "return document.querySelector('{}');".format(self.First_Name)
            )
        
        return self.driver.execute_script(
            "arguments[0].value='{}';".format(firstName),
              first_name_field
        )
        
        
    def inputlastName(self, lastName):    
        last_name_field = self.driver.execute_script(
            "return document.querySelector('{}');".format(self.Last_Name)
            )
        
        return self.driver.execute_script(
            "arguments[0].value='{}';".format(lastName),
              last_name_field
        )
    
        
    def inputEmail(self, email):
        Email_field = self.driver.execute_script(
            "return document.querySelector('{}');".format(self.Email)
            )
        
        return self.driver.execute_script(
            "arguments[0].value='{}';".format(email),
              Email_field
        )
    
    def inputPhone(self, phone):
        phone_field = self.driver.execute_script(
            "return document.querySelector('{}');".format(self.Phone)
            )
        return self.driver.execute_script(
            "arguments[0].value='{}';".format(phone),
              phone_field
        )
    
    def inputPassword(self, password):
        password_field = self.driver.execute_script(
            "return document.querySelector('{}');".format(self.Password)
            )
        return self.driver.execute_script(
            "arguments[0].value='{}';".format(password),
              password_field
        )

    
    def inputpasswordConfirm(self, password_confirm):
        password_confirm_field = self.driver.execute_script(
            "return document.querySelector('{}');".format(self.Password_Confirm)
            )
        return self.driver.execute_script(
            "arguments[0].value='{}';".format(password_confirm),
              password_confirm_field
        )
        
    
    def subScribe(self):
        subscribebox = self.driver.find_element(By.XPATH, self.Subscribe_yes)
        return self.driver.execute_script("arguments[0].click()", subscribebox)

    def agreetoTerms(self):
        agree_field = self.driver.find_element(By.XPATH, self.Agree_Yes)
        return self.driver.execute_script("arguments[0].click()", agree_field)

    def submit(self):
        submit_button = self.driver.execute_script(
            "return document.querySelector('{}')".format(self.Submit_Button)
            )
        self.driver.execute_script("arguments[0].click()", submit_button)
        time.sleep(10)

        

