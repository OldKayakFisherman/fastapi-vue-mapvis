from database import VirginiaLandmarkModel
from database import VirginiaLandmarkRepository
from parameters import VirginiaLandmarkSearchParameters
from responses import VirgniaLandmarkSearchResponse
from sqlalchemy.orm import Session
from timers import GeneralTimer
from typing import List

class VirginiaLandmarkService:

    def perform_search(self, db: Session ,request: VirginiaLandmarkSearchParameters) -> VirgniaLandmarkSearchResponse:

        response: VirgniaLandmarkSearchResponse = VirgniaLandmarkSearchResponse() 
        repo: VirginiaLandmarkRepository = VirginiaLandmarkRepository(db)

        timer: GeneralTimer = GeneralTimer()

        try:
            with timer:
                records: List[VirginiaLandmarkModel] = repo.search(db, request.county_filters, request.location_type_filters)
                response.county_filters = [x.location_county for x in records]
                response.location_filters = [x.location_type for x in records]
                response.record_count = len(records)
                response.data = [x.__dict__ for x in records]
                
        except Exception as ex:
            response.success = False
        finally:
            response.execution_time = timer.expired_milliseconds
            return response





