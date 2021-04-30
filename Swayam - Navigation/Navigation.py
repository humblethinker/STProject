from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\humbl\\Downloads\\chromedriver_win32\\chromedriver.exe')

driver.maximize_window()
driver.get("https://swayam.gov.in/")

links = set()
elems = driver.find_elements_by_xpath("//a[@href]")

open('Output1.txt', 'w').close()

text_file = open('Output1.txt', "a")

for elem in elems:
    link = str(elem.get_attribute("href"))
    if "https" in link:
        links.add(link)

no = 0

for link in links:
    no=no+1
    text_file.write("Link "+str(no)+": " +str(link)+"\n\n")

text_file.close()

driver.quit()

