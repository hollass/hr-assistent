from pydantic import BaseModel


class CV(BaseModel):
    text: str


class JobDescription(BaseModel):
    text: str


class MatchResult(BaseModel):
    score: float
    model: str