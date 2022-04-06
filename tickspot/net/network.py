import json
import requests
import logging
from typing import Tuple
from tickspot.net.manual_settings import Constants


logger = logging.getLogger(__name__)


class Authorize(object):
    __slots__ = ["username", "password", "token", "sub_id"]

    def __init__(self, username: str, password: str):
        self.token, self.sub_id = self.authorize(username, password)

    def authorize(self, username: str, password: str) -> Tuple[str, str]:
        headers = {"User-agent": f"DPS ({username})"}
        r = requests.get(
            Constants.BaseUrl + "roles.json", headers=headers, auth=(username, password)
        )
        if r.status_code == 200:
            data = json.loads(r.text)[0]
            return data.get("api_token"), data.get("subscription_id")
        else:
            raise Exception(r.text)


class Resource(object):
    __slots__ = ["token", "sub_id"]
    """
    Base model for calls to TickSpot
    Note - add get, put and delete
    """

    def __init__(self, token, sub_id):
        self.token = token
        self.sub_id = sub_id

    def post(self, obj, data):
        headers = {"User-agent": f"DPS (andrew.beattie@farmersedge.ca)"}
        headers.update({"Authorization": f"Token token={self.token}"})
        r = requests.post(Constants.BaseUrlSubId % self.sub_id + obj, json=data, headers=headers)
        logger.debug(r.status_code)
        if r.status_code == 201:
            return json.loads(r.text)
        else:
            logger.warning(r.text)
            raise Exception(r.text)

    def get(self, obj):
        headers = {"User-agent": f"DPS (andrew.beattie@farmersedge.ca)"}
        headers.update({"Authorization": f"Token token={self.token}"})
        r = requests.get(Constants.BaseUrlSubId % self.sub_id + obj, headers=headers)
        logger.debug(r.status_code)
        if r.status_code == 200:
            logger.debug(r.text)
            return json.loads(r.text)
        else:
            logger.warning(r.text)
            return Exception(r.text)

    def list(self, obj):
        headers = {"User-agent": f"DPS (andrew.beattie@farmersedge.ca)"}
        headers.update({"Authorization": f"Token token={self.token}"})
        r = requests.get(Constants.BaseUrlSubId % self.sub_id + obj, headers=headers)
        logger.debug(r.status_code)
        if r.status_code == 200:
            return json.loads(r.text)
        else:
            logger.warning(r.text)
            return Exception(r.text)


class Entry(Resource):
    """
    Class for interacting with TickSpot entries
    """

    def __init__(self, sub_id: int, token: str):
        self.sub_id = sub_id
        self.token = token

    def post(self, data: dict):
        return super(Entry, self).post("/entries.json", data)

    def list(self, project_id: int, start_date: str, end_date: str):
        return super(Entry, self).get(
            f"/projects/{project_id}/entries.json?start_date={start_date}&end_date={end_date}"
        )


class Task(Resource):
    def __init__(self, sub_id: int, token: str):
        self.sub_id = sub_id
        self.token = token

    def list(self, project_id: int):
        """list

        :param int project_id: a specific TickSpot project id available to the user
        :return list: returns a list of dictionaries containing information on each task available to the user
        """
        if project_id:
            return super(Task, self).list(f"/projects/{project_id}/tasks.json")
        else:
            return super(Task, self).list("tasks.json")

    def get(self, task_id: int):
        return super(Task, self).get(f"/tasks/{task_id}.json")


class Project(Resource):
    def __init__(self, sub_id: int, token: str):
        self.sub_id = sub_id
        self.token = token

    def list(self):
        return super(Project, self).list("projects.json")

    def get(self, project_id: int):
        return super(Project, self).get(f"/projects/{project_id}.json")
