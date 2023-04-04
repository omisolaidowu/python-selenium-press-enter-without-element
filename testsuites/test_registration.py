import unittest
import sys
sys.path.append(sys.path[0] + "/..")
import time
from webactions.web_actions import registerWebActions

from settings.testSetup import Setting

settings = Setting()
todo = registerWebActions(settings.driver)




class testRun(unittest.TestCase):
    
    def testMe(self):
        settings.setUp()
        todo.getWeb(
            "https://ecommerce-playground.lambdatest.io/index.php?route=account/register"
            )

        title = todo.getTitle()

        self.assertIn("Register", title, "Todo is not in title")
        

        todo.addTask("Idowu",
                      "Omisola",
                      "SoT65illIdowu@gmail.com",
                      "08034567782",
                      "123456789",
                      "123456789",
                      )
        settings.driver.current_url

        current_title = todo.getTitle()
        self.assertIn("Created", current_title, "Has Been Created is not in title")


        settings.tearDown()

if __name__ == '__main__':

    unittest.main()


    # addTodo.send_keys( "Life is good with selenium", Keys.ENTER)
    # time.sleep(10)

    


        







        