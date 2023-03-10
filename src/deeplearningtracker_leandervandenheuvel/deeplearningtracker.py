from requests import post
import json


'''
A Deep Learning Tracker for Home Assistant
Author: Leander van den Heuvel

Deep Learning Tracker provides an easy way to keep track of your deep learning metrics while training via Home Assistant
When the model starts training, an announcement is made via a webhook. 

Metrics are updated via the Home Assistant REST API.

'''

class DeepLearningTracker():
    def __init__(self, model_name, hass_url, api_key, webhook_id):
        self.api_key = api_key
        self.webhook_id = webhook_id
        self.hass_url = hass_url+"/api/states/"
        self.sensor_name = "sensor."+model_name
        self.model_name = model_name
        self.make_announcement()
        
    def make_announcement(self):
        headers = {'content-type': 'application/json'}
        payload = json.dumps({"type": "data","data": {"model_name": str(self.model_name)}})
        url = self.hass_url + "/api/webhook/" + self.webhook_id
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