from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Setup Selenium
driver = webdriver.Firefox()  # or webdriver.Chrome()
driver.get("https://courses.ethernet.edu.et/portal/courses")

time.sleep(5)  # wait for page to load

soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

# Extract course titles
courses = soup.find_all("div", class_="course-box")  # Inspect exact class
for course in courses:
    title = course.find("h4").text.strip()
    print("Course:", title)
