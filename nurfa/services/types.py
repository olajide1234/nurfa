from typing import TypedDict


class Source(TypedDict):
    id: str
    name: int


class News(TypedDict):
    source: Source
    author: str
    title: str
    description: str
    url: str
    urlToImage: str
    publishedAt: str
    content: str


class Result(TypedDict):
    status: str
    totalResults: int
    articles: list[News]


class OpenAIMessage(TypedDict):
    role: str
    content: str


class OpenAIChoices(TypedDict):
    index: int
    message: OpenAIMessage
    finish_reason: str


class OpenAIUsage(TypedDict):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class OpenAIResponse(TypedDict):
    id: str
    object: str
    created: int
    model: str
    choices: list[OpenAIChoices]
    usage: OpenAIUsage

class PdlCompanyType(TypedDict):
    status: int
    name: str
    size: str
    employee_count: int
    id: str
    founded: int
    industry: str
    naics: list[dict]
    sic: list[dict]
    location: dict
    linkedin_id: str
    linkedin_url: str
    facebook_url: str
    twitter_url: str
    profiles: list[str]
    website: str
    ticker: str
    gics_sector: str
    mic_exchange: str
    type: str
    summary: str
    tags: list[str]
    headline: str
    alternative_names: list[str]
    alternative_domains: list[str]
    affiliated_profiles: list[str]
    employee_count_by_country: dict[str, int]
    likelihood: int
