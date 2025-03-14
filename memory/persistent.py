from typing import List, Optional
from agno.models.ollama import Ollama
import typer
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.storage.agent.postgres import PostgresAgentStorage
from agno.vectordb.pgvector import PgVector, SearchType
# postgresql://postgres:[YOUR-PASSWORD]@db.twrcowjjcfgcyqhnioqb.supabase.co:5432/postgres
import os
import ollama
# VUI LONG VAO SCHEMA AI @@@
os.environ["OPENAI_API_KEY"] = ""  # Loại bỏ API key
from agno.vectordb.pgvector import PgVector

class OllamaEmbedder:
    def __init__(self, model="mistral"):
        self.model = model
        self.dimensions = 4096  # Cần kiểm tra số chiều chính xác cho model Ollama

    def get_embedding(self, text):
        return ollama.embeddings(model=self.model, prompt=text)["embedding"]

    def get_embedding_and_usage(self, text):
        embedding = self.get_embedding(text)
        return embedding, {"tokens_used": len(text)}  # Giả lập usage

db_url = "postgresql://postgres:%40TLTHa0512@db.twrcowjjcfgcyqhnioqb.supabase.co:5432/postgres"
vector_db=PgVector(
        embedder=OllamaEmbedder(),
        table_name="recipes", db_url=db_url, search_type=SearchType.hybrid
    )
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://www.antennahouse.com/hubfs/xsl-fo-sample/pdf/basic-link-1.pdf"],
    # urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=vector_db
)

storage = PostgresAgentStorage(table_name="pdf_agent", db_url=db_url)


def pdf_agent(new: bool = False, user: str = "user"):
    session_id: Optional[str] = None
    if not new:
        existing_sessions: List[str] = storage.get_all_session_ids(user)
        if len(existing_sessions) > 0:
            session_id = existing_sessions[0]
    agent = Agent(
        model=Ollama("mistral"),
        session_id=session_id,
        user_id=user,
        knowledge=list(knowledge_base.document_lists),
        storage=storage,
        # Show tool calls in the response
        show_tool_calls=True,
        # Enable the agent to read the chat history
        read_chat_history=True,
        add_history_to_messages=True,
        # Number of historical responses to add to the messages.
        # num_history_responses=3,
    )
    if session_id is None:
        session_id = agent.session_id
        print(f"Started Session: {session_id}\n")
    else:
        print(f"Continuing Session: {session_id}\n")

    # Runs the agent as a cli app
    agent.cli_app(markdown=True)


if __name__ == "__main__":
    # Load the knowledge base: Comment after first run
    knowledge_base.load(recreate=False,upsert=True)
    all_docs = list(knowledge_base.document_lists)  # Convert generator to a list
    # for doc in all_docs:
    #     print(doc)  # Print extracted text

    # print(len(documents))
    typer.run(pdf_agent)