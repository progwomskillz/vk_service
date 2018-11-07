from .attachment import Attachment
from vk_service.factories.attachment import PreviewFactory


class Doc(Attachment):
    def __init__(self, values):
        factories = {
            'preview': PreviewFactory(),
        }
        super(Doc, self).__init__(values, factories)
