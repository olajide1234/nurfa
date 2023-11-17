import json
from nurfa.services.api.pdl_api import PdlAPIWrapper
from dotenv import load_dotenv
from expiring_dict import ExpiringDict
from tldextract import extract

CACHE_TTL = 60 * 60 * 24 * 30 * 2  # Two months. We only need to cache the company name for a long time.
cache = ExpiringDict(ttl=CACHE_TTL)

load_dotenv()

def get_company_name(url: str) -> str:
    # print('---cache before fetch--->' + cache[url])
    try:
        if url in cache:
            # print('----get company name cache exit---->' + cache[url]['name'])
            return str(cache[url]['name'])
        
        pdl_api = PdlAPIWrapper()
        # extract domain from url
        ext = extract(url)
        domain = ext.domain + '.' + ext.suffix
        # print(domain)
        data = pdl_api.enrich_company(domain=domain)
        cache[url] = data
        # print('---cache after fetch--->' + cache[url])
        return data['name']
    except Exception as e:
        raise ValueError(str(e))
