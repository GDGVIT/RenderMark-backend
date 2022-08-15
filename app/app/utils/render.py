from utils.templates import thefirstone


def render_video(video):
    # print(video)
    template = video["template"]

    if template == "thefirstone":

        return thefirstone.render(video)

    return None
