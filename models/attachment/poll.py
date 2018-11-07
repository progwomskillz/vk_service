from .attachment import Attachment
from vk_service.factories.attachment.answer_list_factory import AnswerListFactory
from vk_service.factories.attachment.photo_factory import PhotoFactory
from vk_service.factories.attachment.background_factory import BackgroundFactory


class Poll(Attachment):
    def __init__(self, values):
        factories = {
            'answers': AnswerListFactory(),
            'photo': PhotoFactory(),
            'background': BackgroundFactory(),
        }
        super(Poll, self).__init__(values, factories)
