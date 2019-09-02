from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
from pathlib import Path
import sys


# Input your SemRush Login here
semrush_mail ="XXXXXXXX"
semrush_password ="XXXXXXX"


# Input Websites (Max 5)
while True:
    website = input("Enter your website:").casefold()
    if not re.match(".*?\.[a-z]{2,}|none",website):
        print("No Website Detected ! Insert valid domain or URL")
    else:
        break

while True:
    website1 = input("Enter second website, (if no website type : \"None\") : ").casefold()
    if not re.match(".*?\.[a-z]{2,}|none",website1):
        print("No Website Detected ! Insert valid domain or URL")
    else:
        break

if website1 != "none":
    while True:
        website2 = input("Enter third website, (if no website type : \"None\") : ").casefold()
        if not re.match(".*?\.[a-z]{2,}|none", website2):
            print("No Website Detected ! Insert valid domain or URL")
        else:
            break
if website1 != "none" and website2 != "none":
    while True:
        website3 = input("Enter fourth website, (if no website type : \"None\") : ").casefold()
        if not re.match(".*?\.[a-z]{2,}|none", website3):
            print("No Website Detected ! Insert valid domain or URL")
        else:
            break
if website1 != "none" and website2 != "none" and website3 != "none":
    while True:
        website4 = input("Enter last website, (if no website type : \"None\") : ").casefold()
        if not re.match(".*?\.[a-z]{2,}|none", website4):
            print("No Website Detected ! Insert valid domain or URL")
        else:
            break

# Database input + Keep asking until input is in list
db_list = [
    "us", "uk", "br", "ca", "au", "fr", "de", "it", "nl", "es", "in", "ru",
    "jp", "tr", "dk", "mx", "ar", "pl", "be", "ie", "se", "ch", "fi", "hu",
    "no", "il", "sg", "hk"
]
db_input = None
while db_input not in db_list:
    if db_input is not None:
        print("Wrong Data base input, must be one of the one above")

    db_input = input("Enter yout Data Base ( " +str(db_list) + ") :")

print("Ok let's go !")

# URLs creation
url_website = "https://semrush.com/analytics/organic/positions/?db=" + db_input + "&searchType=domain&q=" + website

if website1 != "none":
    url_website1 = "https://semrush.com/analytics/organic/positions/?db=" + db_input + "&searchType=domain&q=" + website1
if website1 != "none" and website2 !="none":
    url_website2 = "https://semrush.com/analytics/organic/positions/?db=" + db_input + "&searchType=domain&q=" + website2
if website1 != "none" and website2 !="none" and website3 != "none":
    url_website3 = "https://semrush.com/analytics/organic/positions/?db=" + db_input + "&searchType=domain&q=" + website3
if website1 != "none" and website2 !="none" and website3 != "none" and website4 != "none":
    url_website4 = "https://semrush.com/analytics/organic/positions/?db=" + db_input + "&searchType=domain&q=" + website4

# Setting up Chrome headless download
def enable_download_in_headless_chrome(browser, download_dir):
    #add missing support for chrome "send_command"  to selenium webdriver
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    #Set up download folder
    excel_folder = Path.cwd() / "excel"
    myexcel_folder = str(excel_folder)
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': myexcel_folder}}
    browser.execute("send_command", params)



# Setting up Chrome options
chrome_folder = Path.cwd() / "driver" / "chromedriver"
mychrome_folder = str(chrome_folder)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--lang=en")
chrome_options.add_argument("--disable-features=NetworkService")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument('headless')
browser = webdriver.Chrome(mychrome_folder, options=chrome_options)

# Setting up Chrome headless download
enable_download_in_headless_chrome(browser, "c:\temp")

# Opening a new URL
source = browser.get(url_website)

# Clicking on login text
login_icon = WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,"//div[contains(text(),'Log in')]")))
login_icon.click()

# Putting the logins
login_bar = browser.find_element_by_name("email")
login_bar.send_keys(semrush_mail)
mdp_bar = browser.find_element_by_name("password")
mdp_bar.send_keys(semrush_password)

# Click on logging button
login_button = WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.CLASS_NAME,"sc-btn__inner")))
login_button.click()

try:
    confirm_log = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'srf-line')))
    print("Login Successful")
except:
    error_log = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'sc-notice__body')))
    print("Wrong Login or Password, try changing it")
    time.sleep(2)
    browser.quit()
    sys.exit()

# Website

#No results
if website != "none":
    source = browser.get(url_website)
    try:
        noresults = WebDriverWait(browser,3).until(EC.visibility_of_element_located((By.CLASS_NAME,"cl-nothing-found-page__title")))
        print(website + " status : " + noresults.text)
    except:
#Click on export
        export_icon = WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Export')]")))
        export_icon.click()
#Click on excel
        export_excel = WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Excel')]")))
        export_excel.click()
        time.sleep(3)
        print(website + " status : report downloaded")

# Website 1
if website1 != "none":
    source = browser.get(url_website1)
    try:
# No results
        noresults2 = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, "cl-nothing-found-page__title")))
        print(website1 + " status : " + noresults2.text)

    except:
#Click on export
        export_icon = WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Export')]")))
        export_icon.click()
#Click on excel
        export_excel = WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Excel')]")))
        export_excel.click()
        time.sleep(3)
        print(website1 + " status : report downloaded")

# Website 2
if website1 != "none" and website2 !="none" :
    source = browser.get(url_website2)

    try:
        # No results
        noresults3 = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, "cl-nothing-found-page__title")))
        print(website2 + " status : " + noresults3.text)

    except:
#Click on export
        export_icon = WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Export')]")))
        export_icon.click()
#Click on excel
        export_excel = WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Excel')]")))
        export_excel.click()
        time.sleep(3)
        print(website2 + " status : report downloaded")

# Website 3
if website1 != "none" and website2 !="none" and website3 != "none" :
    source = browser.get(url_website3)

    try:
        # No results
        noresults4 = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, "cl-nothing-found-page__title")))
        print(website3 + " status : " + noresults4.text)

    except:
#Click on export
        export_icon = WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Export')]")))
        export_icon.click()
#Click on excel
        export_excel = WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Excel')]")))
        export_excel.click()
        time.sleep(3)
        print(website3 + " status : report downloaded")

# Website 4
if website1 != "none" and website2 !="none" and website3 != "none" and website4 != "none":
    source = browser.get(url_website4)

    try:
        # No results
        noresults5 = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, "cl-nothing-found-page__title")))
        print(website4 + " status : " + noresults5.text)

    except:
#Click on export
        export_icon = WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Export')]")))
        export_icon.click()
#Click on excel
        export_excel = WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Excel')]")))
        export_excel.click()
        time.sleep(3)
        print(website4 + " status : report downloaded")

# Closing Browser
time.sleep(5)
browser.quit()
print("Done ! ")
