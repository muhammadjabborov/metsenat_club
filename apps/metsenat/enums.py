from django.db.models import TextChoices


class SponsorTypeChoose(TextChoices):
    INDIVIDUAL = 'individual', 'Individual'
    ENTITY = 'entity', 'Entity'


class SponsorStatusChoose(TextChoices):
    NEW = 'yangi', 'New'
    IN_MODERATION = 'moderatsiyada', 'In Moderation'
    CONFIRMED = 'tasdiglangan', 'Confirmed'
    CANCELED = 'bekor qilingan', 'Canceled'


class PaymentTypeChoose(TextChoices):
    UZCARD = 'uzcard', 'Uzcard'
    HUMO = 'humo', 'Humo'
    VISA = 'visa', 'Visa'
    CASH = 'cash', 'Cash'


class StudentTypeChoose(TextChoices):
    BACHELOR = 'bakalavr', 'Bachelor'
    MASTERS = 'magistr', 'Masters'
