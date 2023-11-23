# Pokémon RDF Data
A Pokémon dataset in RDF to do queries in SPARQL and inferences in OWL. Final project for the Web Data (CC7220) course.
For the SPARQL queries, we used the ``rdflib`` library, and for converting the CSV dataset to TTL, we used ``pandas``.

## Requirements
Before running the script you need to follow these steps:

1. Create a virtual environment:
```
python -m venv venv
```

2. Activate the virtual environment to install the requirements:
```
.\venv\Scripts\activate
```

3. Once you have the virtual environment active:
```
pip install -r requirements.txt
```

## SPARQL Queries
After setting up the virtual environment and installing the requirements, you should navigate to the ``py`` folder to run the ``query_sparql.py`` script, but first, open the script file and insert your SPARQL query, for example:

```python
PREFIXES = """
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX pkmn: <http://www.ex.org/#>
"""

# This should be your query
sparql_query = PREFIXES + """
SELECT DISTINCT ?pokemonName
WHERE {
  ?pokemon rdf:type pkmn:Pokemon ;
           pkmn:hasName ?pokemonName ;
           pkmn:isLegendary 1.
  FILTER(LANG(?pokemonName) = "en")
  {
    ?pokemon pkmn:hasType1 "grass"
  }
  UNION
  {
    ?pokemon pkmn:hasType2 "grass"
  }
}
"""


results = g.query(sparql_query)

for row in results:
    # Make sure to change 'pokemonName' with what you have selected in your SPARQL query.
    print(row['pokemonName'])
```

Then, simply execute the following command:
```
python query_sparql.py
```
This will print in the terminal the results of your SPARQL query using the Pokemon dataset provided (in this case, all legendary Pokémon that are grass type):
```
Celebi
Shaymin
Virizion
Tapu Bulu
Kartana
```

👀 We have some queries in the ``./queries/queries.sparql`` file so you can try it! 👀

## OWL Inferences
👀 You can also find OWL inferences for this dataset in `./inferences/inferences.ttl`! 👀\
To see the results, it is necessary to copy some example Pokémon (from the dataset) into [RDF Playground](https://rdfplayground.fabianvillena.cl/).

For instance, consider the following statement that infers all the Starter Pokémon:
```owl
pkmn:Starter rdf:type owl:Class .
pkmn:Starter owl:equivalentClass [owl:hasValue 'Overgrow' ; owl:onProperty pkmn:hasAbility] .
pkmn:Starter owl:equivalentClass [owl:hasValue 'Blaze' ; owl:onProperty pkmn:hasAbility] .
pkmn:Starter owl:equivalentClass [owl:hasValue 'Torrent' ; owl:onProperty pkmn:hasAbility] .
```

We selected these Pokémon from the dataset to test it:
```ttl
@prefix pkmn:<http://www.ex.org/#>.
@prefix rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>.

pkmn:Bulbasaur rdf:type pkmn:Pokemon ;
    pkmn:hasName 'Bulbasaur'@en, 'Fushigidaneフシギダネ'@jp ;
    pkmn:hasPokedexNumber 1 ;
    pkmn:hasType1 "grass" ;
    pkmn:hasType2 "poison" ;
    ...
    ...

pkmn:Pidgey rdf:type pkmn:Pokemon ;
    pkmn:hasName 'Pidgey'@en, 'Poppoポッポ'@jp ;
    pkmn:hasPokedexNumber 16 ;
    pkmn:hasType1 "normal" ;
    pkmn:hasType2 "flying" ;
    ...
    ...

pkmn:Oshawott rdf:type pkmn:Pokemon ;
    pkmn:hasName 'Oshawott'@en, 'Mijumaruミジュマル'@jp ;
    pkmn:hasPokedexNumber 501 ;
    pkmn:hasType1 "water" ;
    ...
    ...

pkmn:Pikachu rdf:type pkmn:Pokemon ;
    pkmn:hasName 'Pikachu'@en, 'Pikachuピカチュウ'@jp ;
    pkmn:hasPokedexNumber 25 ;
    pkmn:hasType1 "electric" ;
    ...
    ...
```
We know that in this example only Bulbasaur and Oshawott are starters, when we run the inference, we obtain the following results:

```
pkmn:Bulbasaur a _:naa84f3000a7d46888eceaf7354cf52bbb1,
        _:naa84f3000a7d46888eceaf7354cf52bbb2,
        _:naa84f3000a7d46888eceaf7354cf52bbb3,
        pkmn:Pokemon,
        pkmn:Starter, # It works!
        owl:Thing ;
        ...
        ...

pkmn:Oshawott a _:naa84f3000a7d46888eceaf7354cf52bbb1,
        _:naa84f3000a7d46888eceaf7354cf52bbb2,
        _:naa84f3000a7d46888eceaf7354cf52bbb3,
        pkmn:Pokemon,
        pkmn:Starter, # It works!
        owl:Thing ;
        ...
        ...

pkmn:Pidgey a pkmn:Pokemon ;
    pkmn:againstBug 0.5 ;
    pkmn:againstDark 1.0 ;
    pkmn:againstDragon 1.0 ;
    pkmn:againstElectric 2.0 ;
    ...
    ...

pkmn:Pikachu a pkmn:Pokemon ;
    pkmn:againstBug 1.0 ;
    pkmn:againstDark 1.0 ;
    pkmn:againstDragon 1.0 ;
    pkmn:againstElectric 0.5 ;
    ...
    ...
```