# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 00:11:30 2018

@author: appu
"""

from selenium import webdriver

driver = webdriver.Chrome("H:\\chromedriver.exe")
driver.set_page_load_timeout(30)

driver.get("https://www.github.com/login")
driver.maximize_window()
driver.implicitly_wait(20)
#driver.get_screenshot_as_file("github_screenshot.png")
driver.find_element_by_id("login_field").send_keys("mahadevan.rajamani@gmail.com")
driver.find_element_by_id("password").send_keys("Ods@5649")
driver.find_element_by_name("commit").click()
driver.quit()
