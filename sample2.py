from selenium import webdriver
import time
class radiobutton():
    def test(self):
        driver=webdriver.Chrome()
        driver.get("http://google.com")
        driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input").send_keys("lets kode it practice")
        time.sleep(5)
        driver.find_element_by_name("btnK").click()
        driver.maximize_window()
        time.sleep(10)
        driver.find_element_by_class_name("LC20lb").click()
        time.sleep(5)

ff=radiobutton()
ff.test()
