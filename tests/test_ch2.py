'''
Learnign basics of automation testing with python.
I am using this video: https://www.youtube.com/watch?v=73qAGhXu5mM

I am not able to accept google cookies.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_google_search():
    driver = webdriver.Chrome()

    #1. go to google.com
    driver.get('https://google.com')
    time.sleep(3)

    driver.find_element(By.XPATH, "//span[contains(text(), 'Přijmout vše')]").click()

    #2. type in search 'puppies
    driver.find_element(By.NAME, 'q').send_keys('puppies')

    #3. submit or enter the search
    driver.find_element(By.NAME, 'btnK').submit()

    #4. assert we got a search page for puppies
    assert 'puppies' in driver.title