import requests
from bs4 import BeautifulSoup
def scrape_ethiostudy_info(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; +https://yourdomain.com/)"
    }
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    info = {
        "company_name": None,
        "address": None,
        "contact_number": None,
        "website": None
    }
    # Extract company name—based on observed HTML structure
    name_tag = soup.select_one("h1")
    if name_tag:
        info["company_name"] = name_tag.get_text(strip=True)
    # Extract paragraphs or list items containing the details
    text = soup.get_text(separator="\n")
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    for i, line in enumerate(lines):
        if line.startswith("Address"):
            info["address"] = lines[i + 1] if i + 1 < len(lines) else None
        elif line.startswith("Contact number"):
            parts = line.split(":", 1)
            info["contact_number"] = parts[1].strip() if len(parts) > 1 else None
        elif "Website" in line:
            # next line is actual URL
            info["website"] = lines[i + 1] if i + 1 < len(lines) else None
    return info
if __name__ == "__main__":
    url = "https://www.ethyp.com/company/364669/EthioStudy_online_learning?utm_source=chatgpt.com"
    data = scrape_ethiostudy_info(url)
    for key, val in data.items():
        print(f"{key}: {val}")
