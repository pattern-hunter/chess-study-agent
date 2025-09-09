from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
import classes as cls
import graph as grp

def init_prompt() -> ChatPromptTemplate:
    system_message = """
    Given an input question, determine the number of games that need to be extracted. Default is 1.
    """
    user_prompt = "Question: {question}"

    return ChatPromptTemplate(
        [("system", system_message), ("user", user_prompt)]
    )

def init_llm() -> ChatOllama:
    # DeepSeek models like DeepSeek-R1 or V3 are generally better for complex reasoning
    # and multi-step analysis, making them more suitable for providing detailed positional insights.
    # Llama models are better for general language tasks and offer speed and flexibility but 
    # lack the depth for complex reasoning required in detailed chess analysis.

    return ChatOllama(model="llama3.1")
    # return ChatOllama(model="deepseek-r1:8b")

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
state["question"] = "Analyze the last game and tell me areas of improvement."
graph = grp.build_graph()
state = grp.execute_graph(graph=graph, state=state)