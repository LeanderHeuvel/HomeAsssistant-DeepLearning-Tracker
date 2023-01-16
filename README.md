# HomeAsssistant-DeepLearning-Tracker
This repository contains the code the for the Home Assistant Deep Learning Tracker

The hass_dl_tracker packages allows to easily upload your deeplearning metrics through home assistant while training.

## Installation

```

python3 -m pip install --index-url https://github.com/LeanderHeuvel/HomeAsssistant-DeepLearning-Tracker --no-deps deeplearningtracker_leandervandenheuvel
pip install git+https://github.com/LeanderHeuvel/HomeAsssistant-DeepLearning-Tracker.git#egg=deeplearningtracker_leandervandenheuvel
```

## Home Assistant Requirements

1. Obtain a [long lived access token](https://community.home-assistant.io/t/how-to-get-long-lived-access-token/162159)
2. Obtain webhook ID: create an automation, in trigger use 'webhook', an webhook_id will appear.
3. Get your home assistant instance url (including port number), e.g. http://homeassistant.local:8123
4. install the package, see usage

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