from django.db import models
from django.db import models
from django.db.models import Model, DateTimeField
from django.utils.text import slugify

from metsenat.enums import SponsorTypeChoose, SponsorStatusChoose, PaymentTypeChoose, StudentTypeChoose


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Sponsor(BaseModel):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True, null=True, blank=True)
    sponsor_type = models.CharField(max_length=100, choices=SponsorTypeChoose.choices,
                                    default=SponsorTypeChoose.INDIVIDUAL)
    phone_number = models.CharField(max_length=128)
    balance = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    company_name = models.CharField(max_length=128, null=True, blank=True)
    register_datetime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=SponsorStatusChoose.choices, default=SponsorStatusChoose.NEW)
    spent_amount = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    payment_type = models.CharField(max_length=100, choices=PaymentTypeChoose.choices, default=PaymentTypeChoose.UZCARD)

    def __str__(self):
        return self.name

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Sponsor.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.name = slugify(self.name)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)


class University(BaseModel):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True, null=True, blank=True)

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while University.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.name = slugify(self.name)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return self.name


class Student(BaseModel):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True, null=True, blank=True)
    student_type = models.CharField(max_length=100, choices=StudentTypeChoose.choices)
    received_amount = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    tuition_fee = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    phone_number = models.CharField(max_length=128)

    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='students')

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Student.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.name = slugify(self.name)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return self.name


class StudentSponsor(BaseModel):
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, related_name='students')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='sponsors')
    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        sponsor = self.sponsor
        sponsor.balance -= self.amount
        sponsor.spent_amount += self.amount
        sponsor.save()

        student = self.student
        student.received_amount += self.amount
        student.save()

        super().save(force_insert=False, force_update=False, update_fields=None)

    def __str__(self):
        return f"{self.sponsor}:{self.student}"
