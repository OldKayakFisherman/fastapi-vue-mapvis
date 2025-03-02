def convert_string_to_bool(value: str) -> bool:
    return (value.lower() == "true" or value.lower() == "1" or value.lower() == "t")

def convert_str_list_to_unique(values: list[str]) -> list[str]:

    result: list[str] = []

    if values:
        for value in values:
            eval = [x for x in result if x == value]

            if eval is None:
                result.append(eval)

    return result