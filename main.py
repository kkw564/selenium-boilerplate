import env
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions


edge_options = EdgeOptions()
edge_options.use_chromium = True
edge_options.add_experimental_option("detach", True)

JANGINTHE_LOGIN_URL = 'http://www.janginthe.com/member/login.html'

JANGINTHE_YAKGWA_URL = 'http://www.janginthe.com/product/%EC%9D%98%EC%A0%95%EB%B6%80-%EC%9E%A5%EC%9D%B8%ED%95%9C%EA%B3%BC-%EB%AA%BB%EB%82%9C%EC%9D%B4-%EC%95%BD%EA%B3%BC-%ED%8C%8C%EC%A7%80%EC%95%BD%EA%B3%BC/260/category/28/display/1/'
JANGINTHE_YAKGWA_BREAD_URL = 'http://www.janginthe.com/product/%EC%9E%A5%EC%9D%B8%EB%8D%94-%EC%95%BD%EA%B3%BC%EB%B9%B5/258/category/24/#none'
JANGINTHE_BUY_URL = JANGINTHE_YAKGWA_URL

BUY_XPATH = '//*[@id="contents"]/div[2]/div[2]/div[2]/div[6]/div[1]/a[1]'

driver = webdriver.Chrome("./chromedriver")

driver.get(JANGINTHE_LOGIN_URL)
driver.find_element(By.XPATH, '//*[@id="member_id"]').send_keys(env.ID)
driver.find_element(By.XPATH, '//*[@id="member_passwd"]').send_keys(env.PASSWORD)
driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div/form/div/div/fieldset/a').click()
time.sleep(3)

driver.get(JANGINTHE_BUY_URL)

time.sleep(0.1)
driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div/div[2]/div[2]/div[2]/div[4]/table/tbody[1]/tr/td[2]/span/input').send_keys(Keys.CONTROL + "a")
driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div/div[2]/div[2]/div[2]/div[4]/table/tbody[1]/tr/td[2]/span/input').send_keys(Keys.DELETE)
driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div/div[2]/div[2]/div[2]/div[4]/table/tbody[1]/tr/td[2]/span/input').send_keys("1")
driver.execute_script("document.getElementsByClassName('first')[1].style.cssText = 'display:block !important';")
time.sleep(0.1)

count = 0
while True:
  if count > 10000:
    break
  print("count : ", count)
  count += 1
  try:
    driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div/div[2]/div[2]/div[2]/div[6]/div[1]/a[1]').send_keys(Keys.ENTER)
    time.sleep(0.1)
    driver.switch_to.alert.accept()
  except:
    break

driver.find_element(By.XPATH, '/html/body/form[1]/div/div[10]/div/div[1]/input').click()
time.sleep(0.1)
driver.find_element(By.XPATH, '/html/body/form[1]/div/div[11]/button').send_keys(Keys.ENTER)
time.sleep(0.1)
