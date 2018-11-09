import unittest

from vk_service.factories.news.video_post_factory import VideoPostFactory
from vk_service.models.news.video_post import VideoPost
from vk_service.models.news.video_list_meta_data import VideoListMetaData
from vk_service.models.profile.profile import Profile
from vk_service.models.group.group import Group


class VideoPostFactoryTEst(unittest.TestCase):
    def setUp(self):
        self.factory = VideoPostFactory()
        self.like = {'user_likes': 0, 'count': 5}
        self.repost = {'count': 5, 'user_reposted': 0}
        self.video = {
            'id': 456242504, 'owner_id': -30666517, 'title': 'Highload++',
            'duration': 0, 'description': 'Ссылка: https://tprg.ru/x3iB',
            'date': 1541750162, 'comments': 140, 'views': 81050,
            'width': 1280,  'height': 720,
            'photo_130': 'https://pp.userap...a39/hSJ7265fPik.jpg',
            'photo_320': 'https://pp.userap...a37/erWB1hglgrs.jpg',
            'photo_800': 'https://pp.userap...a35/PCiEykYG7_Y.jpg',
            'photo_1280': 'https://pp.userap...a36/S-2i3rzvcps.jpg',
            'access_key': '6627f0cc8fab088de5',
            'live': 1, 'spectators': 523,
            'first_frame_800': 'https://pp.userap...2b3/J0vvDsbM_pY.jpg',
            'first_frame_320': 'https://pp.userap...2b4/Cgga3761OLM.jpg',
            'first_frame_160': 'https://pp.userap...2b5/V1siEEwv2xo.jpg',
            'first_frame_130': 'https://pp.userap...2b6/P5QNkFK4jTI.jpg',
            'can_add': 1, 'can_comment': 1, 'can_repost': 1,
            'likes': self.like.copy(), 'reposts': self.repost.copy()
        }
        self.video_list = [self.video.copy()]
        self.videos = {'count': 1, 'items': self.video_list.copy()}
        self.values = {
            'type': 'video', 'source_id': -30666517,
            'date': 1541688854, 'video': self.videos.copy()
        }
        self.submodels = {
            'video': VideoListMetaData
        }
        self.profiles = []
        self.groups = [
            {
                'id': 72495085, 'name': '/dev/null',
                'screen_name': 'tnull', 'is_closed': 0,
                'type': 'page', 'is_admin': 0, 'is_member': 1,
                'photo_50': 'https://sun1-6.us...-h6o_8VS8.jpg?ava=1',
                'photo_100': 'https://sun1-5.us...PTdjZrLgo.jpg?ava=1',
                'photo_200': 'https://sun1-20.u...EBzYm5fAU.jpg?ava=1'
            }, {
                'id': 30666517, 'name': 'Типичный программист',
                'screen_name': 'tproger', 'is_closed': 0,
                'type': 'page', 'is_admin': 0, 'is_member': 1,
                'photo_50': 'https://pp.userap...KNrvjYkdo.jpg?ava=1',
                'photo_100': 'https://pp.userap...JJG4iknq0.jpg?ava=1',
                'photo_200': 'https://pp.userap...eV7nJitGY.jpg?ava=1'
            }
        ]

    def test_factory_build(self):
        values = self.values.copy()
        profiles = self.profiles.copy()
        groups = self.groups.copy()
        video_post = self.factory.build(values, profiles, groups)
        self.assertIsInstance(video_post, VideoPost)
        for key in self.submodels:
            values[key] = video_post.__dict__[key]
        for key in self.submodels:
            self.assertIsInstance(video_post.__dict__[key], self.submodels[key])
        if values['source_id'] > 0:
            self.assertIsInstance(video_post.owner, Profile)
        else:
            self.assertIsInstance(video_post.owner, Group)
        values['owner'] = video_post.owner
        self.assertEqual(video_post.__dict__, values)


if __name__ == '__main__':
    unittest.main()
