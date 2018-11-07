from vk_service.models.attachment import Section


class SectionFactory:
    def build(self, values):
        return Section(values)
