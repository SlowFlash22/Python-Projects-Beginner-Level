import os
from datetime import datetime
from dotenv import load_dotenv
import requests

load_dotenv()

# ###BREAKING DOWN OF NATURAL LANGUAGE INTO USABLE DATA USING NUTRITIONX API###################
app_id = os.getenv("APP_ID")
app_key = os.getenv("APP_KEY")

headers = {
    "x-app-id": app_id,
    "x-app-key": app_key
}

GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 175
AGE = 23


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()

#####
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheet_endpoint = "https://api.sheety.co/6137092d39b13d59a4032e11b57934cf/myWorkouts/workouts"
auther = {
    "Authorization": os.environ.get("Bearer")
}
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=auther)

    print(sheet_response.text)