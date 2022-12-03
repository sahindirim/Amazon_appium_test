from appium import webdriver
# For W3C actions
from desired_cap import desired_cap as cap
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from appium.webdriver.common.appiumby import AppiumBy as By
import time

class Amazon_test(webdriver):

    def __init__(self, driver_path = webdriver.Remote("http://127.0.0.1:4723/wd/hub",cap.desired_cap)):
        self.driver = driver_path
        self.driver.implicitly_wait(15)
    def test_login(self):
        #fill your login information
        pass
    def test_scenario_1(self):
        #Scrool
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(531, 2004)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(543, 1198)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        # scroll botton
        actions.w3c_actions.pointer_action.move_to_location(918, 1468)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(463, 1474)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        self.driver.find_element(By.XPATH,"//android.widget.TextView[@bounds='[645,1182][888,1395]']").click()  # Click health
        price_on_menu = self.driver.find_element(By.XPATH,"//android.widget.Image[@bounds='[60,744][411,1257]']").get_attribute('text')
        self.driver.find_element(By.XPATH,"//android.widget.Image[@bounds='[60,744][411,1257]']").click()  # Click first product
        self.driver.find_element(By.XPATH, "//android.widget.Button[@bounds='[243,975][981,1113]']").click()  # add to cart
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//android.widget.TextView[@bounds='[610,2073][742,2139]']").click()  # add to cart

        cart_check = self.driver.find_element(By.XPATH,"//android.widget.TextView[@bounds='[610,2073][742,2139]']").get_attribute('text')  # verify cart
        price_on_cart = self.driver.find_element(By.XPATH,"//android.widget.TextView[@bounds='[483,1164][750,1245]']").get_attribute('text')  # verify price
        assert cart_check == 1
        assert price_on_menu == price_on_cart

        self.driver.find_element(By.XPATH, "//android.widget.Image[@bounds='[60,1386][159,1479]']").click()  # delete to cart

        cart_check = self.driver.find_element(By.XPATH,"//android.widget.TextView[@bounds='[669,2100][695,2139]']").get_attribute('text')  # verify cart
        assert cart_check == 0

    def test_scenario_2(self):
        #click your login info
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(570, 2050)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(591, 440)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        actions.w3c_actions.pointer_action.move_to_location(1019, 822)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(156, 808)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        actions.w3c_actions.pointer_action.move_to_location(935, 863)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(649, 857)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        self.driver.find_element(By.XPATH,"//android.widget.TextView[@bounds='[849,789][981,888]']").click()  #
        for i in range(2):
            actions.w3c_actions.pointer_action.move_to_location(1019, 877)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(69, 872)
            actions.w3c_actions.pointer_action.release()
            actions.perform()

        self.driver.find_element(By.XPATH, "//android.widget.Button[@bounds='[399,846][972,894]']").click()
        self.driver.find_element(By.XPATH, "//android.widget.RelativeLayout[@bounds='[0,2070][1080,2139]']").click()
        self.driver.find_element(By.XPATH, "//android.widget.Image[@bounds='[48,1077][489,1401]']").click() # Select highest one


class BoxTestCases:
    pass