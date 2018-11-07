from .attachment import Attachment
from vk_service.factories.attachment import SectionFactory


class Category(Attachment):
    def __init__(self, values):
        factories = {
            'section': SectionFactory(),
        }
        super(Category, self).__init__(values, factories)
