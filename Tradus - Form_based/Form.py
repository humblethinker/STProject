from selenium.webdriver import Chrome, ChromeOptions, DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


caps = DesiredCapabilities.CHROME.copy()
caps['acceptInsecureCerts'] = True

browser = Chrome('C:\\Users\\humbl\\Downloads\\chromedriver_win32\\chromedriver.exe', desired_capabilities=caps)
browser.get('https://www.tradus.com/account/login#tab-login')

#time.sleep(2)

login_ids = [
    "",
    "a@b",
    "aab",
    " ewfrtrtjje@sammdmk.ac.in",
    "ewfrtrtjje@ sammdmk.ac.in",
    "ewfrtrtjje@sammdmk.ac.in ",
    "ewfrtrtjje@sammdmk.ac.in"
]

passwords = [
    "",
    "qwert",
    "qwerty",
    "Abcdefgh"
]

open('Output.txt', 'w').close()

tc=1

text_file = open("Output.txt", "a")

for i in login_ids:
    for j in passwords:
        # Fill user's email ID
        text_file.write("Test case " + str(tc) + " : ")
        tc=tc+1
        email = browser.find_element_by_id('username_login')
        email.clear()
        email.send_keys(i)

        #time.sleep(2)
        # Fill user's password
        password = browser.find_element_by_id('password_login')
        password.clear()
        password.send_keys(j)

        #time.sleep(1)

        # click on signup page
        signupbutton = browser.find_element_by_xpath("//button[@type='submit']")
        signupbutton.click()

        validation_msg=False

        try:
            validation_msg = email.get_attribute("validationMessage")
            text_file.write("Email: "+validation_msg+"\n")
        except:
            text_file.write("Email: No validation message\n")

        try:
            validation_msg = password.get_attribute("validationMessage")
            text_file.write("Password: "+validation_msg+"\n")
        except:
            text_file.write("Password: No validation message\n")

        error_message = browser.find_element_by_xpath("//article/div/div")

        if error_message.text == "Offer of the day" :
            text_file.write("Success \n\n")
            browser.get('https://www.tradus.com/account/logout')
        elif error_message.text == "" :
            text_file.write("No error message \n\n")
        else:
            text_file.write(error_message.text+"\n\n")
        browser.get('https://www.tradus.com/account/login#tab-login')
        #browser.implicitly_wait(10)


text_file.close()

browser.close()