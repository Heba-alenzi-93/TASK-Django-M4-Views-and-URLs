from django.http import HttpResponse
from .models import Pokemon


def get_pokemon (request,pokemon_id):
    pokemons = Pokemon.objects.get(id =pokemon_id )
    print(pokemons)
    return HttpResponse (f"{pokemons.name}\n {pokemons.type}\n {pokemons.hp}")






