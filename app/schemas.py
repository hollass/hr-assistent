from typing import List, Optional
from pydantic import BaseModel, Field


class ChunkScore(BaseModel):
    chunk_index: int
    similarity: float = Field(..., ge=0.0, le=1.0)
    explanation: Optional[str] = None


class SemanticScore(BaseModel):
    overall_score: float = Field(..., ge=0.0, le=1.0)
    chunk_scores: List[ChunkScore]


class SkillMatch(BaseModel):
    skill: str


class SkillResult(BaseModel):
    cv_skills: List[str]
    jd_skills: List[str]
    matched: List[SkillMatch]
    score: float = Field(..., ge=0.0, le=1.0)


class BiasResult(BaseModel):
    keywords_found: List[str]
    risk: bool


class BiasBaseline(BaseModel):
    gender: BiasResult
    age: BiasResult
    nationality: BiasResult


class FairnessScore(BaseModel):
    gender: float = Field(..., ge=0.0, le=1.0)
    age: float = Field(..., ge=0.0, le=1.0)
    nationality: float = Field(..., ge=0.0, le=1.0)


class FairnessBlock(BaseModel):
    cv: FairnessScore
    jd: FairnessScore


class FairnessResult(BaseModel):
    baseline: BiasBaseline
    scoring: FairnessBlock


class LLMInsight(BaseModel):
    summary: str
    skill_gaps: List[str]
    fairness_risks: List[str]
    recommendation: str


class MatchResponse(BaseModel):
    semantic: SemanticScore
    skills: SkillResult
    fairness: FairnessResult
    llm_insight: Optional[LLMInsight] = None

class CandidateProfile(BaseModel):
    candidate_id: str
    cv_text: str


class RankedCandidate(BaseModel):
    candidate_id: str
    score: float
    semantic: SemanticScore
    skills: SkillResult


class ATSRankingResponse(BaseModel):
    jd_text: str
    results: List[RankedCandidate]
