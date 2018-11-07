from vk_service.models.attachment import Answer


class AnswerListFactory:
    def build(self, values):
        return [Answer(value) for value in values]
