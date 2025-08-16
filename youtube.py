from youtube_comment_downloader import YoutubeCommentDownloader

video_id = 'dQw4w9WgXcQ'
downloader = YoutubeCommentDownloader()

comments = []
for c in downloader.get_comments(video_id):
    comments.append(c)
    if len(comments) >= 100:
        break

print(f"Total comments fetched: {len(comments)}")

# print first 5 comments
for comment in comments[:5]:
    print(f"{comment['author']} said: {comment['text']}")
