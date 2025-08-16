from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()  # or Firefox
driver.get("https://learning.gov.et/all-courses/")
time.sleep(5)

soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

# Find courses
courses = soup.find_all("div", class_="ld-course-list-items")  # Adjust if needed

for course in courses:
    title_tag = course.find("h3")
    if title_tag:
        print("Course:", title_tag.text.strip())
