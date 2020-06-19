BASE_HEADERS = {"Content-Type": "application/json"}


def build_headers(**kwargs) -> dict:
    headers = BASE_HEADERS.copy()

    for key, value in kwargs.items():
        if key == "User_Agent":
            headers.update({"User-Agent": value})
            continue
        headers.update({key: value})
    return headers
