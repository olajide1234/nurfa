Nurfa is an AI app that helps sales professionals work smarter and better. Nurfa helps sales professionals save time and effort by summarizing the most relevant news about their prospects. This saves you valuable time when preparing for meetings. It also makes the sales process go smoother because you're aware of the latest developments in your prospect's business and industry.

Technologies used: Python, FastAPI, OpenAI, Poetry, News API, People Data Labs API

To run the app:

1 - Clone the project
2 - Install Poetry (python package)
3 - Install app dependencies with `poetry install`
4 - Add env tokens to `.env`. file:

    NEWS_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    PDL_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    OPENAI_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

5 - Run app with `make dev`
6 - Visit app at `http://127.0.0.1:8000`
7 - You can make an example query in this format: `http://127.0.0.1:8000/v1/company/news?url=apple.com&search=iPhone%2015` by replacing the company URL and any search keywords you are interested in.