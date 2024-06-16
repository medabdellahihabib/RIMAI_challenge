from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logging.basicConfig(level=logging.INFO)

def scrape_facebook_marketplace(email, password):
    chromedriver_path = "C:/Users/Dell/Downloads/chromedriver-win64 (2)/chromedriver-win64/chromedriver.exe"
    
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--headless") 
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
   
   
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        
        logging.info("Opening Facebook login page")
        driver.get("https://www.facebook.com/login")

        logging.info("Entering login credentials")
        email_input = driver.find_element(By.ID, "email")
        password_input = driver.find_element(By.ID, "pass")
        email_input.send_keys(email)
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)

        time.sleep(10)
        logging.info("Navigating to Facebook Marketplace vehicles category")
        driver.get("https://www.facebook.com/marketplace/category/vehicles")

        time.sleep(10)  
        elements = driver.find_elements(By.CLASS_NAME, 'x9f619.x78zum5.x1r8uery.xdt5ytf.x1iyjqo2.xs83m0k.x1e558r4.x150jy0e.xiiorvi4.xjkvuk6.xnpuxes.x291uyu.x1uepa24')

        for ele in elements:
            print(ele.text)
            print(ele.get_attribute('outerHTML'))

            print(ele.get_attribute('title'))
            img_tags = ele.find_elements(By.TAG_NAME, 'img')
            for img in img_tags:
                print(img.get_attribute('src'))

    except Exception as e:
        logging.error(f"An error occurred: {e}")

    finally:
        driver.quit()

email = ".............."
password = "..........."

scrape_facebook_marketplace(email, password)


for ele in elements:
    print(ele.text)
    display(HTML(ele.get_attribute('outerHTML')))
    print(ele.get_attribute('title'))
    
    img_tags = ele.find_elements(By.TAG_NAME, 'img')
    for img in img_tags:
        print(img.get_attribute('src'))

scrape_facebook_marketplace("...........", "..........")

