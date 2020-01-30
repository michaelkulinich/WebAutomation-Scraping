# https://intellipaat.com/community/16524/take-screenshot-of-full-page-with-selenium-python-with-chromedriver  set up classes
from selenium import webdriver
import time

# Selenium to automate through web
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
inputFirstName = input("Enter First Name ")
inputLastName = input("Enter last Name ")
lastNameList = [ "lastName", "LastName", "lastname", "lname"]
firstNameList = ["firstName", "FirstName", "firstname", "fname"]



driver = webdriver.Chrome()
driver.set_page_load_timeout(15)
driver.maximize_window()
driver.get("http://www.superiorcourt.maricopa.gov/docket/CriminalCourtCases/caseSearch.asp")

try:
    driver.find_element_by_name("lastName").send_keys(inputLastName)
except NoSuchElementException:
    pass



try:
    driver.find_element_by_name("FirstName").send_keys(inputFirstName)
    driver.find_element_by_name("FirstName").send_keys(Keys.ENTER)
except NoSuchElementException:
    pass


# looks for the first case number
# driver.find_element_by_link_text('CR2018-000971').click()

# find all the links on the page that corrispond to a caseNumber, add them to list
caseList = driver.find_elements_by_xpath("//a[contains(@href,'caseNumber')]")


# This while loop handles if there are multiple pages of
# case numbers. It will click the next link
# and add those cases to the caseList
while True:
    try:
        driver.find_element_by_link_text('next >').click()
        caseList.extend(driver.find_elements_by_xpath("//a[contains(@href,'caseNumber')]"))
    except NoSuchElementException:
        break
caseNum = 1
# Prints the case number, the text link
# for i in caseList:
#     print(str(i.get_attribute('text')).strip())

for i in caseList:
    # open new window so the first window stays
    # because we need it to access the other cases
    secondDriver = webdriver.Chrome()
    secondDriver.set_page_load_timeout(15)
    secondDriver.maximize_window()
    secondDriver.get(i.get_attribute("href"))
    url = driver.current_url
    numShot = 1
    fileName = str(i.get_attribute('text')).strip() + "_Pic" + str(numShot) + ".jpg"
    SCROLL_PAUSE_TIME = .05


    # Get scroll height
    # driver.execute_script("window.scrollTo(0, height)")
    secondDriver.get_screenshot_as_file("screenshots/" + fileName)
    height = 500
    scroll_height = secondDriver.execute_script('return document.body.parentNode.scrollHeight')
    while height < scroll_height:
        secondDriver.execute_script("window.scrollBy(0,500)")
        height += 500
        # time.sleep(SCROLL_PAUSE_TIME)
        numShot += 1
        fileName = str(i.get_attribute('text')).strip() + "_Pic" + str(numShot) + ".jpg"
        # secondDriver.get_screenshot_as_file(fileName)
        secondDriver.save_screenshot("screenshots/" + fileName)

    height = 500
    numShot = 1
    secondDriver.quit()
driver.quit()
#
#
#
# print("yes")
# # while True:
# #     # Scroll down to bottom
# #
# #     # driver.execute_script("window.scrollBy(0,1000)")
# #
# #     # Wait to load page
# #
# #
# #     # Calculate new scroll height and compare with last scroll height
# #     new_height = driver.execute_script("window.scrollBy(0,1000)")
# #     time.sleep(SCROLL_PAUSE_TIME)
# #     numShot += 1
# #     fileName = "test" + str(numShot) + ".jpg"
# #     driver.get_screenshot_as_file(fileName)
# #     if new_height == last_height:
# #         break
# #     last_height = new_height
#
#
#

# Scrape the court case with beautiful soup
# import bs4 as bs
# import urllib.request
# source = urllib.request.urlopen(url)
# soup = bs.BeautifulSoup(source, 'lxml')
# table = soup.find(id = 'tblDocket2')
# table_rows = table.find_all('tr')
# info = []
# for tr in table_rows:
#     td = tr.find_all('td')
#     row = [i.text.strip() for i in td]
#     info.append(row)
# print(info)
# for i in range(len(info)):
#     for j in range(len(info[i])):
#         print(info[i][j], end = ' ')
#
#     print()
#
# print()
# fullname = info[3][0].strip(' -(2)').split()
# first = fullname[0]
# middle = fullname[1]
# last = fullname[2]
# sex = info[3][2]
# caseNumber = info[3][5]
# print("First Name: ", first)
# print("Middle Name: ", middle)
# print("Last Name: ",last)
# print("Sex: ", sex)
# print("Case number: ", caseNumber)
#
# print()
# tables = soup.find_all('table')
# for t in tables:
#     if id == 'tblDocket2':
#         print("Found")





# driver.maximize_window()
# driver.refresh()
# driver.implicitly_wait(3)
# driver.quit()
