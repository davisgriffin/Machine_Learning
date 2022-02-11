import json

with open("../Datasets/beer_ratings.json", "r") as f:
    review = json.loads(f.read())
    print(review[0]['beer/name'])