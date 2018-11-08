from vk_service.models.news.view import View


class ViewFactory:
    def build(self, values):
        return View(values)
