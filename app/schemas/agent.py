from sqlmodel import Field, SQLModel


class AgentRequest(SQLModel):
    query: str | None = None


class AgentResponse(SQLModel):
    response: str = Field(default="Agent response")
