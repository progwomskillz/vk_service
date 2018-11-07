from vk_service.models.profile.counter import Counter


class CounterFactory:
    def build(self, values):
        return Counter(values)
