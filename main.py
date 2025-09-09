import agent.agent as ag
import agent.graph as grp
import sys

if len(sys.argv) > 1:
    model = sys.argv[1]
    state = ag.init_state(prompt=ag.init_prompt(), llm=ag.init_llm(model))
    state["question"] = "Analyze the last game and tell me areas of improvement."
    graph = grp.build_graph()
    state = grp.execute_graph(graph=graph, state=state)
else:
    print("Please provide an Ollama model name; e.g. python main.py llama3.1")