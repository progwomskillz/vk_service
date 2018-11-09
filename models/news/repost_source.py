from abc import ABC
from vk_service.models.common.common import Common
from vk_service.factories.profile.profile_factory import ProfileFactory
from vk_service.factories.group.group_factory import GroupFactory


class RepostSource(Common, ABC):
    def __init__(self, post, profiles, groups, factories={}):
        super(RepostSource, self).__init__(post, factories)
        self.owner = self._get_owner(profiles, groups)

    def _get_owner(self, profiles, groups):
        if self.owner_id > 0:
            factory = ProfileFactory()
            profile = self._find_profile(profiles)
            return factory.build(profile)
        factory = GroupFactory()
        group = self._find_group(groups)
        return factory.build(group)

    def _find_profile(self, profiles):
        for profile in profiles:
            if profile['id'] == self.owner_id:
                return profile

    def _find_group(self, groups):
        for group in groups:
            if group['id'] == abs(self.owner_id):
                return group
