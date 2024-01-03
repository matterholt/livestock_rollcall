from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("registered", views.registered_animal, name="registered"),
]

"""'
SAMPLE
catalog/
catalog/books/
catalog/authors/
catalog/book/<id>
catalog/author/<id>


animals/  -> all animals entered
animal/records -> all animals bought and sold
animal/specie  -> all types of animals on the farm

animal/<id> -> shows animal specifics , and history
animal/<id>/relations -> all animals related to animal id

animal/specie/<id> -> all the sheep or whatever
animal/specie/<id>/<breed> -> all the katahdin or what ever



"""
