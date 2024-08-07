from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from django.test.testcases import LiveServerTestCase
import time
from django.test import override_settings


#TODO: arrive to sign up. I am trying to test my new function that allows to save a test
#TODO: write the tests in unitest too, however I think only testing the templats and correct functions is enough, as this one tests overall functionality

class HomePageTest(LiveServerTestCase):
    """ I set this one up following django docs. One big difference is to use 'live_server_url to find the pages"""
    fixtures = ["PersonalStyleGroup.yaml", "PersonalStyleSection.yaml"]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
        cls.selenium.implicitly_wait(2)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_title(self):    
        time.sleep(1) # Let the user actually see something!
        #user arrives to CreaTherapy
        self.selenium.get(f"{self.live_server_url}/")
        self.assertEqual(self.selenium.title, "CreaTherapy")
        #user reads a little intro
        self.selenium.find_element(By.ID,"welcome-no-authenticated")
        #user sees a menu
        nav = self.selenium.find_element(By.ID,"top-nav-bar")
        self.assertIn("MY TESTS",nav.text)
        
    @override_settings(DEBUG=True)
    def test_take_test_and_signup(self):
        #user presses a link for a test
        self.selenium.get(f"{self.live_server_url}/")
        test_link = self.selenium.find_element(By.LINK_TEXT, "Take a profile test")
        test_link.click()
        #user takes the test
        slider = self.selenium.find_elements(By.CLASS_NAME,"form-range")
        actions = ActionChains(self.selenium)
        for s in slider:
            actions.move_to_element(s)
            actions.key_down(Keys.ARROW_RIGHT)
            actions.key_up(Keys.ARROW_RIGHT)
        #user sends the test
        actions.send_keys(Keys.TAB)
        actions.key_down(Keys.ENTER)
        actions.key_up(Keys.ENTER)
        actions.perform()
        time.sleep(5)
        self.selenium.find_element(By.ID,"results-card")
        #user goes to sign up exited
        signup = self.selenium.find_element(By.ID,"signup-link")
        actions.move_to_element(signup)
        actions.key_down(Keys.ENTER)
        actions.key_up(Keys.ENTER)
        actions.perform()
        signup = self.selenium.find_element(By.ID,"id_username")

        #user finds its test recorded




