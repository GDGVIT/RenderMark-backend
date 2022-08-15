from utils.video_templates import dark, thefirstone


def render_video(video):
    # print(video)
    template = video["template"]

    if template == "thefirstone":
        return thefirstone.render(video)
    elif template == "dark":
        return dark.render(video)
    return None
