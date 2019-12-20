#pip install selenium
 
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

prueba = webdriver.Chrome(executable_path=r'C:\Users\c.san\Desktop\chromedriver.exe')

prueba.get('http://www.cfp18.edu.ar/contact.html')
time.sleep(3)
prueba.find_element_by_id('nombre').send_keys('Matense Giles')
prueba.find_element_by_id('Telefono').send_keys('01144444444')
prueba.find_element_by_id('Email').send_keys('probando@gmail.com')
prueba.find_element_by_id('message').send_keys('Probando........................................')
# prueba.find_element_by_id('Enviar').send_keys(Keys.RETURN)
python_button = prueba.find_elements_by_xpath("//input[@name='Enviar' and @value='Enviar']")[0]
python_button.click()
 
time.sleep(30)