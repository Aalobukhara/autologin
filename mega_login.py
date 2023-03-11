from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Replace with the path to your geckodriver
driver = webdriver.Firefox(executable_path='/path/to/geckodriver')

# Define your dictionary of login ids and passwords
login_dict = {'email1@example.com': 'password1', 'email2@example.com': 'password2'}

# Iterate over the key-value pairs in the dictionary
for email, password in login_dict.items():
    # Navigate to the login page
    driver.get('https://mega.nz/login')

    # Find the email and password fields
    email_field = driver.find_element_by_id('login-name2')
    password_field = driver.find_element_by_id('login-password2')

    # Enter the email and password from the current iteration of the loop
    email_field.send_keys(email)
    password_field.send_keys(password)

    # Click the login button
    login_button = driver.find_element_by_class_name('big-red-button')
    login_button.click()

    # Wait for 2 seconds
    time.sleep(2)

    # Click on the avatar icon to open the user menu
    avatar_icon = driver.find_element_by_class_name('avatar-wrapper')
    avatar_icon.click()

    # Click on the logout button in the user menu
    logout_button = driver.find_element_by_class_name('top-menu-logout')
    logout_button.click()

# Close the browser window
driver.quit()