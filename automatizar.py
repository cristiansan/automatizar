#pip install selenium

 
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

prueba = webdriver.Chrome(executable_path=r'C:\Users\c.san.emeterio\Desktop\chromedriver.exe')

# prueba = webdriver.Chrome('chromedriver.exe')
# WebDriver driver = new ChromeDriver()
# prueba.get('http://www.cfp18.edu.ar/')
prueba.get('http://www.cfp18.edu.ar/contact.html')
# prueba.get('https://in.accenture.com/hispanicsouthamerica/?site=1&blog=359&p=29879')
time.sleep(3)
# prueba.finde_element_by_id('Enterprise ID *').send_keys('test')
prueba.find_element_by_id('nombre').send_keys('Matense Giles')
prueba.find_element_by_id('Telefono').send_keys('01144444444')
prueba.find_element_by_id('Email').send_keys('probando@gmail.com')
prueba.find_element_by_id('message').send_keys('Probando........................................')
# prueba.find_element_by_id('Enviar').send_keys(Keys.RETURN)

# python_button = driver.find_elements_by_xpath("//input[@name='lang' and @value='Python']")[0]
python_button = prueba.find_elements_by_xpath("//input[@name='Enviar' and @value='Enviar']")[0]
python_button.click()
 
time.sleep(30)
# prueba.quit()



# colors = ['ROJO', 'VERDE', 'AZUL', 'AMARILLO']

# for i, color in enumerate(colors):
# 	print(i, '-->', colors[i])
 

#for i in range(16):
#	print(i**2)   