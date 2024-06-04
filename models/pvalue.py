from pydantic import BaseModel

class PValueResponse(BaseModel):
    pvalue: float