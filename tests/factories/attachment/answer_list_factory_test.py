import unittest

from vk_service.factories.attachment.answer_list_factory import AnswerListFactory
from vk_service.models.attachment.answer import Answer


class AnswerListFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = AnswerListFactory()
        self.answer = {'id': 2, 'text': 'Vote2', 'votes': 52, 'rate': 5}
        self.values = [self.answer.copy(), self.answer.copy()]

    def test_factory_build(self):
        values = self.values.copy()
        answers = self.factory.build(values)
        self.assertIsInstance(answers, list)
        for i, answer in enumerate(answers):
            self.assertIsInstance(answer, Answer)
            self.assertEqual(answer.__dict__, values[i])


if __name__ == '__main__':
    unittest.main()
