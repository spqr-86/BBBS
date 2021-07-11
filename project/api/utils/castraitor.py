from django.db.models import QuerySet
from django.db import models

from ..exceptions import InvalidCountException


class Castraitor:
    def __init__(self, model: models.Model, n: int, order_field: str):
        self.model = model
        self.n = n
        self.order_field = order_field
        self.check_n()

    def check_n(self):
        if self.n <= 0:
            raise InvalidCountException(self.model)
        return self.n

    def get_n_records(self) -> QuerySet:
        model_records = self.model.objects.filter(output_to_main=True)
        if len(model_records) < self.n:
            return model_records.order_by(self.order_field)
        return model_records.order_by(self.order_field)[:self.n]
