import json
from nurfa.services.api.news_api import NewsAPIWrapper
from dotenv import load_dotenv
from nurfa.services.llm import LlmWrapper

load_dotenv()


def get_news(search: str, company_name: str, fromTime: str, toTime: str) -> dict:
    try:
        news_api = NewsAPIWrapper()
        llm = LlmWrapper()
        news = news_api.all_news(
            q=search,
            fromTime=fromTime,
            toTime=toTime,
            language="en",
            sortBy="relevancy",
            pageSize=30,
        )
        
        summary = llm.summarize(news=news, sentences_number=50, company_name=company_name)
        
        return dict(
            search=search,
            summary=summary,
            news=[
                dict(
                    title=new["title"],
                    description=new["description"],
                    url=new["url"],
                    published_at=new["publishedAt"],
                    content=new["content"],
                )
                for new in news["articles"]
            ],
        )
    except Exception as e:
        raise ValueError(str(e))
