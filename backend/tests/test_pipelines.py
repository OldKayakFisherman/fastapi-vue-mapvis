from config import AppSettings
from database import get_context_session, ensure_database_created
from pipelines import GenericPipelineResponse, VirginiaLandmarkPipeline
import unittest


class VirginiaLandmarkPipelineTests(unittest.TestCase):

    def test_injest(self):

        ensure_database_created()

        settings = AppSettings()

        settings.refresh_data = True
        pipeline: VirginiaLandmarkPipeline = VirginiaLandmarkPipeline()
        response: GenericPipelineResponse = None

        with get_context_session() as db:
            response = pipeline.injest(db=db, settings=settings) 

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.data_filepath)
        self.assertIsNotNone(response.data_pipeline)
        self.assertIsNone(response.error)
        self.assertGreater(response.records_imported, 0)
        self.assertGreater(response.execution_time, 0)
    