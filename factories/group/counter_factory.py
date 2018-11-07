from vk_service.models.group.counter import Counter


class CounterFactory:
    def build(self, values):
        return Counter(values)
