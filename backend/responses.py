from pydantic import BaseModel


class VirgniaLandmarkSearchResponse(BaseModel):

    data: list[dict] = []
    county_filters: list[str] = []
    location_filters: list[str] = []
    execution_time: float = 0
    record_count: int = 0
    success:bool = True


