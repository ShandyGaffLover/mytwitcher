from selenium import webdriver
import chromedriver_binary

username=''
password=''

driver = webdriver.Chrome()
driver.get('https://twitter.com/')

input_tag_of_username = driver.find_element_by_name('session[username_or_email]')
input_tag_of_username.send_keys(username)
input_tag_of_password = driver.find_element_by_name('session[password]')
input_tag_of_password.send_keys(password)
input_tag_of_password.submit()



