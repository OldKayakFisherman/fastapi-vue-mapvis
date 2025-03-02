from database import SessionDep
from fastapi import APIRouter
import logging
from parameters import VirginiaLandmarkSearchParameters
from responses import VirginiaLandmarkSearchResponse, VirginiaLandmarkLookupResponse
from services import VirginiaLandmarkService


logger = logging.getLogger(__name__)

virginia_router = APIRouter(prefix="/virginia", tags=["virginia"])


@virginia_router.post("/landmarks")
async def landmarks(prms: VirginiaLandmarkSearchParameters, session: SessionDep) -> VirginiaLandmarkSearchResponse:
    service: VirginiaLandmarkService = VirginiaLandmarkService()
    result: VirginiaLandmarkSearchResponse = service.perform_search(db=session, request=prms)
    return result

@virginia_router.get("/landmark/locations")
async def locations(session: SessionDep) -> VirginiaLandmarkLookupResponse:
    service: VirginiaLandmarkService = VirginiaLandmarkService()
    result: VirginiaLandmarkLookupResponse = service.get_location_lookups(db=session)
    return result

@virginia_router.get("/landmark/location_types")
async def location_types(session: SessionDep) -> VirginiaLandmarkLookupResponse:
    service: VirginiaLandmarkService = VirginiaLandmarkService()
    result: VirginiaLandmarkLookupResponse = service.get_location_type_lookups(db=session)
    return result
