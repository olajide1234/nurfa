Nurfa is an AI app that helps sales professionals work smarter and better. Nurfa helps sales professionals save time and effort by summarizing the most relevant news about their prospects. This saves you valuable time when preparing for meetings. It also makes the sales process go smoother because you're aware of the latest developments in your prospect's business and industry.

<img width="730" alt="Screenshot 2023-11-17 at 10 56 31 AM" src="https://github.com/olajide1234/nurfa/assets/42445456/860b2bd4-9541-40e0-8c6b-695d3325ff0c">

Technologies used: Python, FastAPI, OpenAI, Poetry, News API, People Data Labs API

To run the app:

- Clone the project
- Install Poetry (python package)
- Install app dependencies with `poetry install`
- Add env tokens to `.env`. file:

    NEWS_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    PDL_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    OPENAI_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

- Run app with `make dev`
- Visit app at `http://127.0.0.1:8000`
- You can make an example query in this format: `http://127.0.0.1:8000/v1/company/news?url=apple.com&search=iPhone%2015` by replacing the company URL and any search keywords you are interested in.
