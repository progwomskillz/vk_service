from social_network import SocialNetworkBase
from vk_service.factories.news.post_list_factory import PostListFactory
from vk_service.factories.profile.profile_list_factory import ProfileListFactory


class VKService(SocialNetworkBase):

    API_VERSION = 5.87

    # Writing variables to an object during initialization.
    #
    # Params:
    #   access_token -
    #       This is a personal token for VK authentication and
    #       for using the VK API methods.
    #   user_id -
    #       This is the user ID for this access token.
    def __init__(self, access_token=None, user_id=None):
        self.access_token = access_token
        self.user_id = user_id

    # Creating a session in VK with a given access_token and connecting
    # to the API
    def authenticate(self):
        self.session = vk.Session(access_token=self.access_token)
        self.API = vk.API(self.session)

    # Get the response from the VK method newsfeed.get and return list
    # from the received dict with key 'items'
    #
    # Params:
    #   params -
    #       Dict with the params (https://vk.com/dev/newsfeed.get)
    def get_feed_online(self, params):
        # newsfeed -
        #   This dictionary is the response from VK with keys: items,
        #   profiles, groups, new_offset and next_from
        #   (https://vk.com/dev/newsfeed.get)
        return self.API.newsfeed.get(v=self.API_VERSION, **params)

    # Get the response from the get_feed_online method and return list of
    # News object(s)
    #
    # Params: same as get_feed_online method
    def get_feed(self, params={'filters': 'post'}):
        factory = PostListFactory()
        result = factory.build(self.get_feed_online(params))
        return result

    # Get the response from the VK method wall.post and return dict response
    #
    # Params:
    #   params -
    #       Dict with the params (https://vk.com/dev/wall.post)
    def create_post_online(self, params):
        return self.API.wall.post(v=self.API_VERSION, **params)

    # Get the response from the create_post_online method and return
    # True if message was posted or False if message wasnt posted
    #
    # Params: same as create_post_online method
    def create_post(self, params={'message': 'Test message'}):
        # Writing the response from the create_post_online method to the
        # post variable
        post = self.create_post_online(params)
        # Check for the errors in the response
        if 'error_code' in post:
            return False
        return True

    # Get the response from the VK method users.get and return list that
    # contains dicts with User object fields
    #
    # Params:
    #   params -
    #       Dict with the params (https://vk.com/dev/users.get)
    def get_profiles_online(self, params):
        return self.API.users.get(v=self.API_VERSION, **params)

    # Get the response from the create_post_online method and return list of
    # User object(s)
    #
    # Params: same as get_users_online method
    def get_profiles(self, params):
        factory = ProfileListFactory()
        result = factory.build(self.get_users_online(params))
        return result

    # Get the response from the VK method likes.add and return dict response
    #
    # Params:
    #   params -
    #       Dict with the params (https://vk.com/dev/likes.add)
    def like_add_online(self, params):
        return self.API.likes.add(v=self.API_VERSION, **params)

    # Get the response from the like_add_online method and return
    # True if like was added or False if isnt
    #
    # Params: same as like_add_online method
    def like_add(self, params):
        # like - dict that contains key 'error_code' if was error
        # during request or 'likes' (count of likes on object) if
        # request if successfull
        like = self.like_add_online(params)
        if 'error_code' in like:
            return False
        return True

    # Get the response from the VK method likes.delete and return dict response
    #
    # Params:
    #   params -
    #       Dict with the params (https://vk.com/dev/likes.delete)
    def like_delete_online(self, params):
        return self.API.likes.delete(v=self.API_VERSION, **params)

    # Get the response from the like_delete_online method and return
    # True if like was deleted or False if isnt
    #
    # Params: same as like_delete_online method
    def like_delete(self, params):
        # like - dict that contains key 'error_code' if was error
        # during request or 'likes' (count of likes on object) if
        # request if successfull
        like = self.like_delete_online(params)
        if 'error_code' in like:
            return False
        return True
