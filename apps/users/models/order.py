from django.contrib.auth import get_user_model
from django.db.models import (Model, CharField, ManyToManyField, ForeignKey, IntegerField, CASCADE, DO_NOTHING,
                              TextChoices, Choices, BooleanField, TimeField)
from django.conf import settings
from apps.admins.models import Branches
from apps.product.models import Product

from . import Address
from .basket import Basket

User = get_user_model()


class Order(Model):
    class DeliveryType(TextChoices):
        Delivery = '1', "Delivery"
        TakeAway = '2', "Take away"

    # class IsCall(Choices):
    #     YES = 1, "Yes"
    #     NO = 0, "No"

    class PaymentType(TextChoices):
        CASH = '1', "Cash"
        PAYME = '2', "Payme"
        CLICK = '3', "Click"

    user = ForeignKey(User, CASCADE)
    address = ForeignKey(Address, CASCADE, null=True, blank=True)
    branch = ForeignKey(Branches, DO_NOTHING, null=True, blank=True)
    basket = ManyToManyField(Basket)
    delivery_type = CharField(choices=DeliveryType.choices, max_length=1)
    is_call = BooleanField(default=True)
    deliver_now = BooleanField(default=True)
    delivery_time = TimeField(null=True, blank=True)
    payment_type = CharField(choices=PaymentType.choices, max_length=1)
    commentary = CharField(max_length=200)

    class Meta:
        ordering = ['-id']
