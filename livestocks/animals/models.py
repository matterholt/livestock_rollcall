import uuid
from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns

# animal_species
#   id integer [primary key]
#   breed varchar
#   species varchar
#   created_at timestamp


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
    ANIMAL_STATUS = (
        ("s", "sold"),
        ("i", "ill"),
        ("a", "active"),
        ("p", "purchased"),
        ("d", "delivered"),
    )
    status = models.CharField(
        max_length=1, choices=ANIMAL_STATUS, blank=True, default="a"
    )
    notes = models.CharField(max_length=500)
    animal_id = models.ForeignKey("Specific", on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return self.status

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
    which_animal = models.ForeignKey("Specific", on_delete=models.RESTRICT, null=True)

    family_tree = models.ForeignKey(
        "Specific",
        on_delete=models.RESTRICT,
        null=True,
        default=0,
        related_name="same_blood",
    )
    RELATION_TYPE = (
        ("m", "mother"),
        ("f", "father"),
        ("s", "sibling"),
    )
    relation = models.CharField(max_length=1, choices=RELATION_TYPE, blank=True)

    def __str__(self):
        return self.which_animal

    def get_absolute_url(self):
        return reverse("relation-detail", args=[str(self.id)])


class Record(models.Model):
    SELL_PURCHASE = (
        ("s", "sold"),
        ("p", "purchased"),
        ("fs", "for sale"),
        ("k", "keeper"),
    )
    action = models.CharField(
        max_length=2, choices=SELL_PURCHASE, blank=True, default="k"
    )
    value = models.IntegerField(default=0)
    animal_id = models.ForeignKey("Specific", on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return self.action

    def get_absolute_url(self):
        return reverse("action-detail", args=[str(self.id)])
