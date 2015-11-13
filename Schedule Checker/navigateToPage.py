#selenium used to navigate through webpages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
#time used to pause code so we can wait for refresh
import time
#beautifulsoup used to grab contnent from webpage and then search for specific term
from bs4 import BeautifulSoup
#smtplib used for email purposes
import smtplib


#global variables to be changed by the user
baseurl = "https://cas.fsu.edu/cas/login?service=https%3A%2F%2Fmy.fsu.edu%2Fc%2Fportal%2Flogin"
username = "fsuid"
password = "fsupassword"
desiredTerm = "2016 Spring"
desiredSubject = "CIS"
desiredCourseNumber = "4930"
#fill desiredClassName with whatever key expression you want the page to search for 
desiredClassName = "PYTHON"
emailAddress = "me@gmail.com"
emailPassword = 'password'
fromAddr = 'me@gmail.com'
#example path to webdriver
pathToDriver = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
mydriver = webdriver.Firefox(executable_path=pathToDriver) 
mydriver.get(baseurl)

def login():
	xpaths = { 'usernameTxtBox' : "//*[@id='username']",
			   'passwordTxtBox' : "//*[@id='password']",
			   'submitButton' : "//*[@id='fm1']/table/tbody/tr[2]/td[3]/input"

			 }
	#Clear username textbox if already allowed "Rememebr Me"
	mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()

	#send user name
	mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)

	#Clear Password TextBox if already allowed "Remember Me" 
	mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()

	#Write Password in password TextBox
	mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)

	#Click Login button
	mydriver.find_element_by_xpath(xpaths['submitButton']).click()
	
def navigateToSearchScreen():
	#need to wait for page to load before searching for elements
	time.sleep(7)
	
	xpaths = { 'futureTab' : "//*[@id='fsuMyCoursesFutureTab']",
			   'searchButton' : "//*[@id='future1IconSearch']",
			   'termDropBox' : "CLASS_SRCH_WRK2_STRM$35$",
			   'subjectTextBox' : "//*[@id='SSR_CLSRCH_WRK_SUBJECT$2']",
			   'courseNumberTextBox' : "//*[@id='SSR_CLSRCH_WRK_CATALOG_NBR$3']",
			   'submitSearchButton' : "//*[@id='CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH']",
			 }

	#click future tab
	mydriver.find_element_by_xpath(xpaths['futureTab']).click()
	
	#click search icon that takes us to new search page
	mydriver.find_element_by_xpath(xpaths['searchButton']).click()
	
	#need to wait for page to load
	time.sleep(7)
	
	#need to change iframe to where our elements are
	mydriver.switch_to_frame("ptifrmtgtframe")
	time.sleep(1)
	
	#this will select semester based on user variable for year
	select = Select(mydriver.find_element_by_id(xpaths['termDropBox']))
	select.select_by_visible_text(desiredTerm)
	time.sleep(3)
	
	#set subject to desired
	mydriver.find_element_by_xpath(xpaths['subjectTextBox']).send_keys(desiredSubject)
	
	#set course to desired
	mydriver.find_element_by_xpath(xpaths['courseNumberTextBox']).send_keys(desiredCourseNumber)
	
	#click search and go to search results
	#need to click twice for chrome/firefox on windows10, not sure why, and untested on other platforms
	mydriver.find_element_by_xpath(xpaths['submitSearchButton']).click()
	mydriver.find_element_by_xpath(xpaths['submitSearchButton']).click()
	time.sleep(3)
	
	
def refreshSearch():
	xpaths = { 'modifySearch' : "//*[@id='CLASS_SRCH_WRK2_SSR_PB_MODIFY']",
			   'submitSearchButton' : "//*[@id='CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH']",
			 }
	
	#click modify button which will take us to search page with data already filled
	mydriver.find_element_by_xpath(xpaths['modifySearch']).click()
	mydriver.find_element_by_xpath(xpaths['modifySearch']).click()
	
	#wait 15 seconds before searching again to avoid killing the server
	time.sleep(15)
	
	#switch iframe so we can find button
	#mydriver.switch_to_frame("ptifrmtgtframe")
	time.sleep(1)
	
	#click search button to take us back to search result page
	mydriver.find_element_by_xpath(xpaths['submitSearchButton']).click()
	mydriver.find_element_by_xpath(xpaths['submitSearchButton']).click()
	time.sleep(5)
		
def downloadSource():
	foundFlag = False
	
	#this will store the contents of the html page into variable named 'source'
	content = mydriver.page_source
	source = BeautifulSoup(content, "lxml")
	
	#we then only look for our desired class using methods from beautifulsoup
	lookingFor = source.body.findAll(text=desiredClassName)
	
	#and then we will check if our desired class is available 
	if desiredClassName in lookingFor:
		foundFlag = True
	else:
		refreshSearch()
	return foundFlag
def downloadSourceLoop():
	#keep re-searching until a match occurs
	while(downloadSource() == False):
		downloadSource()
	#email user once we find a match
	emailUser()

def emailUser():
	#standard template for emailing user in python
	#we send an email from yourself to yourself
	msg = "\r\n".join([
		"From: " + fromAddr,
		"To: " + emailAddress,
		"Subject: Class "+ desiredClassName + " Available",
		"",
		"Class " + desiredClassName + " Found!"	
	])
	#only works with gmail with current params, if change needed, change the smtp server to desired client
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login(emailAddress, emailPassword)
	server.sendmail(fromAddr, emailAddress, msg)
	server.quit()
	
def main():
	login()
	navigateToSearchScreen()
	downloadSourceLoop()
	#close browser when finished
	mydriver.quit()
	
main()
