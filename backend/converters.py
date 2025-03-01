def convert_string_to_bool(value: str) -> bool:
    return (value.lower() == "true" or value.lower() == "1" or value.lower() == "t")
