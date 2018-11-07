from .attachment import Attachment
from vk_service.factories.attachment import (
    AnswerListFactory, PhotoFactory, BackgroundFactory
)


class Poll(Attachment):
    def __init__(self, values):
        factories = {
            'answers': AnswerListFactory(),
            'photo': PhotoFactory(),
            'background': BackgroundFactory(),
        }
        super(Poll, self).__init__(values, factories)
