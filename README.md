# automatizar:

Gracias Mati Fortiniti por tu código, lo adapté un poquito en estas cosas:
- from selenium.webdriver.common.keys import Keys #para que me deje usar la tecla Enter para el botón.
- prueba = webdriver.Chrome(executable_path=r'C:\Users\c.san\Desktop\chromedriver.exe') #para que me tome el path del driver.
- python_button = prueba.find_elements_by_xpath("//input[@name='Enviar' and @value='Enviar']")[0] # para que haga click en el botón.

