from database import VirginiaLandmarkRepository, get_context_session
import unittest

class VirginiaLandmarkRepositoryTest(unittest.TestCase):


    def test_get_location_counties(self):
        with get_context_session() as db:
            repo: VirginiaLandmarkRepository = VirginiaLandmarkRepository(db)
            self.assertGreater(len(repo.get_locations()), 0)

    def test_get_location_types(self) :
        with get_context_session() as db:
            repo: VirginiaLandmarkRepository = VirginiaLandmarkRepository(db)
            self.assertGreater(len(repo.get_location_types()), 0)
 