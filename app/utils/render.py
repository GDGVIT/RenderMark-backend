import cv2
import numpy as np
from moviepy.editor import *


def render_video(video):
    print(video)
    template = video.template
    screen_1 = ImageClip(f"assets/template{template}/back1.jpg").set_duration(5)
    img1 = (
        ImageClip(f"assets/template{template}/asset1.png")
        .set_duration(5)
        .set_position("center")
    )
    screen_1 = CompositeVideoClip([screen_1, img1])

    screen_2 = ImageClip(f"assets/template{template}/back2.jpg").set_duration(5)
    img1 = (
        ImageClip(f"assets/template{template}/asset2.png")
        .set_duration(5)
        .set_position(("center", 0.45), relative=True)
        .resize(2)
    )
    text1 = (
        TextClip("We're App Only", fontsize=90, color="white")
        .set_duration(5)
        .set_position(("center", 0.2), relative=True)
    )
    text2 = (
        TextClip(
            "The ______ app is now available as an app",
            fontsize=40,
            font="Calibri light",
            color="white",
        )
        .set_duration(5)
        .set_position(("center", 0.35), relative=True)
    )
    screen_2 = CompositeVideoClip([screen_2, img1, text1, text2])

    # img_path = f"assets/template{template}/asset3.png"
    # img1 = ImageClip(f"assets/template{template}/asset3.png")
    # W, H = img1.w, img1.h
    # AR = 1.0 * W / H
    # camera = Camera("location", [-1, 0, -1], "look_at", [0, 0, 0])
    # light = LightSource([-1, 0, -1])
    # bg = Background("colour", [0, 0, 0, 1])
    # s = Scene(camera=camera, objects=[light, bg])
    # s = s.add_objects(
    #     [
    #         Box(
    #             [0, 0, 0],
    #             [W, H, 0],
    #             Texture(
    #                 Pigment(ImageMap('"{}"'.format(img_path), "once")),
    #                 Finish("ambient", 1.0),
    #             ),
    #             "translate",
    #             [-0.5, -0.5, 0],
    #             "scale",
    #             [AR, 1, 0],
    #         )
    #     ]
    # )
    # s.render("./temp.png")

    img1 = (
        ImageClip(f"assets/template{template}/asset3.png")
        .set_duration(5)
        .set_position((0.1, "center"), relative=True)
        .resize(0.55)
    )
    text1 = (
        TextClip(
            "Lorem ipsum dolor sit amet, consectetur adipiscing \nelit. Aliquam ultrices",
            fontsize=60,
            color="white",
            align="center",
        )
        .set_duration(5)
        .set_position((0.4, 0.6), relative=True)
    )
    text2 = (
        TextClip(
            "All new version",
            fontsize=40,
            bg_color="green",
            color="white",
            align="center",
        )
        .set_duration(5)
        .set_position((0.32, 0.3), relative=True)
    )
    cur_x = 0.4 * 1920
    cur_y = 0.6 * 1080 + 65
    image_width = text1.w
    screen_3 = cv2.imread(f"assets/template{template}/back2.jpg")
    cv2.line(
        screen_3,
        (int(cur_x), int(cur_y)),
        (int(cur_x + image_width), int(cur_y)),
        (250, 250, 250),
    )
    screen_3 = ImageClip(cv2.cvtColor(screen_3, cv2.COLOR_RGB2BGR)).set_duration(5)
    screen_3 = CompositeVideoClip([screen_3, img1, text1, text2])

    img1 = (
        ImageClip(f"assets/template{template}/asset3.png")
        .set_duration(5)
        .set_position((0.7, "center"), relative=True)
        .resize(0.55)
    )
    text1 = (
        TextClip(
            "Lorem ipsum dolor sit amet, consectetur \nadipiscing elit. Aliquam ultrices",
            fontsize=60,
            color="white",
            align="west",
        )
        .set_duration(5)
        .set_position((0.05, 0.2), relative=True)
    )
    text2 = (
        TextClip(
            "All new version",
            fontsize=40,
            bg_color="green",
            color="white",
            align="center",
        )
        .set_duration(5)
        .set_position((0.55, 0.7), relative=True)
    )
    cur_x = 0.05 * 1920
    cur_y = 0.2 * 1080 + 65
    image_width = text1.w
    screen_4 = cv2.imread(f"assets/template{template}/back2.jpg")
    cv2.line(
        screen_4,
        (int(cur_x), int(cur_y)),
        (int(cur_x + image_width), int(cur_y)),
        (250, 250, 250),
    )
    screen_4 = ImageClip(cv2.cvtColor(screen_4, cv2.COLOR_RGB2BGR)).set_duration(5)
    screen_4 = CompositeVideoClip([screen_4, img1, text1, text2])
    # screen_4.preview(fps=24)

    video = concatenate([screen_1, screen_2, screen_3, screen_4], method="compose")
    video.write_videofile("media/video.mp4", fps=24)

    return "media/video.mp4"
