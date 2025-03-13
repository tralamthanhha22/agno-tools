from agno.agent import Agent
from agno.tools.youtube import YouTubeTools
from agno.models.ollama import Ollama
import os

# Đặt API key đúng cách
os.environ["YOUTUBE_API_KEY"] = "api_key"
youtube_token = os.getenv("api_key")

# Khởi tạo YouTubeTools
yt_tool = YouTubeTools()

# Khởi tạo Agent
agent = Agent(
    model=Ollama("mistral"),
    tools=[yt_tool],  # Không cần truyền access_token
    show_tool_calls=True,
    markdown=True,
)

# Gửi yêu cầu tìm kiếm video
agent.print_response("Search for recent videos about artificial intelligence, i just need you search videos for me and send full videos'link i dont want you show me instruction.")

# from googleapiclient.discovery import build

# from youtube_transcript_api import YouTubeTranscriptApi

# # Nhập API key của bạn vào đây
# API_KEY = "api_key"

# def get_video_transcript(video_id, language="en"):
#     try:
#         # Get transcript (subtitles) in the specified language
#         transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
        
#         # Convert transcript list into a single text string
#         text = "\n".join([entry["text"] for entry in transcript])
        
#         return text
#     except Exception as e:
#         return f"Error: {e}"
# transcript_text = get_video_transcript("SWDhGSZNF9M")
# print(transcript_text)

# Khởi tạo dịch vụ YouTube API
# youtube = build("youtube", "v3", developerKey=API_KEY)

# Gọi API tìm kiếm video liên quan đến chủ đề "AI technology"
# response = youtube.search().list(
#     q="AI technology",   # Từ khóa tìm kiếm
#     part="snippet",
#     maxResults=5         # Giới hạn số kết quả trả về
# ).execute()

# In danh sách tiêu đề video
# for item in response["items"]:
    # print(f"Title: {item['snippet']['title']}")
    # print(f"Video ID: {item['id'].get('videoId', 'N/A')}")
    # print(f"Link video:https://www.youtube.com/watch?v={item['id'].get('videoId', 'N/A')}")
    # print("---")