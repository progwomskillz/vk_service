from vk_service.models.attachment.section import Section


class SectionFactory:
    def build(self, values):
        return Section(values)
