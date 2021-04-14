from selenium import webdriver 
from time import sleep

browser = webdriver.Firefox() 
browser.get('https://leader.ignaciopardo.repl.co/')
element = browser.find_element_by_id('arrow') 
element.click()


#on start
sleep(3)
mp_btn = browser.find_element_by_class_name('mercadopago-button') 
mp_btn.click()
sleep(7)
iframe = browser.find_element_by_id('mercadopago-checkout') 
browser.switch_to_frame(iframe)

pay = browser.find_element_by_id('mercadopago-checkout') 
pay.click()