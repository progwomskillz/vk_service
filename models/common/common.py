class Common:
    def __init__(self, values, factories={}):
        for key in values:
            if key in factories:
                factory = factories[key]
                result_value = factory.build(values[key])
            else:
                result_value = values[key]
            setattr(self, key, result_value)
