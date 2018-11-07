from vk_service.models.attachment.page import Page


class PageFactory:
    def build(self, values):
        return Page(values)
