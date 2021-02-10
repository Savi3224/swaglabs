from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

driver: WebDriver = webdriver.Chrome("C:\\Chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
element = driver.find_element_by_name("user-name")
element.send_keys("standard_user")
element = driver.find_element_by_name("password")
element.send_keys("secret_sauce")
element = driver.find_element_by_class_name("btn_action").click()
element = driver.find_element_by_xpath("//body/div[@id='page_wrapper']/div[@id='contents_wrapper']/div["
                                       "@id='inventory_container']/div[1]/div[2]/div[1]/div[1]/div[3]/button["
                                       "1]").click()
element = driver.find_element_by_xpath("//body[1]/div[1]/div[2]/div[1]/div[2]/a[1]/svg[1]/path[1]").click()  #Error in the xpath
element = driver.find_element_by_xpath("//a[contains(text(),'CHECKOUT')]").click()
driver.close()
driver.quit()



