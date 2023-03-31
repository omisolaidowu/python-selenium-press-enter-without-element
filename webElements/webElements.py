from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains

from dataclasses import dataclass



class todoLocator:
    addTodo = "new-todo"
    completeTodo = "toggle"
    clearTodo = "clear-completed"
    

@dataclass
class todoWebActions(todoLocator):
    driver: any

    def getWeb(self, URL):
        self.driver.get(URL)

    def getTitle(self):
        return self.driver.title
    
    def addTask(self, task):
        todoInput = self.driver.find_elements(By.CLASS_NAME, self.addTodo)

        # completeTodo = self.driver.find_element(By.CLASS_NAME, self.addTodo)

        # clearTodo = self.driver.find_element(By.CLASS_NAME, self.clearTodo)
        
        action = ActionChains(self.driver)

        action.send_keys(task)\
        .send_keys(Keys.ENTER)\
        .perform()


    # def addTask(self, task):
    #     self.driver.find_element(By.CLASS_NAME, self.addTodo).send_keys(task, Keys.RETURN)

    def completeTask(self):
        self.driver.find_element(By.CLASS_NAME, self.completeTodo).click()

    def clearTask(self):
        self.driver.find_element(By.CLASS_NAME, self.clearTodo).click()