from pydantic import BaseModel


class SummaryPayloadSchema(BaseModel):
    url: str
    summary: str


class SummaryResponseSchema(SummaryPayloadSchema):
    id: int
