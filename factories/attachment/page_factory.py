from vk_service.models.attachment import Page


class PageFactory:
    def build(self, values):
        return Page(values)
