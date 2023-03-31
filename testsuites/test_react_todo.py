import unittest
import sys
sys.path.append(sys.path[0] + "/..")
import time
from webElements.webElements import todoWebActions

from settings.testSetup import Setting

settings = Setting()
todo = todoWebActions(settings.driver)




class testRun(unittest.TestCase):
    
    def testMe(self):
        settings.setUp()
        todo.getWeb("https://todomvc.com/examples/react/#/")

        title = todo.getTitle()

        self.assertIn("Todo", title, "Todo is not in title")
        

        todo.addTask("Omisola")
        todo.completeTask()
        todo.clearTask()


        settings.tearDown()

if __name__ == '__main__':

    unittest.main()


    # addTodo.send_keys( "Life is good with selenium", Keys.ENTER)
    # time.sleep(10)

    


        







        