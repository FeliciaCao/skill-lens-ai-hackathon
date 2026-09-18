from fastapi import APIRouter

from app.schemas import HealthResponse, SkillRequest, SkillResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health():
    return HealthResponse(status="ok")


@router.post("/skills/analyze", response_model=SkillResponse)
def analyze_skill(request: SkillRequest):
    return SkillResponse(
        skill_name=request.skill_name,
        analysis=f"Analysis result for {request.skill_name}",
    )
