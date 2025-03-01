from pydantic import BaseModel
from typing import List

class VirginiaLandmarkSearchParameters(BaseModel):

    county_filters: List[str] = None
    location_type_filters: List[str] = None

    
