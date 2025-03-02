from database import VirginiaLandmarkModel
from database import VirginiaLandmarkRepository
import logging
from mappers import virginia_landmarks_minimal_to_dicts
from parameters import VirginiaLandmarkSearchParameters
from responses import VirginiaLandmarkSearchResponse, VirginiaLandmarkLookupResponse
from sqlalchemy.orm import Session
from timers import GeneralTimer


logger = logging.getLogger(__name__)

class VirginiaLandmarkService:

    def perform_search(self, db: Session ,request: VirginiaLandmarkSearchParameters) -> VirginiaLandmarkSearchResponse:

        response: VirginiaLandmarkSearchResponse = VirginiaLandmarkSearchResponse() 
        repo: VirginiaLandmarkRepository = VirginiaLandmarkRepository(db)

        timer: GeneralTimer = GeneralTimer()

        try:
            with timer:
                records: list[VirginiaLandmarkModel] = repo.search(request.location_filters, request.location_type_filters)
                response.record_count = len(records)
                response.data = virginia_landmarks_minimal_to_dicts(records)
                
        except Exception as ex:
            logger.error(ex)
            response.success = False
        finally:
            response.execution_time = timer.expired_milliseconds
            return response


    def get_location_lookups(self, db: Session) -> VirginiaLandmarkLookupResponse:
        response: VirginiaLandmarkLookupResponse = VirginiaLandmarkLookupResponse() 
        repo: VirginiaLandmarkRepository = VirginiaLandmarkRepository(db)

        timer: GeneralTimer = GeneralTimer()

        try:
            with timer:
                
                response.data = repo.get_locations()
                response.record_count = len(response.data)
                response.lookup_type = "Virginia Landmark Locations"

        except Exception as ex:
            logger.error(ex)
            response.success = False
        finally:
            response.execution_time = timer.expired_milliseconds
            return response


    def get_location_type_lookups(self, db: Session) -> VirginiaLandmarkLookupResponse:
        response: VirginiaLandmarkLookupResponse = VirginiaLandmarkLookupResponse() 
        repo: VirginiaLandmarkRepository = VirginiaLandmarkRepository(db)

        timer: GeneralTimer = GeneralTimer()

        try:
            with timer:
                
                response.data = repo.get_location_types()
                response.record_count = len(response.data)
                response.lookup_type = "Virginia Landmark Location Types"

        except Exception as ex:
            logger.error(ex)
            response.success = False
        finally:
            response.execution_time = timer.expired_milliseconds
            return response


