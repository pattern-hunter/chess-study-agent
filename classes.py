from typing_extensions import Annotated, TypedDict
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_ollama.chat_models import ChatOllama

class State(TypedDict):
    prompt_template: ChatPromptTemplate
    llm: ChatOllama 
    question: str
    result: str
    answer: str
    count: int
    games: str

class LichessParamsOutput(TypedDict):
    """Generated response."""

    count: Annotated[int, ..., "Number of games to be extracted"]