from config import AppSettings
from database import get_context_session, ensure_database_created
from parameters import VirginiaLandmarkSearchParameters
from pipelines import VirginiaLandmarkPipeline
from responses import VirginiaLandmarkSearchResponse, VirginiaLandmarkLookupResponse
from services import VirginiaLandmarkService
import unittest


class VirginiaLandmarkServiceTests(unittest.TestCase):

    def test_basic_search(self):

        settings: AppSettings = AppSettings()
        pipeline: VirginiaLandmarkPipeline = VirginiaLandmarkPipeline()
    

        with get_context_session() as db:
            
            #ensure the database is created
            ensure_database_created()

            #make sure we have data
            settings.refresh_data = True
            pipeline.injest(settings, db)

            #create our request
            request: VirginiaLandmarkSearchParameters = VirginiaLandmarkSearchParameters() 

            #create our service
            service: VirginiaLandmarkService = VirginiaLandmarkService()

            #perform a basic search
            response: VirginiaLandmarkSearchResponse = service.perform_search(db, request)

            #test our result
            self.assertIsNotNone(response)
            self.assertEqual(response.record_count, 7026)
            self.assertEqual(len(response.data), 7026)
            self.assertTrue(response.success)

    def test_county_filter(self):
        settings: AppSettings = AppSettings()
        pipeline: VirginiaLandmarkPipeline = VirginiaLandmarkPipeline()
    

        with get_context_session() as db:
            
            #ensure the database is created
            ensure_database_created()

            #make sure we have data
            settings.refresh_data = True
            pipeline.injest(settings, db)

            #create our request
            request: VirginiaLandmarkSearchParameters = VirginiaLandmarkSearchParameters() 

            #add a county filter
            request.location_filters = ["Fairfax County"]

            #create our service
            service: VirginiaLandmarkService = VirginiaLandmarkService()

            #perform a basic search
            response: VirginiaLandmarkSearchResponse = service.perform_search(db, request)

            #test our result
            self.assertIsNotNone(response)
            self.assertNotEqual(response.record_count, 7026)
            self.assertNotEqual(len(response.data), 7026)
            self.assertGreater(response.record_count,0)
            self.assertGreater(len(response.data), 0)
            self.assertTrue(response.success)



    def test_location_type_filter(self):
        settings: AppSettings = AppSettings()
        pipeline: VirginiaLandmarkPipeline = VirginiaLandmarkPipeline()
    

        with get_context_session() as db:
            
            #ensure the database is created
            ensure_database_created()

            #make sure we have data
            settings.refresh_data = True
            pipeline.injest(settings, db)

            #create our request
            request: VirginiaLandmarkSearchParameters = VirginiaLandmarkSearchParameters() 

            #add a county filter
            request.location_type_filters = ["Airports"]

            #create our service
            service: VirginiaLandmarkService = VirginiaLandmarkService()

            #perform a basic search
            response: VirginiaLandmarkSearchResponse = service.perform_search(db, request)

            #test our result
            self.assertIsNotNone(response)
            self.assertNotEqual(response.record_count, 7026)
            self.assertNotEqual(len(response.data), 7026)
            self.assertGreater(response.record_count,0)
            self.assertGreater(len(response.data), 0)
            self.assertTrue(response.success)


    def test_get_location_lookups(self):

        with get_context_session() as db:

            #create our service
            service: VirginiaLandmarkService = VirginiaLandmarkService()

            response: VirginiaLandmarkLookupResponse = service.get_location_lookups(db=db)

            self.assertIsNotNone(response)
            self.assertGreater(len(response.data), 0)
            self.assertGreater(response.record_count, 0)
            self.assertTrue(response.success)

    def test_get_location_type_lookups(self):

        with get_context_session() as db:

            #create our service
            service: VirginiaLandmarkService = VirginiaLandmarkService()

            response: VirginiaLandmarkLookupResponse = service.get_location_type_lookups(db=db)

            self.assertIsNotNone(response)
            self.assertGreater(len(response.data), 0)
            self.assertGreater(response.record_count, 0)
            self.assertTrue(response.success)