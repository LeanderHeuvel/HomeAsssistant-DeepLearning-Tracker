# HomeAsssistant-DeepLearning-Tracker
This repository contains the code the for the Home Assistant Deep Learning Tracker

The hass_dl_tracker packages allows to easily upload your deeplearning metrics through home assistant while training.

## Installation

```
pip install git+https://github.com/LeanderHeuvel/HomeAsssistant-DeepLearning-Tracker.git#egg=deeplearningtracker_leandervandenheuvel
```

## Usage

```

from deeplearningtracker_leandervandenheuvel import DeepLearningTracker


API_KEY = 'your long lived access token'
HASS_URL = 'your home assistant url'
WEBHOOK_ID = 'your webhook id'
model_name = "DeepLearningTest"

upload = DeepLearningTracker(model_name,HASS_URL, API_KEY,WEBHOOK_ID)

##upload any metrics by adding them to the constructer of update_state(). By default the loss will be used to update the 'state' attribute of the entity.
upload.update_state(loss = i*0.45, epoch = i, accuracy_val = 74)

```