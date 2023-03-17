from datetime import datetime


class IndexWrapper:

    def __init__(self, start_date=None):
        if start_date is None:
            self.start_date = datetime.today()

    def get(self):
        return self.start_date
