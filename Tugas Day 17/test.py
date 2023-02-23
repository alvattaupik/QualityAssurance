import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]").send_keys("standard_user") # isi username
        time.sleep(2)
        browser.find_element(By.CSS_SELECTOR,"#password").send_keys("secret_sauce") # isi password
        time.sleep(2)
        browser.find_element(By.ID,"login-button").click() # klik tombol sign in
        time.sleep(2)

        # validasi
        #response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"react-burger-menu-btn").text

        #self.assertIn('Welcome', response_data)
        self.assertEqual(response_message, 'Open Menu')

   

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()