# Chess Coach AI Agent

Currently, this agent will download your latest game on Lichess, analyze it, and give feedback on areas of improvement.

## Usage

Steps to run it locally:

- Download your favorite model from Ollama
- Provide the name of the model while running the code `python main.py llama3.1` (replace `llama3.1` with your desired model)

## Upcoming Improvements

- Dockerize lichess MCP server
- Download games from chess.com as well
- Specify game types to analyze (e.g. blitz, rapid, etc.)
- Specify number of games and timeframe to analyze (e.g. analyze 10 games from the last week)
- Run local agent
