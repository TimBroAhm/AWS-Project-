import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://eopcw.com/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

course_divs = soup.select("div#popular-courses a")  # adjust selector based on actual site structure
courses = []

for div in course_divs:
    title = div.text.strip()
    link = div.get("href")
    courses.append({"title": title, "link": link})

pd.DataFrame(courses).to_csv("eopcw_courses.csv", index=False)
print("Courses saved to eopcw_courses.csv")
