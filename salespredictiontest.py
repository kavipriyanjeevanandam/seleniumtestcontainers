import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from os import environ
from time import sleep

class LoginTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu') 
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument("--disable-software-rasterizer")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--disable-features=VizDisplayCompositor")
        chrome_options.add_argument("--disable-audio-output")
        chrome_options.add_argument("--disable-background-networking")
        chrome_options.add_argument("--disable-default-apps")
        chrome_options.add_argument("--disable-sync")
        chrome_options.add_argument("--disable-translate")
        chrome_options.add_argument("--disable-background-timer-throttling")
        chrome_options.add_argument("--disable-logging")
        chrome_options.add_argument("--disable-save-password-bubble")
        chrome_options.add_argument("--disable-gpu-sandbox")
        chrome_options.add_argument("--remote-debugging-address=0.0.0.0")
        chrome_options.add_argument("--remote-debugging-port=9222")
        environ["DISPLAY"] = ":99"
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("http://frontendcontainer:80")

    def invalid_email_type(self):
        email_input = driver.find_element(By.CSS_SELECTOR, "input[formControlName='email']")
        email_error_message = driver.find_element(By.XPATH, "//small[contains(text(),'Enter a valid email')]")
        email_input.send_keys("kavigmail")
        email_input.send_keys(Keys.TAB)  # Move focus out of the input field
        self.assertTrue(email_error_message.is_displayed())
    def valid_email_type(self):
        email_input = driver.find_element(By.CSS_SELECTOR, "input[formControlName='email']")
        email_error_message = driver.find_element(By.XPATH, "//small[contains(text(),'Enter a valid email')]")
        email_input.send_keys("kavipriyan@gmail")
        email_input.send_keys(Keys.TAB)  # Move focus out of the input field
        self.assertFalse(email_error_message.is_displayed())

    def test_invalid_password_length(self):
        # Find the password input field and the password error message element
        password_input = self.driver.find_element(By.CSS_SELECTOR, "input[formControlName='password']")
        password_error_message = self.driver.find_element(By.XPATH, "//small[contains(text(),'Password must be atleast 8 letters long')]")

        # Test Case: Verify that entering a too short password shows an error message
        password_input.send_keys("short")
        password_input.send_keys(Keys.TAB)  # Move focus out of the input field
        self.assertTrue(password_error_message.is_displayed())

    def test_valid_password_length(self):
        # Find the password input field and the password error message element
        password_input = self.driver.find_element(By.CSS_SELECTOR, "input[formControlName='password']")
        password_error_message = self.driver.find_element(By.XPATH, "//small[contains(text(),'Password must be atleast 8 letters long')]")

        # Test Case: Verify that entering a valid password length clears the error message
        password_input.clear()
        password_input.send_keys("validpassword")
        password_input.send_keys(Keys.TAB)  # Move focus out of the input field
        self.assertFalse(password_error_message.is_displayed())

    def test_successful_login(self):
        email_input = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="email"]')
        password_input = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="password"]')
        email_input.send_keys("kavi@gmail.com")
        password_input.send_keys("kavipriyan")
        login_button = driver.find_element(By.XPATH, '//button[.//span[contains(text(), "Login")]]')
        login_button.click()
        expected_url = "http://frontendcontainer/prediction"
        sleep(1)
        self.assertEqual(driver.current_url, expected_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
