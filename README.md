# Personalized Course Recommendation System for Ethiopian E-Learning Platforms

A course recommendation project that uses **collaborative filtering** and **user interaction data** (ratings and comments) to suggest relevant online courses to learners on Ethiopian e-learning platforms.

The repository covers the full pipeline: collecting course data, collecting learner feedback, and building and testing the recommender in a Jupyter notebook.

---

## Why this project?

Learners on e-learning platforms are often faced with a long list of courses and little guidance on where to start. This project explores how ratings and feedback from other learners can be used to point each learner toward courses they are more likely to find useful, with a focus on the Ethiopian context.

## How it works

```
   Data collection                    Data files                 Modeling
┌───────────────────────┐        ┌────────────────────┐     ┌──────────────────────────┐
│ Scrape course catalogs │  ───►  │ all_courses.csv    │     │                          │
│ (Selenium, BeautifulSoup)│      │ eopcw_courses.csv  │ ──► │ course_recommendation    │
│                       │        │ courses.csv.xls    │     │ .ipynb                   │
│ Collect YouTube        │  ───►  │ ethio_comments.csv │     │ (collaborative filtering)│
│ comments (YouTube API) │        │ rating_df.csv      │     │                          │
└───────────────────────┘        │ final.csv          │     └──────────────────────────┘
                                 └────────────────────┘
```

1. **Collect** course listings from e-learning portals and comments from YouTube videos.
2. **Prepare** the results as CSV files (course catalog, ratings, comments, and a final merged dataset).
3. **Recommend** courses in `course_recommendation.ipynb` using collaborative filtering on the rating data.

## Repository contents

### Notebooks

| File | Purpose |
| --- | --- |
| `course_recommendation.ipynb` | Main notebook: loads the data and builds and evaluates the collaborative-filtering recommender. **Start here.** |
| `Webscrap.ipynb` | Notebook version of the web scraping work. |

### Data collection scripts

| File | Purpose |
| --- | --- |
| `lms.py` | Uses Selenium and BeautifulSoup to open the course portal at `courses.ethernet.edu.et` and print the course titles. |
| `youtube_comment.py` | Uses the YouTube Data API v3 to download all top-level comments for a video and save them to `ethio_comments.csv`. |
| `webscrapp.py`, `seleniumscrap.py`, `selenimscrap2.py`, `ethyp.py`, `wu.py`, `youtube.py`, `del.py` | Additional scraping and helper scripts used while building the datasets. |

### Data files

| File | Description |
| --- | --- |
| `all_courses.csv` | Combined course catalog. |
| `eopcw_courses.csv` | Courses collected from an additional source (EOPCW). |
| `courses.csv.xls` | Course data in spreadsheet form. |
| `ethio_comments.csv` | Comments collected from YouTube (author, text, like count, publish date). |
| `rating_df.csv` | Rating data used by the recommender (about 4 MB). |
| `final.csv` | Final merged dataset. |

## Getting started

### Prerequisites

- Python 3.9 or newer
- [Jupyter Notebook or JupyterLab](https://jupyter.org/install)
- Firefox or Chrome plus the matching WebDriver (only needed to run the Selenium scrapers)
- A YouTube Data API key (only needed to run `youtube_comment.py`)

### Installation

```bash
git clone https://github.com/TimBroAhm/AWS-Project-.git
cd AWS-Project-

python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

pip install pandas numpy scikit-learn jupyter
pip install selenium beautifulsoup4 google-api-python-client
```

> The notebook's first cells list the exact libraries it imports. Install any that are missing.

### Run the recommender

The data files are already included, so you can try the recommender without scraping anything:

```bash
jupyter notebook course_recommendation.ipynb
```

Then run the cells from top to bottom.

### Re-collect the data (optional)

**Course catalog**

```bash
python lms.py
```

**YouTube comments**

1. Create an API key in the [Google Cloud Console](https://console.cloud.google.com/) and enable the YouTube Data API v3.
2. Set the key as an environment variable instead of writing it into the file:

   ```bash
   export YOUTUBE_API_KEY="your-key-here"
   ```

3. In `youtube_comment.py`, read the key with `os.environ["YOUTUBE_API_KEY"]` and set `VIDEO_ID` to the video you want.
4. Run:

   ```bash
   python youtube_comment.py
   ```

## Responsible data use

- Check each website's terms of service and `robots.txt` before scraping it.
- The comment data contains public usernames. Do not use it to identify or contact individuals.
- Never commit API keys or passwords to the repository.

## Roadmap

Ideas for taking the project further:

- Content-based filtering using course descriptions, to help new courses that have no ratings yet
- A hybrid model that combines collaborative and content-based methods
- Support for Amharic and other local-language course content
- A simple web app so learners can get recommendations without using a notebook
- Deployment on AWS

## Contributing

Contributions and suggestions are welcome. To contribute:

1. Fork the repository
2. Create a branch (`git checkout -b feature/your-idea`)
3. Commit your changes
4. Open a pull request

## Author

**TimBroAhm** - [GitHub profile](https://github.com/TimBroAhm)
