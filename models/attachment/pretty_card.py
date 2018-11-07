from .attachment import Attachment
from vk_service.factories.attachment import CardListFactory


class PrettyCard(Attachment):
    def __init__(self, values):
        factories = {
            'cards': CardListFactory()
        }
        super(PrettyCard, self).__init__(values, factories)
