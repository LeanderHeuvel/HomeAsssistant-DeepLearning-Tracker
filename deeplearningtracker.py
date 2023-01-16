from requests import post
import json


__version__ = 'beta'

class DataUploader():
    def __init__(self, model_name, hass_url) -> None:
        self.api_key = API_KEY
        self.hass_url = HASS_URL+"/api/states/"
        self.sensor_name = "sensor."+model_name
        self.model_name = model_name
        self.make_announcement()
        
    def make_announcement(self):
        headers = {'content-type': 'application/json'}
        payload = json.dumps({"type": "data","data": {"model_name": str(self.model_name)}})
        url = HASS_URL + "/api/webhook/" + WEBHOOK_ID
        post(url, headers = headers, data=payload)

    def update_state(self, **kwargs):
        payload = {}
        attributes = {}
        for key, value in kwargs.items():
            if "loss" in key:
                payload['state'] = value
            attributes[key] = value
        attributes['icon'] = "mdi:chart-bell-curve-cumulative"
        attributes['unit_of_measurement'] = ''
        attributes['state_class'] = 'measurement'
        payload['attributes'] = attributes
        payload = json.dumps(payload)
        headers = {"Authorization": "Bearer "+self.api_key, "content-type": "application/json"}
        resp = post(self.hass_url + self.sensor_name, data=payload, headers=headers)
        return resp.text