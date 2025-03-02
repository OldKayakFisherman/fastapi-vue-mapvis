from pydantic import BaseModel


class VirginiaLandmarkSearchResponse(BaseModel):

    data: list = [dict]
    execution_time: float = 0
    record_count: int = 0
    success:bool = True

class VirginiaLandmarkLookupResponse(BaseModel):

    data: list = [dict]
    lookup_type: str = None
    execution_time: float = 0
    record_count: int = 0
    success:bool = True



