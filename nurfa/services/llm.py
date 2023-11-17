import os

from nurfa.services.types import Result
import openai

from pydantic import BaseModel, model_validator

OPENAI_API_KEY_ENV = "OPENAI_API_KEY"


class LlmWrapper(BaseModel):
    """initializes an llm instance.

    Have the openAI api key set in the environment variable ``OPENAI_API_KEY``.

    Example:
        .. code-block:: python

            from nurfa.services.llm import LlmWrapper
            llm = LlmWrapper()
            llm.summarize(news, 10)
    """

    base_url: str = "https://api.peopledatalabs.com/v5/company/enrich"

    @model_validator(mode="after")
    def validate_environment(self):
        """Validate if api key exists in environment."""
        api_key = os.environ.get(OPENAI_API_KEY_ENV)

        if not api_key:
            raise ValueError(f"{OPENAI_API_KEY_ENV} environment variable not set")

        return self

    def summarize(
        self,
        news: Result,
        sentences_number: int,
        company_name: str,
    ) -> str:
        """Summarize news with LLM
        Args:
            news: Result set from News API.
            sentences_number: Number of sentences to summarize.
        """
        # Extract all the contents into a giant string with space in between
        content = ""
        for new in news["articles"]:
            content += new["content"] + " "
            content += new["description"] + " "
            content += new["title"] + " "


        # Summarize with LLM
        summary: str = self.llm(content=content, sentences_number=sentences_number, company_name=company_name)
        return summary

    def llm(
        self,
        content: str,
        sentences_number: int,
        company_name: str,
    ) -> str:
        """Summarize news with LLM
        Args:
            content: Result set from News API.
        """
        # Summarize with LLM
        openai.api_key = os.environ.get(OPENAI_API_KEY_ENV)
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a helpful assistant who researchers analyse the new. Summarize the users given news into about {sentences_number} lines with a strong focus on how the news relates to {company_name}",
                },
                {"role": "user", "content": f"{content}"},
            ],
            temperature=0.4,
            max_tokens=2000,
            presence_penalty=1,
            frequency_penalty=1,
        )
        return response.choices[0].message.content
