import requests

r = requests.post(
    "http://127.0.0.1:8000/api/v1/render",
    json={
        "template": "thefirstone",
        "title": "Gmeet Stickers",
        "scenes": [
            {
                "image": "https://i.imgur.com/vCgTihs.jpg",
            },
            {
                "image": "https://previews.123rf.com/images/varijanta/varijanta1701/varijanta1"
                + "70100028/70057980-set-of-flat-design-social-network-stickers-isolated-vector-i"
                + "llustrations-for-online-communication-ne.jpg",
                "text": "Stickers in Gmeet!",
                "subtext": "Express yourself with your favourite stickers",
            },
            {
                "image": "https://i.insider.com/5f6a2bb5323fc4001e0d7c7c?width=750&format=jpeg",
                "text": "Insert stickers with a click of a button!",
            },
            {
                "image": "https://cdn.nerdschalk.com/wp-content/uploads/2018/10/Pokemon-WAStickers.jpg",
                "text": "Use your own stickers!",
                "subtext": "The pokemon sticker pack is available for free",
            },
            {
                "text": "Check it out now!",
                "subtext": "stick-it-out.com",
            },
        ],
    },
)

print(r.json())
