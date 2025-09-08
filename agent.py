from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
import classes as cls
import graph as grp

def init_prompt() -> ChatPromptTemplate:
    system_message = """
    Given an input question, determine the number of games that need to be extracted.
    """
    user_prompt = "Question: {question}"

    return ChatPromptTemplate(
        [("system", system_message), ("user", user_prompt)]
    )

def init_llm() -> ChatOllama:
    return ChatOllama(model="llama3.1")

def init_state(prompt: ChatPromptTemplate, llm: ChatOllama) -> cls.State:
    return cls.State(
        prompt_template = prompt,
        llm = llm,
        limit = 5000,
        question = "",
        query = "",
        result = "",
        answer = "",
        count = 0
    )

state = init_state(prompt=init_prompt(), llm=init_llm())
state["question"] = "Analyze the last 10 games and tell me areas of improvement."
graph = grp.build_graph()
state = grp.execute_graph(graph=graph, state=state)