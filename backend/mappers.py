from database import VirginiaLandmarkModel


def cvs_dict_to_virginia_landmark(record: dict) -> VirginiaLandmarkModel:

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
    model.location = record["FIPSname"]

    return model


def virginia_landmarks_minimal_to_dicts(records: list[VirginiaLandmarkModel]) -> list[dict]:

    results: list[dict] = []

    if records:
        for record in records:
            row = {}

            row["id"] = record.id
            row["landmark_name"] = record.landmark_name


            row["latitude"] = str(record.latitude)
            row["longitude"] = str(record.longitude)

            results.append(row)

    return results

