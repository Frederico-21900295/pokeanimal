from django_tables2 import tables

from website.models import Pokedex


class PersonTable(tables.Table):
    class Meta:
        model = Pokedex
        attrs = {'class': 'paleblue'}


table = PersonTable()

