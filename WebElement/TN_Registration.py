from selenium import webdriver
from selenium.webdriver.common.by import By

from faker import Faker
fake = Faker()

driver = webdriver.Firefox()

driver.get("https://tutorialsninja.com/demo/")

my_account = driver.find_element(By.CSS_SELECTOR, ".list-inline .dropdown .hidden-md")
my_account.click()

register = driver.find_element(By.LINK_TEXT, "Register")
register.click()

first_name = driver.find_element(By.CSS_SELECTOR, "#input-firstname")
first_name.send_keys(fake.first_name())

last_name = driver.find_element(By.CSS_SELECTOR, "#input-lastname")
last_name.send_keys(fake.last_name())

email = driver.find_element(By.CSS_SELECTOR, "#input-email")
email.send_keys(fake.email())

telephone = driver.find_element(By.CSS_SELECTOR, "#input-telephone")
telephone.send_keys("9876543210")

password = driver.find_element(By.CSS_SELECTOR, "#input-password")
password.send_keys("abc@123")

password_confirm = driver.find_element(By.CSS_SELECTOR, "#input-confirm")
password_confirm.send_keys("abc@123")

privacy_policy = driver.find_element(By.CSS_SELECTOR, "[type='checkbox']")
privacy_policy.click()

continue_btn = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
continue_btn.click()

# Validate Account Registration success or not
expected_success = "Your Account Has Been Created!"
actual_success = driver.find_element(By.CSS_SELECTOR, "#content h1").text
assert expected_success == actual_success, f"Unsuccessful Registration!!"

print("Test Registration is passed")

driver.quit()

