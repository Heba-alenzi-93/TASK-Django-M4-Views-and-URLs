from django.http import HttpResponse
from .models import Pokemon


def get_pokemon (request,pokemon_id):
    pokemons = Pokemon.objects.get(id =pokemon_id )
    print(pokemons)
    return HttpResponse (f"""<ol><li> name: {pokemons.name}</li>
     <li> type:{pokemons.type}</li>
     <li> hp: {pokemons.hp} </li> </ol>""")


def get_pokemons (request):
    pokemonss = Pokemon.objects.all().values_list("name",flat=True)
    Pokemon_list = "\n".join(f"<li>{pokemon}</li>" for pokemon in pokemonss)
    return HttpResponse(f"<i>{Pokemon_list}</i>")


