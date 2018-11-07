import unittest

from vk_service.factories.attachment.poll_factory import PollFactory
from vk_service.models.attachment.poll import Poll
from vk_service.models.attachment.answer import Answer
from vk_service.models.attachment.photo import Photo
from vk_service.models.attachment.background import Background


class PollFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = PollFactory()
        self.answer = {'id': 1, 'text': 'Vote1', 'votes': 52, 'rate': 5}
        self.answers = [self.answer.copy(), self.answer.copy()]
        self.size = {
            'src': 'http://example.com/m.jpg', 'width': 130,
            'height': 87, 'type': 'm'
        }
        self.sizes = [self.size.copy(), self.size.copy(), self.size.copy()]
        self.photo = {
            'id': 3, 'album_id': 2, 'owner_id': 53, 'user_id': 53,
            'text': 'D', 'date': 25748559, 'sizes': self.sizes.copy(),
            'width': 153, 'height': 154
        }
        self.point = {'position': 1, 'color': 'FFFFFF'}
        self.points = [self.point.copy(), self.point.copy(), self.point.copy()]
        self.background = {
            'id': 25, 'type': 'gradient', 'angle': 48, 'color': 'FFFFFF',
            'points': self.points.copy()
        }
        self.values = {
            'id': 2, 'owner_id': 53, 'created': 62622626, 'question': 'BeOrNo',
            'votes': 54, 'answers': self.answers.copy(), 'anonymous': True,
            'multiple': False, 'answer_ids': ['1'],
            'end_date': 0, 'closed': False, 'is_board': False,
            'can_edit': False, 'can_vote': True, 'can_report': True,
            'can_share': True, 'author_id': 53, 'photo': self.photo.copy(),
            'background': self.background.copy(),
            'friends': ['25', '52', '54']
        }
        self.submodels = {
            'answers': Answer,
            'photo': Photo,
            'background': Background
        }

    def test_factory_build(self):
        values = self.values.copy()
        poll = self.factory.build(values)
        self.assertIsInstance(poll, Poll)
        for key in self.submodels:
            values[key] = poll.__dict__[key]
        for key in self.submodels:
            if isinstance(poll.__dict__[key], list):
                for item in poll.__dict__[key]:
                    self.assertIsInstance(item, self.submodels[key])
            else:
                self.assertIsInstance(poll.__dict__[key], self.submodels[key])
        self.assertEqual(poll.__dict__, values)


if __name__ == '__main__':
    unittest.main()
