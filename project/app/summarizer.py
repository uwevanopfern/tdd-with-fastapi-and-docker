# pylint: disable=import-error
import nltk
from newspaper import Article

from app.models.tortoise import TextSummary


async def generate_summary(summary_id: int, url: str) -> None:
    article = Article(url)
    article.download()  # HTML page data
    article.parse()  # convert HTML data into json format

    try:
        nltk.data.find("tokenizers/punkt")
    except LookupError:
        nltk.download("punkt")
    finally:
        article.nlp()

    summary = article.summary
    await TextSummary.filter(id=summary_id).update(summary=summary)
