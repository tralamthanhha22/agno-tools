import agno
from agno.tools.googlesearch import GoogleSearchTools
from agno.models.ollama import Ollama
from agno.agent import Agent, RunResponse  # noqa
import os

# Đặt API key đúng cách
os.environ["GOOGLE_API_KEY"] = "api-key"
gg_api_key = os.getenv("api-key")

os.environ["GOOGLE_CSE_ID"]="cseid"
gg_cse=os.getenv("cseid")

# Khởi tạo DuckDuckGo tool
tool = GoogleSearchTools()

# Tạo Agent với DuckDuckGo tool
agent = Agent(model=Ollama("mistral"), tools=[tool],show_tool_calls=True,markdown=True)

# Sử dụng agent để tìm kiếm thông tin qua DuckDuckGo
response = agent.run("Tìm kiếm thông tin về Trấn Thành. Tôi không cần code hướng dẫn, tôi cần bạn tìm kiếm thông tin cho tôi.")
print(response.content)








# import requests

# def google_search(query, api_key, cse_id, num_results=10):
#     url = "https://www.googleapis.com/customsearch/v1"
#     params = {
#         "q": query,         # Search query
#         "key": api_key,     # API key
#         "cx": cse_id,       # Custom Search Engine ID
#         "num": num_results  # Number of results
#     }
    
#     response = requests.get(url, params=params)
#     results = response.json()
    
#     return results.get("items", [])

# # Replace with your API Key and Search Engine ID
# API_KEY = "api-key"
# CSE_ID = "cseid"

# # Search for something
# search_results = google_search("latest AI news", API_KEY, CSE_ID)
# # Print results
# for idx, result in enumerate(search_results):
#     print(f"Result {idx+1}:")
#     for key, value in result.items():
#         print("\n"+f"{key}: {value}"+"\n")
#     print("-" * 50)