import os
from nurfa.services.types import PdlCompanyType

import requests
from pydantic import BaseModel, model_validator

PDL_API_KEY_ENV = "PDL_API_KEY"


class PdlAPIWrapper(BaseModel):
    """Enrich company data with PDL.

    Have the pdl api key set in the environment variable ``PDL_API_KEY``.

    Example:
        .. code-block:: python

            from nurfa.services.api.pdl_api import PdlAPIWrapper
            pdlApi = PdlAPIWrapper()
            pdlApi.enrich_company('testcompany.com')
    """

    base_url: str = "https://api.peopledatalabs.com/v5/company/enrich"

    @model_validator(mode="after")
    def validate_environment(self):
        """Validate if api key exists in environment."""
        api_key = os.environ.get(PDL_API_KEY_ENV)

        if not api_key:
            raise ValueError(f"{PDL_API_KEY_ENV} environment variable not set")

        return self

    def enrich_company(
        self,
        domain: str,
    ) -> PdlCompanyType:
        """Enrich domain with PDL
        Args: 
            domain: Domain of the company to enrich.
        """
        # Check supplied arguments and construct into a dictionary if argument is supplied
        params: dict[str, str] = {}
        params["website"] = domain

        message = self._everything(params)
        return message

    def _everything(self, params: dict) -> PdlCompanyType:
        headers = {
            "X-Api-Key": f"{os.environ[PDL_API_KEY_ENV]}",
            "Accept": "application/json",
        }
        req = requests.PreparedRequest()
        req.prepare_url(
            self.base_url,
            params,
        )

        if req.url is None:
            raise ValueError("prepared url is None, this should not happen")

        response = requests.get(req.url, headers=headers)

        if not response.ok:
            raise Exception(f"HTTP error {response.status_code}")
        return response.json()
