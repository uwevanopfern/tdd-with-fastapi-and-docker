# pylint: disable=import-error
# pylint: disable=no-name-in-module
# pylint: disable=no-member
from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary
from typing import Union, List


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(url=payload.url, summary=payload.summary,)
    await summary.save()
    return summary.id


async def get(id: int) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary[0]
    return None


async def get_all() -> List:
    summaries = await TextSummary.all().values()
    return summaries
