from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_root_content(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        wait = WebDriverWait(driver, 15)

        # Wait for root div
        root_div = wait.until(EC.presence_of_element_located((By.ID, "root")))

        # Get innerHTML (safe since it’s attribute access)
        root_html = root_div.get_attribute("innerHTML")
        print("HTML inside root div (first 1000 chars):\n", root_html[:1000])

        # Extract main heading safely: find again right before accessing text
        try:
            heading = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#root h1"))).text
            print("\nMain Heading:", heading)
        except:
            print("\nMain Heading: Not found")

        # Extract all buttons: locate and get texts immediately
        buttons = driver.find_elements(By.CSS_SELECTOR, "#root button")
        print("\nButtons:")
        for btn in buttons:
            try:
                text = btn.text.strip()
                if text:
                    print("-", text)
            except:
                continue  # element became stale, skip

        # Extract all links inside root: locate fresh and print href + text
        links = driver.find_elements(By.CSS_SELECTOR, "#root a")
        print("\nLinks inside root div:")
        for a in links:
            try:
                href = a.get_attribute("href")
                text = a.text.strip()
                if text or href:
                    print(f"Text: {text}, URL: {href}")
            except:
                continue  # stale element, skipxcept Exception as e:
        print("Error:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    url = "https://courses.ethernet.edu.et/portal/courses"
    scrape_root_content(url)
