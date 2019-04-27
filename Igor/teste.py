import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()

chrome_patch = r'C:\Users\igora\PycharmProjects\Driver\chromedriver.exe'
driver = webdriver.Chrome(chrome_patch)
driver.get('https://google.com')
driver.create_options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-infobars")
# driver.maximize_window()

# pyautogui.hotkey('Ctrl', 't')
driver.get('https://globo.com')
time.sleep(3)
driver.switch_to_window(driver.window_handles[-1])
driver.close()
time.sleep(3)
# driver.find_element(By.CSS_SELECTOR('body')).send_keys(Keys.CONTROL + 't')



handle = driver.window_handles

# Título da janela atual


# Trocar para a última janela da lista
driver.switch_to_window_handles(driver.window_handles[-1])


# Fechar a janela atual
driver.close()
# Voltar para a janela do Google
driver.switch_to_window_handles(driver.window_handles[-1])



# E como saber o ID da janela atual? Simples!
driver.current_window_handle


# time.sleep(2)
# pyautogui.hotkey('Ctrl', 't')
# time.sleep(2)
# pyautogui.hotkey('Ctrl', 'w')

# driver.execute(pyautogui.hotkey('Ctrl', 't'))

time.sleep(5)
driver.quit()
