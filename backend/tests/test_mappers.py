from database import VirginiaLandmarkModel, VirginiaLandmarkRepository, get_context_session
from mappers import cvs_dict_to_virginia_landmark, virginia_landmarks_minimal_to_dicts
import unittest

class MapperTests(unittest.TestCase):


    def test_cvs_dict_to_virginia_landmark(self):

        raw_data = {
            "LandmkName": "Bull Run Library",
            "Address": "8051 Ashton Avenue",	
            "City": "Manassas",	
            "State": "VA",	
            "Zip": "20109",	
            "Phone": "703-792-4500",	
            "URL": "https://www.pwcva.gov/department/library/branch-locations-hours",	
            "X": "-77.52050983",	
            "Y": "38.78697117",	
            "SrcTyp": "Public Library",
            "FIPSname": "Prince William County"
        }

        model: VirginiaLandmarkModel = cvs_dict_to_virginia_landmark(raw_data)

        self.assertIsNotNone(model)
        self.assertEqual(model.landmark_name, "Bull Run Library")
        self.assertEqual(model.address, "8051 Ashton Avenue")
        self.assertEqual(model.city, "Manassas")
        self.assertEqual(model.state, "VA")
        self.assertEqual(model.zip, "20109")
        self.assertEqual(model.phone, "703-792-4500")
        self.assertEqual(model.url, "https://www.pwcva.gov/department/library/branch-locations-hours")
        self.assertEqual(model.longitude, -77.52050983)
        self.assertEqual(model.latitude, 38.78697117)
        self.assertEqual(model.location_type, "Public Library")
        self.assertEqual(model.location, "Prince William County")


    def test_virginia_landmarks_to_dicts(self):

        db_models: list[VirginiaLandmarkModel] = []

        with get_context_session() as db:
            repo: VirginiaLandmarkRepository = VirginiaLandmarkRepository(db)
            db_models: list[VirginiaLandmarkModel]  = repo.search()

        self.assertIsNotNone(db_models)

        raw_models: list[VirginiaLandmarkModel] = virginia_landmarks_minimal_to_dicts(db_models)

        self.assertIsNotNone(raw_models)
        self.assertGreater(len(raw_models), 1)

    