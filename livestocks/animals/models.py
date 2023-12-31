import uuid
from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


# Create your models here.
class Specific(models.Model):
    animal_id = models.CharField(
        max_length=200,
        unique=True,
        help_text="any way to ID the lamb visually name or number",
    )
    GENDER_OPTIONS = (
        ("fx", "fixed"),
        ("f", "female"),
        ("m", "male"),
        ("s", "stud"),
    )
    gender = models.CharField(
        max_length=3,
        choices=GENDER_OPTIONS,
        blank=True,
    )

    birth_date = models.DateField()
    sibling_set = models.PositiveSmallIntegerField(
        null=True, default=1, help_text="born as single (1), twin(2), triplet(3), etc"
    )
    species_id = models.ForeignKey("Specie", on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return self.animal_id

    def get_absolute_url(self):
        return reverse("animal-detail", args=[str(self.id)])


class History(models.Model):
    id = (
        models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            help_text="Unique ID animal status update",
        ),
    )
    animal_id = models.ForeignKey("Specific", on_delete=models.RESTRICT, null=True)
    ANIMAL_STATUS = {
        "s": "sold",
        "i": "ill",
        "a": "active",
        "p": "purchased",
        "d": "delivered",
    }
    status = models.CharField(
        max_length=1, choices=ANIMAL_STATUS, blank=True, default="a"
    )
    notes = models.TextField(verbose_name="Info pertaining to status")

    def __str__(self):
        return f"{self.ANIMAL_STATUS[self.status]} status to {self.animal_id} "

    def get_absolute_url(self):
        return reverse("history-detail", args=[str(self.id)])


class Specie(models.Model):
    specie = models.CharField(
        max_length=200, unique=True, help_text="the type of livestock animal"
    )
    breed = models.CharField(
        max_length=200, unique=True, help_text="from the specie what name of breed"
    )

    def __str__(self):
        return self.breed

    def get_absolute_url(self):
        return reverse("breed-detail", args=[str(self.id)])


class Genealogy(models.Model):
    which_animal = models.ForeignKey(
        "Specific",
        on_delete=models.RESTRICT,
        null=True,
        verbose_name="Animal id",
        help_text="Animal define relation to",
    )

    family_tree = models.ForeignKey(
        "Specific",
        on_delete=models.RESTRICT,
        null=True,
        related_name="same_blood",
        verbose_name="Animal that is related",
        help_text="Select animal born of or born with",
    )
    RELATION_TYPE = (
        ("m", "mother"),
        ("f", "father"),
        ("s", "sibling"),
    )
    relation = models.CharField(max_length=1, choices=RELATION_TYPE, blank=True)

    def __str__(self):
        return f"{self.which_animal} related to {self.family_tree}"

    def get_absolute_url(self):
        return reverse("relation-detail", args=[str(self.id)])


class Record(models.Model):
    animal_id = models.ForeignKey("Specific", on_delete=models.RESTRICT, null=True)
    value = models.DecimalField(max_digits=6, decimal_places=2, help_text="currency")
    SELL_PURCHASE = {
        "s": "sold",
        "p": "purchased",
        "fs": "for sale",
    }
    action = models.CharField(
        max_length=2,
        choices=SELL_PURCHASE,
        blank=True,
    )

    def __str__(self):
        return f"{self.SELL_PURCHASE[self.action]} {self.animal_id} "

    def get_absolute_url(self):
        return reverse("action-detail", args=[str(self.id)])
