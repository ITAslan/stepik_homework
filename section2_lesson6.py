import math
import time

from selenium import webdriver
  
browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/get_attribute.html')
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element_by_tag_name('img')
x = x_element.get_attribute('valuex')
y = calc(x)
input1 = browser.find_element_by_id('answer').send_keys(y)
check1 = browser.find_element_by_id('robotCheckbox').click()
check2 = browser.find_element_by_id('robotsRule').click()
check3 = browser.find_element_by_css_selector('.btn-default').click()
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()