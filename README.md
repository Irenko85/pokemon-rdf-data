# Pokemon RDF Data
A Pokemon dataset in RDF to do queries in SPARQL and inferences in OWL. Project for Web Data (CC7220).
For the SPARQL queries, we used the *rdflib* library, and for converting the CSV dataset to TTL, we used *pandas*.

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

## Running the script
After setting up the virtual environment and installing the requirements, you should navigate to the *py* folder to run the *query_sparql.py* script, but first, open the script file and put your SPARQL query, for example:

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
         pkmn:hasName ?pokemonName;
         pkmn:isLegendary 1.
FILTER(LANG(?pokemonName) = "en")
  {?pokemon pkmn:hasType1 "grass"}
  UNION
  {?pokemon pkmn:hasType2 "grass"}
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

We have some interesting 👀 queries in the `./queries/queries.sparql` file so you can try it!\
Also, you can find OWL inferences for this dataset in `./inferences/inferences.ttl`.