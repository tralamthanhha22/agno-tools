import agno
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.ollama import Ollama
from agno.agent import Agent, RunResponse  # noqa

# Khởi tạo DuckDuckGo tool
tool = DuckDuckGoTools()

# Tạo Agent với DuckDuckGo tool
agent = Agent(model=Ollama("mistral"), tools=[tool])

# Sử dụng agent để tìm kiếm thông tin qua DuckDuckGo
response = agent.run("Tìm kiếm thông tin về Apache Airflow.")
print(response.content)


# import ollama
# from duckduckgo_search import DDGS

# def query_duckduckgo(question):
#     # Perform a DuckDuckGo search
#     with DDGS() as ddgs:
#         results = [r["title"] + " - " + r["href"] for r in ddgs.text(question, max_results=5)]
#     return results

# def ask_ollama(prompt):
#     response = ollama.chat(model='mistral', messages=[{"role": "user", "content": prompt}])
#     return response['message']['content']

# if __name__ == "__main__":
#     user_query = input("Ask something: ")
#     search_results = query_duckduckgo(user_query)
    
#     context = "\n".join(search_results)
#     # ollama_prompt = f"Here are the search results:\n{context}\n\nSummarize these results and answer the query: {user_query}"
    
#     # answer = ask_ollama(ollama_prompt)
#     # print("\nAnswer:", answer)
#     print(context)