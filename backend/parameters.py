from pydantic import BaseModel
from typing import Optional

class VirginiaLandmarkSearchParameters(BaseModel):

    location_filters: Optional[list[str]] = None
    location_type_filters: Optional[list[str]] = None

    
