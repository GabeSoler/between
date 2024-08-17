from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import override_settings
import time



MAX_WAIT = 10


class HomePageTest(StaticLiveServerTestCase):
    """ I set this one up following django docs. One big difference is to use 'live_server_url to find the pages"""
    fixtures = ["PersonalStyleGroup.yaml", "PersonalStyleSection.yaml"]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Firefox()
        cls.wait = WebDriverWait(cls.selenium, timeout=2,poll_frequency=.2)
        cls.selenium.implicitly_wait(2)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def wait_for_id(self,id):
        start_time = time.time()
        while True:
            try:
                self.selenium.find_element(By.ID,id)
                return
            except (AssertionError, self.failureException):
                if time.time() - start_time > MAX_WAIT:
                    raise
                time.sleep(1)

    @override_settings(DEBUG=True)
    def test_title(self):    
        #user arrives to CreaTherapy
        self.selenium.get(f"{self.live_server_url}/")
        self.selenium.find_element(By.LINK_TEXT,"Read the theory")
        self.assertEqual(self.selenium.title, "CreaTherapy")
        #user reads a little intro
        self.selenium.find_element(By.ID,"welcome-no-authenticated")
        #user sees a menu
        nav = self.selenium.find_element(By.ID,"top-nav-bar")
        self.assertIn("MY TESTS",nav.text)

        
    @override_settings(DEBUG=True)
    def test_arrive_to_test(self):
        #user presses a link for a test
        self.selenium.get(f"{self.live_server_url}/")
        test_link = self.selenium.find_element(By.LINK_TEXT,"Take a profile test")
        self.wait.until(lambda d: test_link.is_displayed())
        actions = ActionChains(self.selenium)
        actions.move_to_element(test_link)
        #actions.click()
        actions.key_down(Keys.ENTER)
        actions.key_up(Keys.ENTER)        
        actions.perform()
        #user takes the test
        time.sleep(1)
        self.assertEqual(self.selenium.current_url,f"{self.live_server_url}/profile_test/" )
    
    def test_take_profile_test(self):
        self.selenium.get(f"{self.live_server_url}/profile_test/")
        self.assertEqual(self.selenium.title, "Profiles Test")
        slider = self.selenium.find_elements(By.CLASS_NAME,"form-range")
        actions = ActionChains(self.selenium)
        for s in slider:
            self.wait.until(lambda d: s.is_displayed())
            actions.move_to_element(s)
            actions.key_down(Keys.ARROW_RIGHT)
            actions.key_up(Keys.ARROW_RIGHT)
        #user sends the test
        actions.send_keys(Keys.TAB)
        actions.key_down(Keys.ENTER)
        actions.key_up(Keys.ENTER)
        actions.perform()
        results = self.selenium.find_element(By.ID,"results-card")
        self.wait.until(lambda d: results.is_displayed())
        self.assertIn(results, "Description")
        #user goes to sign up exited
    
    def test_move_to_sign_up(self):
        signup = self.selenium.find_element(By.ID,"signup-link")
        actions = ActionChains(self.selenium)
        actions.move_to_element(signup)
        actions.key_down(Keys.ENTER)
        actions.key_up(Keys.ENTER)
        actions.perform()
        self.selenium.find_element(By.ID,"id_username")

    def test_sign_up(self):
        username = self.selenium.find_element(By.ID,"id_username")
        actions = ActionChains(self.selenium)
        actions.move_to_element(username)
        actions.send_keys("testinguser")        
        password1 = self.selenium.find_element(By.ID,"id_password1")
        actions.move_to_element(password1)
        actions.send_keys("BLA&%%user234")
        password2 = self.selenium.find_element(By.ID,"id_password2")
        actions.move_to_element(password2)
        actions.send_keys("BLA&%%user234")
        actions.perform()

        #user finds its test recorded




