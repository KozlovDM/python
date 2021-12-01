import wolframalpha

from python.project.utils import wolfram_alpha_api, bot


def solve(message):
    client = wolframalpha.Client(wolfram_alpha_api)
    res = client.query(message.text)
    print(res)
    for pod in res.pod:
        if type(pod.subpod) == list:
            for subpod in pod.subpod:
                bot.send_photo(message.from_user.id, subpod.img.src)
        else:
            bot.send_photo(message.from_user.id, pod.subpod.img.src)
