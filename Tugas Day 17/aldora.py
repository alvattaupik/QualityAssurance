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
        browser.get("http://192.168.26.160:4080/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]").send_keys("mobilesw01") # isi username
        time.sleep(2)
        browser.find_element(By.CSS_SELECTOR,"input[placeholder='Password']").send_keys("1234") # isi password
        time.sleep(5)
        browser.find_element(By.ID,"submit").click() # klik tombol sign in
        time.sleep(2)


        # validasi
        #response_data = browser.find_element(By.ID,"swal2-title").text
        #response_message = browser.find_element(By.ID,"react-burger-menu-btn").text

        #self.assertIn('Welcome', response_data)
        #self.assertEqual(response_message, 'Open Menu')

   

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()