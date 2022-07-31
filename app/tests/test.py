import requests

r = requests.post(
    "http://127.0.0.1:8000/api/v1/render",
    json={
        "template": 1,
        "title": "A Promo Video",
        "scenes": [
            {
                "image": "https://image.shutterstock.com/image-vector/lorem-ipsum-logo-design-consept-260nw-1456986776.jpg",
                "text": "This is the first scene",
                "subtext": "This is the first scene's subtext",
            },
            {
                "image": "https://www.kindpng.com/picc/m/8-85396_mobile-png-clipart-transparent-android-mobile-png-png.png",
                "text": "This is the second scene",
                "subtext": "This is the second scene's subtext",
            },
            {
                "image": "https://www.kindpng.com/picc/m/8-85396_mobile-png-clipart-transparent-android-mobile-png-png.png",
                "text": "This is the third scene",
                "subtext": "This is the third scene's subtext",
            },
            {
                "image": "https://www.kindpng.com/picc/m/8-85396_mobile-png-clipart-transparent-android-mobile-png-png.png",
                "text": "This is the fourth scene",
                "subtext": "This is the fourth scene's subtext",
            },
        ],
    },
)

with open(r"video.mp4", "wb") as f:
    f.write(r.content)
