import os
from typing import Union, Optional
from nurfa.consts import (
    PossibleCategory,
    PossibleCountry,
    PossibleLanguage,
    PossibleSearchIn,
    PossibleSortBy,
)
from nurfa.services.types import Result

import requests
from pydantic import BaseModel, model_validator

NEWS_API_KEY_ENV = "NEWS_API_KEY"


class NewsAPIWrapper(BaseModel):
    """Fetch news from news api https://newsapi.org/.

    Have the news api key set in the environment variable ``NEW_API_KEY``.

    Example:
        .. code-block:: python

            from nurfa.services.api.new_api import NewsAPIWrapper
            newsApi = NewsAPIWrapper()
            newsApi.everything('testcompany.com')
            newsApi.top_headlines('human@testcompany.com')
    """

    base_url: str = "https://newsapi.org/v2/{route}"

    @model_validator(mode="after")
    def validate_environment(self):
        """Validate if api key exists in environment."""
        api_key = os.environ.get(NEWS_API_KEY_ENV)

        if not api_key:
            raise ValueError(f"{NEWS_API_KEY_ENV} environment variable not set")

        return self

    def all_news(
        self,
        q: str,
        searchIn: Optional[PossibleSearchIn] = None,
        sources: Optional[str] = None,
        domains: Optional[str] = None,
        excludeDomains: Optional[str] = None,
        fromTime: Optional[str] = None,
        toTime: Optional[str] = None,
        language: Optional[PossibleLanguage] = None,
        sortBy: Optional[PossibleSortBy] = None,
        pageSize: int = 100,
        page: int = 1,
    ) -> Result:
        """Search through millions of articles from over 80,000 large and small news sources and blogs.
        This endpoint suits article discovery and analysis.

        Args: Full description here: https://newsapi.org/docs/endpoints/everything
            q: Keywords or phrases to search for in the article title and body.
            searchIn: The fields to restrict your q search to.
            sources: A comma-seperated string of identifiers (maximum 20) for the news sources or blogs you want headlines from
            domains: A comma-seperated string of domains (eg bbc.co.uk, techcrunch.com, engadget.com) to restrict the search to.
            excludeDomains: A comma-seperated string of domains (eg bbc.co.uk, techcrunch.com, engadget.com) to remove from the results.
            from: A date and optional time for the oldest article allowed. This should be in ISO 8601 format
            (e.g. 2021-04-17 or 2021-04-17T00:00:00) Default: the oldest according to your plan.
            to: A date and optional time for the newest article allowed. This should be in ISO 8601 format
            (e.g. 2021-04-17 or 2021-04-17T00:00:00) Default: the newest according to your plan.
            language: The 2-letter ISO-639-1 code of the language you want to get headlines for. Default: all languages returned.
            sortBy: The order to sort the articles in. Possible options: relevancy, popularity, publishedAt. Default: publishedAt.
            pageSize: The number of results to return per page. 20 is the default, 100 is the maximum.
            page: Use this to page through the results.

        """
        # Check supplied arguments and construct into a dictionary if argument is supplied
        params: dict[str, Union[str, int]] = {}
        if q:
            params["q"] = q
        if searchIn:
            params["searchIn"] = searchIn
        if sources:
            params["sources"] = sources
        if domains:
            params["domains"] = domains
        if excludeDomains:
            params["excludeDomains"] = excludeDomains
        if fromTime:
            params["from"] = fromTime
        if toTime:
            params["to"] = toTime
        if language:
            params["language"] = language
        if sortBy:
            params["sortBy"] = sortBy
        if pageSize:
            params["pageSize"] = pageSize
        if page:
            params["page"] = page

        message = self._everything(params)
        return message

    def top_news(
        self,
        country: Optional[PossibleCountry],
        category: Optional[PossibleCategory] = None,
        sources: Optional[str] = None,
        q: Optional[str] = None,
        pageSize: int = 100,
        page: int = 1,
    ) -> Result:
        """This endpoint provides live top and breaking headlines for a country, specific category in a country, single source,
            or multiple sources.
            You can also search with keywords. Articles are sorted by the earliest date published first.
            This endpoint is great for retrieving headlines for use with news tickers or similar.

        Args: Full description here: https://newsapi.org/docs/endpoints/top-headlines
            country: The 2-letter ISO 3166-1 code of the country you want to get headlines for.
            Note: you can't mix this param with the sources param.
            category: The category you want to get headlines for.
            sources: A comma-seperated string of identifiers for the news sources or blogs you want headlines from.
            q: Keywords or a phrase to search for.
            pageSize: The number of results to return per page. 20 is the default, 100 is the maximum.
            page: Use this to page through the results.
        """
        # Check supplied arguments and construct into a dictionary if argument is supplied
        params: dict[str, Union[str, int]] = {}
        if country:
            params["country"] = country
        if category:
            params["category"] = category
        if sources:
            params["sources"] = sources
        if q:
            params["q"] = q
        if pageSize:
            params["pageSize"] = pageSize
        if page:
            params["page"] = page

        message = self._top_headlines(params)
        return message

    def _everything(self, params: dict) -> Result:
        headers = {
            "Authorization": f"Bearer {os.environ[NEWS_API_KEY_ENV]}",
            "Accept": "application/json",
        }
        req = requests.PreparedRequest()
        req.prepare_url(
            self.base_url.format(route="everything"),
            params,
        )
        print(req.url)

        if req.url is None:
            raise ValueError("prepared url is None, this should not happen")

        response = requests.get(req.url, headers=headers)
        print(req.url)

        if not response.ok:
            raise Exception(f"HTTP error {response.status_code}")
        return response.json()

    def _top_headlines(self, params: dict) -> Result:
        headers = {
            "Authorization": f"Bearer {os.environ[NEWS_API_KEY_ENV]}",
            "Accept": "application/json",
        }
        req = requests.PreparedRequest()
        req.prepare_url(self.base_url.format(route="top-headlines"), params)

        if req.url is None:
            raise ValueError("prepared url is None, this should not happen")

        response = requests.get(req.url, headers=headers)

        if not response.ok:
            raise Exception(f"HTTP error {response.status_code}")
        return response.json()
