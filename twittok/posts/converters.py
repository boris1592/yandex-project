class PkConverter:
    regex = '[1-9]\\d*'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)


class RatingConverter:
    regex = '-1|0|1'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)
