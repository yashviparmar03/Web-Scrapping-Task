from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import csv
import os

# --- SETUP CHROME DRIVER ---
chrome_driver_path = "C:/Users/Yashvi/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"  # <-- Change if needed
options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

# --- GO TO FLIPKART ---
driver.get("https://www.flipkart.com")

# --- CLOSE LOGIN POPUP ---
try:
    close_button = driver.find_element(By.XPATH, "//button[contains(text(),'✕')]")
    close_button.click()
except:
    pass  # If popup doesn't appear

# --- SEARCH PRODUCT ---
search_box = driver.find_element(By.NAME, "q")
search_term = "Tshirts"  # <-- Change this to any product you want
search_box.send_keys(search_term + Keys.RETURN)

time.sleep(3)

# --- SCRAPE DATA ---
product_names = driver.find_elements(By.CLASS_NAME, "jt22zr")
product_prices = driver.find_elements(By.CLASS_NAME, "wvIX4U")

# --- SAVE TO CSV ---
output_path = os.path.join(os.getcwd(), "flipkart_prices.csv")
with open(output_path, mode="w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price"])

    for name, price in zip(product_names, product_prices):
        writer.writerow([name.text, price.text])

print("Data scraped and saved to flipkart_prices.csv")

# --- CLOSE BROWSER ---
driver.quit()
