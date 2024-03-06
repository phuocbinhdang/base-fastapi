from pydantic import BaseModel


class CreateDTO(BaseModel):
    name: str
