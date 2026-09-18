from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str


class SkillRequest(BaseModel):
    skill_name: str


class SkillResponse(BaseModel):
    skill_name: str
    analysis: str
