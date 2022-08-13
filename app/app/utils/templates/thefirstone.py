from uuid import uuid4

import cv2
import psutil
from moviepy.editor import CompositeVideoClip, ImageClip, TextClip, concatenate


def render(video):
    template = video["template"]

    screensize = (1080, 1920)

    screen_1 = ImageClip(f"assets/{template}/back1.jpg").set_duration(5)
    img1 = ImageClip(video["scenes"][0]["image"])
    img1 = img1.resize(300 / img1.w if 300 / img1.w > 300 / img1.h else 300 / img1.h)
    img1 = img1.set_duration(5).set_position("center")
    screen_1 = CompositeVideoClip([screen_1, img1])

    screen_2 = ImageClip(f"assets/{template}/back2.jpg").set_duration(5)
    img1 = (
        ImageClip(video["scenes"][1]["image"])
        .set_duration(5)
        .set_position(("center", 0.45), relative=True)
    )
    img1 = img1.resize(500 / img1.w if 500 / img1.w > 500 / img1.h else 500 / img1.h)

    text1 = (
        TextClip(
            video["scenes"][1]["text"],
            fontsize=90,
            color="white",
            font="Calibri",
        )
        .set_duration(5)
        .set_position(("center", 0.2), relative=True)
    )
    text2 = (
        TextClip(
            video["scenes"][1]["subtext"],
            fontsize=40,
            font="Calibri",
            color="white",
        )
        .set_duration(5)
        .set_position(("center", 0.35), relative=True)
    )
    screen_2 = CompositeVideoClip([screen_2, img1, text1, text2])

    screen_3 = cv2.imread(f"assets/{template}/back2.jpg")
    img1 = (
        ImageClip(video["scenes"][2]["image"])
        .set_duration(5)
        .set_position((0.15, "center"), relative=True)
    )
    print(img1.w, img1.h)
    img1 = img1.resize((450 / img1.w) if 450 / img1.w > 900 / img1.h else 900 / img1.h)
    text1 = (
        TextClip(
            video["scenes"][2]["text"],
            fontsize=50,
            color="white",
            align="center",
        )
        .set_duration(5)
        .set_position((0.43, 0.6), relative=True)
    )
    text1 = text1.resize((950 / text1.w))
    cur_x = 0.43 * 1920
    cur_y = 0.6 * 1080 + text1.h + 5
    text_width = text1.w
    cv2.line(
        screen_3,
        (int(cur_x), int(cur_y)),
        (int(cur_x + text_width), int(cur_y)),
        (250, 250, 250),
        thickness=2,
    )
    screen_3 = ImageClip(cv2.cvtColor(screen_3, cv2.COLOR_RGB2BGR)).set_duration(5)
    screen_3 = CompositeVideoClip([screen_3, img1, text1])

    screen_4 = cv2.imread(f"assets/{template}/back2.jpg")
    img1 = (
        ImageClip(video["scenes"][3]["image"])
        .set_duration(5)
        .set_position((0.5, "center"), relative=True)
    )
    img1 = img1.resize((600 / img1.w) if 600 / img1.w > 700 / img1.h else 700 / img1.h)
    text1 = (
        TextClip(
            video["scenes"][3]["text"],
            fontsize=60,
            color="white",
            align="west",
        )
        .set_duration(5)
        .set_position((0.1, 0.25), relative=True)
    )
    text1 = text1.resize((700 / text1.w))
    text2 = (
        TextClip(
            video["scenes"][3]["subtext"],
            fontsize=50,
            color="white",
            align="center",
        )
        .set_duration(5)
        .set_position((0.15, 0.7), relative=True)
    )
    text2 = text2.resize((640 / text2.w))
    cur_x = 0.1 * 1920
    cur_y = 0.25 * 1080 + text1.h + 5
    image_width = text1.w
    cv2.line(
        screen_4,
        (int(cur_x), int(cur_y)),
        (int(cur_x + image_width), int(cur_y)),
        (250, 250, 250),
        thickness=2,
    )
    screen_4 = ImageClip(cv2.cvtColor(screen_4, cv2.COLOR_RGB2BGR)).set_duration(5)
    screen_4 = CompositeVideoClip([screen_4, img1, text1, text2])

    screen_5 = ImageClip(f"assets/{template}/back2.jpg").set_duration(5)
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
    uuid = str(uuid4())
    final.write_videofile(
        f"media/{uuid}.mp4", fps=24, logger=None
    )  # , threads=(psutil.cpu_count()))

    return f"{uuid}.mp4"
