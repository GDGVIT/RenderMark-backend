import requests

r = requests.post(
    "http://127.0.0.1:8000/api/v1/render",
    json={
        "template": 1,
        "title": "A Promo Video",
        "scenes": [
            {
                "image": "shorturl.at/bgor9",
                "text": "This is the first scene",
                "subtext": "This is the first scene's subtext",
            },
            {
                "image": "shorturl.at/bJRV8",
                "text": "This is the second scene",
                "subtext": "This is the second scene's subtext",
            },
            {
                "image": "shorturl.at/bJRV8",
                "text": "This is the third scene",
                "subtext": "This is the third scene's subtext",
            },
            {
                "image": "shorturl.at/bJRV8",
                "text": "This is the fourth scene",
                "subtext": "This is the fourth scene's subtext",
            },
        ],
    },
)

print(r.json())
