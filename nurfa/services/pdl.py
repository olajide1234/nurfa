import json
from nurfa.services.api.pdl_api import PdlAPIWrapper
from dotenv import load_dotenv
from expiring_dict import ExpiringDict
from tldextract import extract

CACHE_TTL = 60 * 60 * 24 * 30 * 2  # Two months. We only need to cache the company name for a long time.
cache = ExpiringDict(ttl=CACHE_TTL)

load_dotenv()

def get_company_name(url: str) -> str:
    try:
        if url in cache:
            return str(cache[url]['name'])
        
        pdl_api = PdlAPIWrapper()
        # extract domain from url
        ext = extract(url)
        domain = ext.domain + '.' + ext.suffix
        data = pdl_api.enrich_company(domain=domain)
        cache[url] = data
        return data['name']
    except Exception as e:
        raise ValueError(str(e))
