import sys
sys.path.append(sys.path[0] + "/..")
from webactions.web_actions import registerWebActions
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

        webactions.navigatetoForm() 
        webactions.inputfirstName("Idowu")
        webactions.presstabOnce()
        webactions.inputlastName("Omisola")
        webactions.presstabOnce()
        webactions.inputEmail("Testershashranda667yytr7dton@gmail.com")
        webactions.presstabOnce()
        webactions.inputPhone("08044554455")
        webactions.presstabOnce()
        webactions.inputPassword("12345678")
        webactions.presstabOnce()
        webactions.inputpasswordConfirm("12345678")
        webactions.presstabTwice()
        webactions.agreetoTerms()
        webactions.presstabTwice()
        webactions.submit()
        webactions.executeactionChain()

        settings.driver.current_url

        current_title = webactions.getTitle()
        assert "Created" in current_title, "Created is not in title"

        settings.tearDown()