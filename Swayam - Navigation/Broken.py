import requests
from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\humbl\\Downloads\\chromedriver_win32\\chromedriver.exe')

driver.maximize_window()
driver.get("https://swayam.gov.in/")

elems = driver.find_elements_by_xpath("//a[@href]")

broken_links = set()

working_links = set()

open('Output2.txt', 'w').close()

text_file = open('Output2.txt', "a")

for elem in elems:
    link = str(elem.get_attribute("href"))
    if "https" in link:
        r = requests.head(link)
        if r.status_code == 404:
            broken_links.add(link)
        else:
            working_links.add(link)

driver.quit()

no = 0

text_file.write("Broken links :\n\n")

for link in broken_links:
    no=no+1
    text_file.write("\t\tLink "+str(no)+": " +str(link)+"\n\n")

n = 0

text_file.write("Working links :\n\n")

for link in working_links:
    no=no+1
    text_file.write("\t\tLink "+str(no)+": " +str(link)+"\n\n")

text_file.close()

