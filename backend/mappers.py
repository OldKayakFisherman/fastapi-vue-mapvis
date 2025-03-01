from database import VirginiaLandmarkModel
from typing import Dict


def cvs_dict_to_virginia_landmark(record: Dict) -> VirginiaLandmarkModel:

    model: VirginiaLandmarkModel = VirginiaLandmarkModel()

    model.landmark_name = record['LandmkName']
    model.address = record['Address']
    model.city = record['City']
    model.state = record['State']
    model.zip = record["Zip"]
    model.phone = record["Phone"]
    model.url = record["URL"]
    model.latitude = float(record["Y"])
    model.longitude = float(record["X"])
    model.location_type = record["SrcTyp"]
    model.location_county = record["FIPSname"]

    return model


