from fastapi import APIRouter, Request, status
from services.agent import get_response
from core.security import limiter
from schemas.agent import AgentResponse, AgentRequest

router = APIRouter()


@router.post(
    "/basic",
    response_model=AgentResponse,
    status_code=status.HTTP_200_OK,
)
@limiter.limit("3/day")
async def get_basic_response(
    request: Request,
    agent_request: AgentRequest,
):
    return AgentResponse(response=get_response(agent_request.query))
