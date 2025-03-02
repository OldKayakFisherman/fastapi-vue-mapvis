from config import AppSettings
from database import VirginiaLandmarkModel
from database import VirginiaLandmarkRepository
from dataclasses import dataclass
import os
from readers import read_virginia_landmarks
from sqlalchemy.orm import Session
from timers import GeneralTimer
from typing import List


@dataclass
class GenericPipelineResponse:

    records_imported: int = 0
    success: bool = False
    error: Exception = None
    execution_time: float = 0
    data_filepath: str = None
    data_pipeline: str = None


class VirginiaLandmarkPipeline:

    def injest(self, settings: AppSettings, db: Session) -> GenericPipelineResponse:
        
        response: GenericPipelineResponse = GenericPipelineResponse()
        repo: VirginiaLandmarkRepository = VirginiaLandmarkRepository(db)
        timer: GeneralTimer = GeneralTimer()
        
        existing_record_count = repo.record_count()

        try:
            with timer:

                response.data_pipeline = "Virginia Landmarks"

                if settings.refresh_data == True:
                    if existing_record_count > 0:
                        repo.truncate()

                if existing_record_count == 0:            
                    #construct our filepath
                    response.data_filepath = os.path.join(settings.data_dir_root, "Virginia_Landmarks.csv")

                    collected_models: List[VirginiaLandmarkModel] = read_virginia_landmarks(response.data_filepath)        

                    if len(collected_models) > 0:
                        repo.save_all(collected_models)
                        response.records_imported = len(collected_models)

                response.success = True

        except Exception as ex:
            response.error = ex
            response.success = False
        finally:
            response.execution_time = timer.expired_milliseconds
            return response
