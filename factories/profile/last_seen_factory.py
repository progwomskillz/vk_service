from vk_service.models.profile.last_seen import LastSeen


class LastSeenFactory:
    def build(self, values):
        return LastSeen(values)
