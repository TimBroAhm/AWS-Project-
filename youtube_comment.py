import csv
from googleapiclient.discovery import build

# ✅ Replace with your own API Key
API_KEY = 'AIzaSyA2XQ3uEepUcs4iQEmXxtBVPGcB2kBlUJM'

# ✅ Replace with a video ID that allows comments
# This is a working example with active comments (change later to Ethiopian video)
VIDEO_ID = 'dQw4w9WgXcQ'  # Example: Rick Astley

# Initialize YouTube API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_comments(video_id):
    comments = []
    next_page_token = None

    while True:
        try:
            request = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                maxResults=100,
                pageToken=next_page_token,
                textFormat="plainText"
            )
            response = request.execute()

            for item in response.get('items', []):
                comment = item['snippet']['topLevelComment']['snippet']
                comments.append({
                    'author': comment['authorDisplayName'],
                    'text': comment['textDisplay'],
                    'like_count': comment['likeCount'],
                    'published_at': comment['publishedAt']
                })

            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break

        except Exception as e:
            print(f"❌ Error: {e}")
            break

    return comments

def save_to_csv(comments, filename):
    keys = ['author', 'text', 'like_count', 'published_at']
    with open(filename, 'w', encoding='utf-8', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(comments)

# Run the script
if __name__ == "__main__":
    print("📥 Fetching comments from video...")
    data = get_comments(VIDEO_ID)
    print(f"✅ Total comments fetched: {len(data)}")

    csv_filename = "ethio_comments.csv"
    save_to_csv(data, csv_filename)
    print(f"📁 Saved to {csv_filename}")
