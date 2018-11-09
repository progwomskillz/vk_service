import unittest

from vk_service.factories.news.post_list_factory import PostListFactory
from vk_service.models.news.text_post import TextPost
from vk_service.models.news.wall_photo_post import WallPhotoPost
from vk_service.models.news.friend_post import FriendPost
from vk_service.models.news.video_post import VideoPost


class PostListFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = PostListFactory()
        self.size_1 = {
            'type': 'm',
            'url': 'https://sun1-1.us...9f7/qecntpIbLJo.jpg',
            'width': 130, 'height': 84
        }
        self.sizes_1 = [self.size_1.copy(), self.size_1.copy()]
        self.photo_1 = {
            'id': 456239033, 'album_id': -7,
            'owner_id': -166813214, 'user_id': 100,
            'sizes': self.sizes_1.copy(),
            'text': '', 'date': 1541765319,
            'post_id': 72, 'access_key': '63a87072b33379dc28'
        }
        self.attachment_1 = {'type': 'photo', 'photo': self.photo_1.copy()}
        self.attachments_1 = [self.attachment_1.copy()]
        self.post_source_1 = {'type': 'vk'}
        self.comments_1 = {
            'count': 0, 'can_post': 1,
            'groups_can_post': True
        }
        self.likes_1 = {
            'count': 1, 'user_likes': 0,
            'can_like': 1, 'can_publish': 1
        }
        self.reposts_1 = {'count': 0, 'user_reposted': 0}
        self.views_1 = {'count': 12}
        self.item_1 = {
            'type': 'post','source_id': -166813214,'date': 1541765319,
            'post_id': 72,'post_type': 'post', 'text': 'None',
            'marked_as_ads': 0, 'attachments': self.attachments_1.copy(),
            'post_source': self.post_source_1.copy(),
            'comments': self.comments_1.copy(), 'likes': self.likes_1.copy(),
            'reposts': self.reposts_1.copy(), 'views': self.views_1.copy()
        }
        self.size_2 = {
            'type': 'm',
            'url': 'https://pp.userap...9f7/qecntpIbLJo.jpg',
            'width': 130, 'height': 84
        }
        self.sizes_2 = [self.size_2.copy(), self.size_2.copy()]
        self.likes_2 = {'user_likes': 0, 'count': 2}
        self.reposts_2 = {'count': 0, 'user_reposted': 0}
        self.comments_2 = {'count': 0}
        self.photo_2 = {
            'id': 456239033, 'album_id': -7, 'owner_id': -166813214,
            'user_id': 100, 'sizes': self.sizes_2.copy(), 'text': 'None',
            'date': 1541765319, 'post_id': 72, 'access_key': '63a87072b33379dc28',
            'likes': self.likes_2.copy(), 'reposts': self.reposts_2.copy(),
            'comments': self.comments_2.copy(), 'can_comment': 1, 'can_repost': 1
        }
        self.photos_2 = [self.photo_2.copy()]
        self.photo_list_meta_data_2 = {
            'count': 1, 'items': self.photos_2.copy()
        }
        self.item_2 = {
            'type': 'wall_photo', 'source_id': -166813214,
            'date': 1541765319, 'post_id': 1541710800,
            'photos': self.photo_list_meta_data_2.copy()
        }
        self.friend_3 = {'user_id': 257473557}
        self.friends_3 = [self.friend_3.copy()]
        self.friend_list_meta_data_3 = {'count': 1, 'items': self.friends_3.copy()}
        self.item_3 = {
            'type': 'friend', 'source_id': 90330786, 'date': 1541696914,
            'friends': self.friend_list_meta_data_3.copy()
        }
        self.likes_4 = {'user_likes': 0, 'count': 5}
        self.reposts_4 = {'count': 5, 'user_reposted': 0}
        self.video_4 = {
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
            'likes': self.likes_4.copy(), 'reposts': self.reposts_4.copy()
        }
        self.videos_4 = [self.video_4.copy()]
        self.video_list_meta_data_4 = {'count': 1, 'items': self.videos_4.copy()}
        self.item_4 = {
            'type': 'video', 'source_id': -30666517,
            'date': 1541688854, 'video': self.video_list_meta_data_4.copy()
        }
        self.items = [self.item_1.copy(), self.item_2.copy(), self.item_3.copy(), self.item_4.copy()]
        self.profile_1 = {
            'id': 90330786, 'first_name': 'Михаил', 'last_name': 'Давиденко',
            'sex': 2, 'screen_name': 'id90330786',
            'photo_50': 'https://pp.userap...26rclnWFI.jpg?ava=1',
            'photo_100': 'https://pp.userap...tdmKR5BsA.jpg?ava=1',
            'online': 0
        }
        self.profiles = [self.profile_1.copy()]
        self.group_1 = {
            'id': 166813214, 'name': 'Storytelling Software',
            'screen_name': 'storytellingsoftware', 'is_closed': 0,
            'type': 'group', 'is_admin': 0, 'is_member': 1,
            'photo_50': 'https://pp.userap...P6q2CLE8Q.jpg?ava=1',
            'photo_100': 'https://pp.userap...Q5spwOtsY.jpg?ava=1',
            'photo_200': 'https://pp.userap...ZLLOrYGm0.jpg?ava=1'
        }
        self.group_2 = {
            'id': 30666517, 'name': 'Типичный программист',
            'screen_name': 'tproger', 'is_closed': 0,
            'type': 'page', 'is_admin': 0, 'is_member': 1,
            'photo_50': 'https://pp.userap...KNrvjYkdo.jpg?ava=1',
            'photo_100': 'https://pp.userap...JJG4iknq0.jpg?ava=1',
            'photo_200': 'https://pp.userap...eV7nJitGY.jpg?ava=1'
        }
        self.groups = [self.group_1.copy(), self.group_2.copy()]
        self.values = {
            'items': self.items.copy(),
            'profiles': self.profiles.copy(),
            'groups': self.groups.copy()
        }
        self.submodels = {
            'post': TextPost,
            'wall_photo': WallPhotoPost,
            'friend': FriendPost,
            'video': VideoPost
        }

    def test_factory_build(self):
        values = self.values.copy()
        posts = self.factory.build(values)
        self.assertIsInstance(posts, list)
        for post in posts:
            self.assertIsInstance(post, self.submodels[post.type])


if __name__ == '__main__':
    unittest.main()
