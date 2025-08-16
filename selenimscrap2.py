from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

def scrape_courses(url):
    options = Options()
    # Uncomment next line to see browser window for debugging
    # options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 60)

    try:
        driver.get(url)

        root_div = wait.until(EC.presence_of_element_located((By.ID, "root")))
        courses_section = wait.until(EC.presence_of_element_located((By.ID, "course-list")))

        course_cards = courses_section.find_elements(By.CSS_SELECTOR, "div.shadow-card")
        print(f"Found {len(course_cards)} courses:\n")

        for idx, card in enumerate(course_cards, start=1):
            try:
                title = card.find_element(By.CSS_SELECTOR, "div.line-clamp-1").text.strip()
            except NoSuchElementException:
                title = "N/A"

            try:
                code = card.find_element(By.CSS_SELECTOR, "div.text-eshe-text-main.text-base").text.strip()
            except NoSuchElementException:
                code = "N/A"

            try:
                go_to_course_link = card.find_element(By.XPATH, ".//a[contains(text(),'Go To Course')]").get_attribute("href")
            except NoSuchElementException:
                go_to_course_link = "N/A"

            print(f"Course {idx}:")
            print(f"  Title: {title}")
            print(f"  Code: {code}")
            print(f"  Link: {go_to_course_link}\n")

    except TimeoutException:
        print("Timeout while waiting for elements")
    except WebDriverException as wde:
        print(f"WebDriver error: {wde}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    url = "https://courses.ethernet.edu.et/portal/courses"
    scrape_courses(url)
