from selenium.webdriver import Chrome, ChromeOptions, DesiredCapabilities
import Data

caps = DesiredCapabilities.CHROME.copy()
caps['acceptInsecureCerts'] = True

browser = Chrome('C:\\Users\\humbl\\Downloads\\chromedriver_win32\\chromedriver.exe', desired_capabilities=caps)
browser.get('https://swayamopenid.b2clogin.com/swayamopenid.onmicrosoft.com/B2C_1_swayam2/oauth2/v2.0/authorize?response_type=code&client_id=019220f4-2ec0-41c2-a727-529f1b54bb06&redirect_uri=https%3A%2F%2Fswayam.gov.in%2Fwso_ok&scope=https%3A%2F%2Fswayamopenid.onmicrosoft.com%2Fapi%2Fuser_impersonation+offline_access+openid&state=ITXOhHbxCBs08xNEmJTh8rhmLKE8pG&access_type=authorization_code')

open('Output.txt', 'w').close()

tc=1

text_file = open("Output.txt", "a")

for i in Data.login_ids:
    for j in Data.passwords:

        text_file.write("Test case " + str(tc) + " : ")
        tc=tc+1
        browser.implicitly_wait(10)
        email = browser.find_element_by_id("logonIdentifier")
        email.clear()
        email.send_keys(i)

        password = browser.find_element_by_id('password')
        password.clear()
        password.send_keys(j)

        signupbutton = browser.find_element_by_xpath("//button[@id='next']")
        signupbutton.click()

        validation_mes_email = browser.find_element_by_xpath("//div[@id='api']/div[3]/div[3]/div/div/p")
        validation_mes_pass = browser.find_element_by_xpath("//div[@id='api']/div[3]/div[3]/div[2]/div[2]/p")

        if validation_mes_email.text!="":
            text_file.write(validation_mes_email.text + "\n")
        else:
            text_file.write("No validation message\n")

        if validation_mes_pass.text!="":
            text_file.write(validation_mes_pass.text + "\n")
        else:
            text_file.write("No validation message\n")

        error_message = browser.find_element_by_xpath("//div[@id='api']/div[3]/div[2]/p")
        if error_message.text!="":
            text_file.write(error_message.text+"\n\n")
        elif validation_mes_email.text=="" and validation_mes_pass.text=="":
            if browser.current_url=="https://swayam.gov.in/":
                browser.get("https://swayam.gov.in/wso_logout")
                browser.get('https://swayamopenid.b2clogin.com/swayamopenid.onmicrosoft.com/B2C_1_swayam2/oauth2/v2.0/authorize?response_type=code&client_id=019220f4-2ec0-41c2-a727-529f1b54bb06&redirect_uri=https%3A%2F%2Fswayam.gov.in%2Fwso_ok&scope=https%3A%2F%2Fswayamopenid.onmicrosoft.com%2Fapi%2Fuser_impersonation+offline_access+openid&state=ITXOhHbxCBs08xNEmJTh8rhmLKE8pG&access_type=authorization_code')
                text_file.write("Success\n\n")
            else:
                text_file.write("No response from login button\n\n")
        else:
            text_file.write("\n")

        browser.refresh()

text_file.close()

browser.close()