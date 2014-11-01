from settings import *
import twitter


def tweet(message):
    api.PostUpdate(message)
