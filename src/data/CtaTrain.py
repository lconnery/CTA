

class CtaTrain(object):

    def __init__(self, data: dict):
        self.data = data

    @property
    def run_number(self) -> str:
        return self.data['rn']

    @property
    def next_parent_stop_id(self) -> str:
        return self.data['nextStaId']

    @property
    def next_stop_id(self) -> str:
        return self.data['nextStpId']

    @property
    def next_stop_proper_title(self) -> str:
        return self.data['nextStaNm']

    @property
    def direction_of_travel(self) -> int:
        return self.data['heading']
