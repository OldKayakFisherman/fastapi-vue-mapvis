from fastapi.testclient import TestClient
import json
from main import app
import unittest



class RouteEndpointTests(unittest.TestCase):

    def test_unfiltered_virginia_landmarks(self):

        client = TestClient(app)

        prms = {}

        response = client.post(url="/api/virginia/landmarks", json=prms)

        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        
        eval_content = json.loads(response.content)
        self.assertIsNotNone(eval_content)
        self.assertGreater(len(eval_content['data']), 0)

    def test_location_filtered_routes(self):

        client = TestClient(app)

        prms = {
            "location_filters": ["Fairfax County"]
        }

        response = client.post(url="/api/virginia/landmarks", json=prms)

        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        
        eval_content = json.loads(response.content)
        self.assertIsNotNone(eval_content)
        self.assertGreater(len(eval_content['data']), 0)

    def test_location_type_filtered_routes(self):

        client = TestClient(app)

        prms = {
            "location_type_filters": ["Airports"]
        }

        response = client.post(url="/api/virginia/landmarks", json=prms)

        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        
        eval_content = json.loads(response.content)
        self.assertIsNotNone(eval_content)
        self.assertGreater(len(eval_content['data']), 0)

    def test_get_landmark_locations(self):

        client = TestClient(app)

       
        response = client.get(url="/api/virginia/landmark/locations")

        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        
        eval_content = json.loads(response.content)
        self.assertIsNotNone(eval_content)
        self.assertGreater(len(eval_content['data']), 0)

    def test_get_landmark_location_types(self):

        client = TestClient(app)

        response = client.get(url="/api/virginia/landmark/location_types")

        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        
        eval_content = json.loads(response.content)
        self.assertIsNotNone(eval_content)
        self.assertGreater(len(eval_content['data']), 0)
