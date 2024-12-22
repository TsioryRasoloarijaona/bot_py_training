from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://www.facebook.com/login')


try :
    email_input =WebDriverWait(driver , 30).until(
    EC.presence_of_element_located((By.ID , "email"))

    ) 
    email_input.send_keys("phone number or email")

    password_input =WebDriverWait(driver , 30).until(
    EC.presence_of_element_located((By.ID , "pass"))
    )
    password_input.send_keys("password")

    boutton = driver.find_element(By.ID , "loginbutton")
    boutton.click() ;

except Exception as e:
    print(f"Erreur : {e}")

finally :
    input('press enter to close...')