from datetime import datetime, timedelta
from typing import Literal


PossibleCategory = Literal[
    "business", "entertainment", "general", "health", "science", "sports", "technology"
]

PossibleCountry = Literal[
    "ae",
    "ar",
    "at",
    "au",
    "be",
    "bg",
    "br",
    "ca",
    "ch",
    "cn",
    "co",
    "cu",
    "cz",
    "de",
    "eg",
    "fr",
    "gb",
    "gr",
    "hk",
    "hu",
    "id",
    "ie",
    "il",
    "in",
    "it",
    "jp",
    "kr",
    "lt",
    "lv",
    "ma",
    "mx",
    "my",
    "ng",
    "nl",
    "no",
    "nz",
    "ph",
    "pl",
    "pt",
    "ro",
    "rs",
    "ru",
    "sa",
    "se",
    "sg",
    "si",
    "sk",
    "th",
    "tr",
    "tw",
    "vu",
    "av",
    "us",
    "ve",
    "za",
]

PossibleSearchIn = Literal[
    "title",
    "description",
    "content",
    "title,description",
    "title,content",
    "description,content",
    "title,description,content",
]

PossibleSortBy = Literal["relevancy", "popularity", "publishedAt"]

PossibleLanguage = Literal[
    "ar", "de", "en", "es", "fr", "he", "it", "nl", "no", "pt", "ru", "sv", "ud", "zh"
]

date_now = datetime.now().isoformat()
date_one_month_ago = (datetime.now() - timedelta(days=30)).isoformat()
