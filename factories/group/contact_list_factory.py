from vk_service.models.group.contact import Contact


class ContactListFactory:
    def build(self, values):
        return [Contact(value) for value in values]
