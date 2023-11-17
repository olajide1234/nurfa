from typing import Optional
from fastapi import APIRouter, HTTPException
import urllib.parse
from nurfa.services.news import get_news
from nurfa.consts import (
    date_now,
    date_one_month_ago,
)
from nurfa.services.pdl import get_company_name

router = APIRouter(
    prefix="/company",
)


@router.get(
    "/news",
    # response_model=UpdateOrganizationResponse,
)
def get_company_news(
    url: str,
    search: Optional[str] = None,
    fromTime: str = date_now,
    toTime: str = date_one_month_ago,
) -> dict:
    try:
        company_name = get_company_name(url)
        search_term = f"{company_name} {search}" if search else company_name
        company_news = get_news(
            search=urllib.parse.quote_plus(search_term),
            company_name=company_name,
            fromTime=fromTime,
            toTime=toTime,
        )
        
        return company_news
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
