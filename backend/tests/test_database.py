from config import AppSettings
from database import VirginiaLandmarkRepository, get_context_session
from database import ensure_database_created
from pipelines import VirginiaLandmarkPipeline
import unittest

class VirginiaLandmarkRepositoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #ensure we are setup and have data
        ensure_database_created()

        settings = AppSettings()
        
        with get_context_session() as db:
            VirginiaLandmarkPipeline().injest(settings=settings, db=db)
        

    def test_get_location_counties(self):
        with get_context_session() as db:
            repo: VirginiaLandmarkRepository = VirginiaLandmarkRepository(db)
            self.assertGreater(len(repo.get_locations()), 0)

    def test_get_location_types(self) :
        with get_context_session() as db:
            repo: VirginiaLandmarkRepository = VirginiaLandmarkRepository(db)
            self.assertGreater(len(repo.get_location_types()), 0)
 