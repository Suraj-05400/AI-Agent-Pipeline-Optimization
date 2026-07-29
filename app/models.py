from pydantic import BaseModel


class AgentResponse(BaseModel):
    summary: str
    status: str
