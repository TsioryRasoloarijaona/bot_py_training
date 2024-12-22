from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from googletrans import Translator
import time


driver = webdriver.Chrome()


driver.get('https://web.whatsapp.com')
print("Scannez le QR code pour vous connecter à WhatsApp Web.")
time.sleep(15)  


contact_name = "3ISI"

try:
   
    contact = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, f"//span[@title='{contact_name}']"))
    )
    contact.click()
    print(f"La conversation avec '{contact_name}' est ouverte.")
    
    
    message_container_xpath = "(//div[contains(@class, 'message-in') or contains(@class, 'message-out')])"
    
    
    WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.XPATH, message_container_xpath))
    )
    
   
    messages = driver.find_elements(By.XPATH, message_container_xpath)
    
    last_message = messages[-2]
    
    
    last_message_text = last_message.find_element(By.XPATH, ".//div[contains(@class, 'copyable-text')]").text
    translator = Translator()
    translated_message = translator.translate(last_message_text , src='auto' , dest='fr').text
    print("web element :")
    print(last_message)
    print("************************************************************************")
    print("Dernier message reçu (original):")
    print(last_message_text)
    print('*************************************************************************')
    print("Dernier message reçu (francais):")
    print(translated_message)
    
except Exception as e:
    print(f"Erreur : {e}")

input("Appuyez sur Entrée pour quitter...")
driver.quit()
