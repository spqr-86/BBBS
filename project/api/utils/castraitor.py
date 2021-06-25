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
        all_model_records = self.model.objects.all()
        if len(all_model_records) < self.n:
            return all_model_records
        return self.model.objects.all().order_by(self.order_field)[:self.n]
