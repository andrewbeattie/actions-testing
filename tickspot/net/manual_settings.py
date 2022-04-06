from airflow.models import Variable 

class Constants:
    """
    URL that are used throughout the script
    """

    BaseUrl = "https://www.tickspot.com/api/v2/"
    BaseUrlSubId = "https://www.tickspot.com/%s/api/v2/"
    UserAgent = {"User-agent": f"DPS ({Variable.get('TICKSPOT_USERNAME')})"}
    DateFormat = "%Y-%m-%d"
