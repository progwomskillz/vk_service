import unittest

from vk_service.factories.group.contact_list_factory import ContactListFactory
from vk_service.models.group.contact import Contact


class ContactListFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = ContactListFactory()
        self.contact = {
            'user_id': 53, 'desc': 'Editor', 'phone': '000',
            'email': 'Editor@example.com'
        }
        self.values = [self.contact.copy(), self.contact.copy()]

    def test_factory_build(self):
        values = self.values.copy()
        contacts = self.factory.build(values)
        self.assertIsInstance(contacts, list)
        for i, contact in enumerate(contacts):
            self.assertIsInstance(contact, Contact)
            self.assertEqual(contact.__dict__, values[i])


if __name__ == '__main__':
    unittest.main()
