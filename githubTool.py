from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.github import GithubTools
import os

# Manually set the GitHub token
os.environ["GITHUB_TOKEN"] = "ghp_"

# Check if the token is set
print(os.getenv("GITHUB_TOKEN"))  # Should print your token (or part of it for security)
github_token = os.getenv("GITHUB_TOKEN")

agent = Agent(model=Ollama("mistral"),
    instructions=[
        "Use your tools to answer questions about the repo: agno-agi/agno",
        "Do not create any issues or pull requests unless explicitly asked to do so",
    ],
    tools=[GithubTools(access_token=github_token)],
)
agent.print_response("List open pull requests", markdown=True)


# import os
# import requests

# def get_pull_request():
#     return

# def get_issues(token_key,owner,repo_name):
#     GITHUB_TOKEN = token_key
#     REPO_OWNER = owner
#     REPO_NAME = repo_name
#     URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"

#     headers = {
#         "Authorization": f"token {GITHUB_TOKEN}",
#         "Accept": "application/vnd.github.v3+json"
#     }

#     response = requests.get(URL, headers=headers)
#     issuesList=[]
#     if response.status_code == 200:
#         issues = response.json()
#         for issue in issues:
#             issuesList.append(f"Issue #{issue['number']}: {issue['title']}")
#         return issuesList
#     else:
#         return "Failed to retrieve issues:", response.status_code, response.text


# # GitHub search function
# def search_github(token, query, num_results=5):
#     headers = {}
#     if token:
#         headers["Authorization"] = f"token {token}"

#     url = f"https://api.github.com/search/repositories?q={query}&sort=stars&per_page={num_results}"
#     response = requests.get(url, headers=headers)

#     if response.status_code == 200:
#         results = response.json().get("items", [])
#         return [f"{repo['full_name']}: {repo['html_url']}" for repo in results]
#     else:
#         return ["Error fetching results."]

# # Example usage
# query = "face detection"
# token_key = os.getenv("ghp_")
# search_results = search_github(token_key,query)
# for i in search_results:
#     print(i+"\n")
# issues=get_issues("ghp_","hedge-dev","XenonRecomp")
# print(issues)