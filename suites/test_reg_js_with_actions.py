import sys
sys.path.append(sys.path[0] + "/..")
from webactions.javaScript_web_actions import registerWebActions
from settings.Setup import Setting
settings = Setting()
webactions = registerWebActions(settings.driver)

class TestUserReg():
    def test_user_registration(self):
        settings.setUp()
        webactions.getWeb(
            "https://ecommerce-playground.lambdatest.io/index.php?route=account/register"
            )

        title = webactions.getTitle()
        assert "Register" in title, "Todo is not in title"
        webactions.inputfirstName("Idowu")
        webactions.inputlastName("Omisola")
        webactions.inputEmail("idowuomi123Test@gmail.com")
        webactions.inputPhone("08044554455")
        webactions.inputPassword("12345678")
        webactions.inputpasswordConfirm("12345678")
        webactions.agreetoTerms()
        webactions.submit() 
        settings.driver.current_url

        current_title = webactions.getTitle()
        assert "Created" in current_title, "Created is not in title"

        settings.tearDown()