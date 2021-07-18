from tickspot.settings import env


class Tasks:
    """
    Dictionary of task labels and TickSpot ids
    """

    CAN = {
        "label": "Smart Agronomy - CAN",
        "id": 14519343,
    }
    US = {
        "label": "Smart Agronomy - US",
        "id": 14519344,
    }
    Trace = {
        "label": "Traceability",
        "id": 14625862,
    }
    Stat = {"label": "Stat Holiday", "id": 15434840}
    Vac = {"label": "Vacation", "id": 15434841}


class Constants:
    """
    URL that are used throughout the script
    """

    BaseUrl = "https://www.tickspot.com/api/v2/"
    BaseUrlSubId = "https://www.tickspot.com/%s/api/v2/"
    UserAgent = {"User-agent": f"DPS ({ env.get('TICKSPOT_USERNAME')})"}
    DPSProjectId = 1955215
    DateFormat = "%Y-%m-%d"
