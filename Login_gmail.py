# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 13:48:06 2017

@author: brook
This programe is used to log Gmail automaticlly.
I cannot login at the begnning, therefore, someone told me that I need to wait
2 second for DOM status change, he gave me this idea and provide sample code.
https://goo.gl/gM6f5q
"""

#login test
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,types
get_attr = lambda driver, e:driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', e)
#20170706 I don't know how this lambda function works.

account="rocktek.test@gmail.com"
pwd="rockmouse"
chromedriver = "/home/brook/python3/chromedriver"
#20170706. I don't konw how to install the webdriver and find it out on my computer.
#I found this method on internet
driver = webdriver.Chrome(chromedriver)
driver.get_attr=types.MethodType(get_attr,driver)
driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
print("Open gmail login page")
driver.find_element_by_id("identifierId").clear()
print("clear completed")
driver.find_element_by_id("identifierId").send_keys(account)
driver.find_element_by_id("identifierId").send_keys(Keys.ENTER)
print("finished ID input")
els=driver.find_elements_by_css_selector("[type='password']")
print(els)
print(driver.get_attr(els[0]))
# From els=.....to print(driver......) is used to print the status of DOM of HTML
time.sleep(2)
#According to other master told to me, I need to wait two second for DOM status change.
els=driver.find_elements_by_css_selector("[type='password']")
print(els)
print(driver.get_attr(els[0]))
# From els=.....to print(driver......) is used to print the status of DOM of HTML
driver.find_element_by_css_selector("[type='password']").send_keys(pwd)
driver.find_element_by_css_selector("[type='password']").send_keys(Keys.ENTER)

