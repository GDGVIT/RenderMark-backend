from uuid import uuid4

from moviepy.editor import (
    AudioFileClip,
    CompositeVideoClip,
    ImageClip,
    TextClip,
    concatenate,
)


def render(video):
    template = video["template"]

    screen_1 = ImageClip(f"assets/{template}/back1.jpg").set_duration(5)
    text1 = (
        TextClip(
            video["scenes"][0]["text"],
            fontsize=90,
            color="white",
            font="Calibri",
        )
        .set_duration(5)
        .set_position(("center", 0.4), relative=True)
    )
    text2 = (
        TextClip(
            video["scenes"][0]["subtext"],
            fontsize=40,
            font="Calibri",
            color="white",
        )
        .set_duration(5)
        .set_position(("center", 0.52), relative=True)
    )
    screen_1 = CompositeVideoClip([screen_1, text1, text2])

    screen_2 = ImageClip(f"assets/{template}/back1.jpg").set_duration(5)
    img1 = (
        ImageClip(video["scenes"][1]["image"])
        .set_duration(5)
        .set_position((0.5, "center"), relative=True)
    )
    img1 = img1.resize(width=800)

    text1 = (
        TextClip(
            video["scenes"][1]["text"],
            fontsize=50,
            color="white",
            font="Calibri",
        )
        .set_duration(5)
        .set_position((0.1, 0.1), relative=True)
    )
    text2 = (
        TextClip(
            video["scenes"][1]["subtext"],
            size=(600, 500),
            fontsize=30,
            font="Calibri",
            color="gray",
            method="caption",
            align="west",
        )
        .set_duration(5)
        .set_position((0.1, 0.5), relative=True)
    )
    screen_2 = CompositeVideoClip([screen_2, img1, text1, text2])

    screen_3 = ImageClip(f"assets/{template}/back1.jpg").set_duration(5)
    img1 = (
        ImageClip(video["scenes"][2]["image"])
        .set_duration(5)
        .set_position(("center", 0.05), relative=True)
    )
    img1 = img1.resize(height=540)
    text1 = (
        TextClip(
            video["scenes"][2]["text"],
            fontsize=60,
            color="white",
            font="Calibri",
            method="caption",
            align="west",
            size=(540, 400),
        )
        .set_duration(5)
        .set_position((0.1, 0.5), relative=True)
    )
    text2 = (
        TextClip(
            video["scenes"][2]["subtext"],
            size=(800, 400),
            fontsize=30,
            font="Calibri",
            color="gray",
            method="caption",
            align="west",
        )
        .set_duration(5)
        .set_position((0.5, 0.5), relative=True)
    )
    screen_3 = CompositeVideoClip([screen_3, img1, text1, text2])

    screen_4 = ImageClip(f"assets/{template}/back1.jpg").set_duration(5)
    img1 = (
        ImageClip(video["scenes"][3]["image"])
        .set_duration(5)
        .set_position((0, "center"), relative=True)
    )
    img1 = img1.resize(width=960)
    text1 = (
        TextClip(
            video["scenes"][3]["text"],
            fontsize=50,
            color="white",
            align="west",
        )
        .set_duration(5)
        .set_position((0.53, 0.15), relative=True)
    )
    text1 = text1.resize(width=700)
    text2 = (
        TextClip(
            video["scenes"][3]["subtext"],
            size=(700, 500),
            fontsize=30,
            font="Calibri",
            color="gray",
            method="caption",
            align="west",
        )
        .set_duration(5)
        .set_position((0.53, 0.3), relative=True)
    )
    screen_4 = CompositeVideoClip([screen_4, img1, text1, text2])

    screen_5 = ImageClip(f"assets/{template}/back1.jpg").set_duration(5)
    text1 = (
        TextClip(
            video["scenes"][4]["text"],
            fontsize=50,
            color="white",
            font="Calibri",
        )
        .set_duration(5)
        .set_position(("center", 0.3), relative=True)
    )
    text2 = (
        TextClip(
            video["scenes"][4]["subtext"],
            fontsize=70,
            font="Calibri",
            color="white",
        )
        .set_duration(5)
        .set_position(("center", 0.45), relative=True)
    )
    screen_5 = CompositeVideoClip([screen_5, text1, text2])

    final = concatenate([screen_1, screen_2, screen_3, screen_4, screen_5])
    audioclip = AudioFileClip("assets/dark/audio.mp3")
    final = final.set_audio(audioclip)

    uuid = str(uuid4())
    final.write_videofile(
        f"media/{uuid}.mp4", fps=24, logger=None
    )  # , threads=(psutil.cpu_count()))

    return f"{uuid}.mp4"
