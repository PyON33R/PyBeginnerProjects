from requests import get

params = {
    "amount": 10,
    "category": 18,
    "difficulty": "easy",
    "type": "boolean",
}

data = get("https://opentdb.com/api.php", params=params)
question_data = data.json()["results"]
