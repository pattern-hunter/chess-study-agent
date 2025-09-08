from langchain_community.tools.sql_database.tool import QuerySQLDatabaseTool
import classes as cls
import lichess

def get_lichess_params(state: cls.State):
    # TODO: add ability to supply 'since' parameter for lichess call.
    prompt = state["prompt_template"].invoke(
        {
            "question": state["question"],
        }
    )
    structured_llm = state["llm"].with_structured_output(cls.LichessParamsOutput)
    result = structured_llm.invoke(prompt)
    state["count"] = result["count"]
    state["result"] = result
    return state

def download_lichess_games(state: cls.State):
    print(f"Downloading {state['count']} games")
    games = lichess.get_user_games_from_lichess("pattern_hunter", 1736959353, int(state["count"]))
    state["games"] = games
    return state

def analyze_games(state: cls.State):
    prompt = (
        "Given the games in PGN notation, act like a chess coach and answer the question.\n"
        f"Games: {state['games']}"
        f"Question: {state['question']}"
    )
    response = state["llm"].invoke(prompt)
    state["answer"] = response.content
    return state