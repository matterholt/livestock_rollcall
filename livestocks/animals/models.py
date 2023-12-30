import uuid
from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

# animal_species
#   id integer [primary key]
#   breed varchar
#   species varchar
#   created_at timestamp

# Create your models here.
class Specific(models.Model):
    gender = models.CharField(max_length=200)
    animal_id = models.CharField(max_length=200, unique=True, help_text = "any way to ID the lamb visually name or number")
    birth_date = models.CharField(max_length=200)
    sibling_set = models.CharField(max_length=200, unique=True, help_text = "born as single (1), twin(2), triplet(3)")


    def __str__(self):
        return self.breed
    
    def get_absolute_url (self):
        return reverse('breed-detail', args=[str(self.id)])
    
class History(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID animal status update"),
    ANIMAL_STATUS =(
        ('s','sold'),
        ('i','ill'),
        ('r','roster'),
        ('p','purchased'),
        ('d','delivered'),
    )
    status = models.CharField(max_length=1, choices=ANIMAL_STATUS, blank=True, default='r')
    notes = models.CharField(max_length=500)
    animal_id = models.ForeignKey(Specific, on_delete=models.RESTRICT, null= True)

    def __str__(self):
        return self.status
    def get_absolute_url(self):
        return reverse('history-detail',args=[str(self.id)])

class Specie(models.Model):
    
    specie = models.CharField(max_length=200, unique=True, help_text = "the type of livestock animal")
    breed = models.CharField(max_length=200, unique=True, help_text = "from the specie what name of breed")
    animal_id = models.ForeignKey(Specific, on_delete=models.RESTRICT, null= True)

    def __str__(self):
        return self.breed
    
    def get_absolute_url (self):
        return reverse('breed-detail', args=[str(self.id)])