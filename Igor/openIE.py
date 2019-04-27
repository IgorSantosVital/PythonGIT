from selenium import webdriver
import time
import webbrowser

#ie = webbrowser.get(webbrowser.iexplore)
#ie.open('https://oisistemas.extranet/')
webbrowser
ie_patch = r'C:\Users\igora\PycharmProjects\Driver\IEDriverServer'
driver = webdriver.Ie(ie_patch)
driver.maximize_window()
driver.get('http://globo.com/')
time.sleep(10)

#usuario = 
#senha = input('Digite Senha:')

#efetuar login citrix
driver.find_element_by_class_name('hui-premium__title').click()
driver.find_element_by_xpath('//*[@id="Enter user name"]').send_keys(usuario)
time.sleep(1)
driver.find_element_by_id('passwd').send_keys(senha)
driver.find_element_by_id('Log_On').click()
time.sleep(7)

#abrir o SAP
driver.find_element_by_xpath('//*[@id="myapps-container"]/div[9]/div[2]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="myapps-container"]/div[24]/div[3]').click()