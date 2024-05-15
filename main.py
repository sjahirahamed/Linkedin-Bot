from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

EMAIL=""
PASSWORD = ""
NUMBER = ""
DETAILS=""


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3918876387&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

# Locate and click the sign-in button
sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()

email_user=driver.find_element(By.ID,value="username")
email_user.send_keys(EMAIL)

password_user=driver.find_element(By.ID,value="password")
password_user.send_keys(PASSWORD)

button_sign=driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
button_sign.click()

number_no=driver.find_element(By.XPATH,value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3918876387-122307466-phoneNumber-nationalNumber"]')
number_no.send_keys(NUMBER)

button_next=driver.find_element(By.ID,value="ember334")
button_next.click()

cover_letter=driver.find_element(By.XPATH,value='//*[@id="multiline-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3918876387-122307498-text"]')
cover_letter.send_keys(DETAILS)
