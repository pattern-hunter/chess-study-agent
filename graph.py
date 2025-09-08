from langgraph.graph import START, StateGraph
from langgraph.graph.state import CompiledStateGraph
import classes as cls
import steps
from datetime import datetime

# TODO: human-in-the-loop
def build_graph():
    graph_builder = StateGraph(cls.State).add_sequence(
        # [steps.get_lichess_params, steps.generate_answer]
        [steps.get_lichess_params, steps.download_lichess_games, steps.analyze_games]
    )
    graph_builder.add_edge(START, "get_lichess_params")
    graph = graph_builder.compile()
    return graph

def execute_graph(graph: CompiledStateGraph, state: cls.State) -> cls.State:
    start = datetime.now()
    for step in graph.stream(state, stream_mode="updates"):
        if "analyze_games" in step:
            seconds = (datetime.now() - start).total_seconds()
            print(f"Elapsed time: {int(seconds/60)}m {int(seconds % 60)}s\n")
            print(f"Here is the analysis:\n{step['analyze_games']['answer']}")

    return state