import csv
from database import VirginiaLandmarkModel
from mappers import cvs_dict_to_virginia_landmark
from typing import List

def read_virginia_landmarks(filepath: str) -> List[VirginiaLandmarkModel]:

    collected_models: List[VirginiaLandmarkModel] = []

    with open(filepath, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            collected_models.append(cvs_dict_to_virginia_landmark(row))

    return collected_models
