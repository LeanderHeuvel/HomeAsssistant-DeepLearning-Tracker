from config import API_KEY, HASS_URL, WEBHOOK_ID
from src.deeplearningtracker_leandervandenheuvel.deeplearningtracker import DeepLearningTracker
import time

model_name = "DeepLearningTest"


upload = DeepLearningTracker(model_name,HASS_URL, API_KEY,WEBHOOK_ID)

for i in range(20):
    print(upload.update_state(loss = i*0.45, epoch = i, accuracy_val = 74))
    time.sleep(1)