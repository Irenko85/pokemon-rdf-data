import pandas as pd

# Importar el csv
dataset = pd.read_csv('../dataset/pokemon.csv', sep=',', encoding='utf-8')

# Crear archivo de salida
file = open('../dataset/pokemon.ttl', 'w', encoding='utf-8')

PREFIX_RDF = "@prefix rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>."
PREFIX_PKMN = "@prefix pkmn:<http://www.ex.org/#>."

# Reemplazar los nulos por 0 en percentage_male
dataset['percentage_male'] = dataset['percentage_male'].fillna(0)

# Recorrer el dataset
text = PREFIX_PKMN + "\n" + PREFIX_RDF + "\n\n"
for index, row in dataset.iterrows():
    text += f"""
    pkmn:{row['name']} rdf:type pkmn:Pokemon ;
        pkmn:hasName '{row['name']}'@en, '{row['japanese_name']}'@jp ;
        pkmn:hasPokedexNumber {row['pokedex_number']} ;
        pkmn:hasType1 "{row['type1']}" ;
        {f'pkmn:hasType2 "{row["type2"]}" ;' if not pd.isna(row['type2']) else ''}
        pkmn:hasHP {row['hp']} ;
        pkmn:hasAttack {row['attack']} ;
        pkmn:hasDefense {row['defense']} ;
        pkmn:hasSpAttack {row['sp_attack']} ;
        pkmn:hasSpDefense {row['sp_defense']} ;
        pkmn:hasSpeed {row['speed']} ;
        pkmn:hasBaseTotal {row['base_total']} ;
        pkmn:hasGeneration {row['generation']} ;
        pkmn:hasHeight {row['height_m']} ;
        pkmn:hasWeight {row['weight_kg']} ;
        pkmn:hasPercentageMale {row['percentage_male']} ;
        pkmn:hasCaptureRate {row['capture_rate']} ;
        pkmn:hasBaseEggSteps {row['base_egg_steps']} ;
        pkmn:hasBaseHappiness {row['base_happiness']} ;
        pkmn:hasExperienceGrowth {row['experience_growth']} ;
        pkmn:hasClassification "{row['classfication']}" ;
        pkmn:againstBug {row['against_bug']} ;
        pkmn:againstDark {row['against_dark']} ;
        pkmn:againstDragon {row['against_dragon']} ;
        pkmn:againstElectric {row['against_electric']} ;
        pkmn:againstFairy {row['against_fairy']} ;
        pkmn:againstFight {row['against_fight']} ;
        pkmn:againstFire {row['against_fire']} ;
        pkmn:againstFlying {row['against_flying']} ;
        pkmn:againstGhost {row['against_ghost']} ;
        pkmn:againstGrass {row['against_grass']} ;
        pkmn:againstGround {row['against_ground']} ;
        pkmn:againstIce {row['against_ice']} ;
        pkmn:againstNormal {row['against_normal']} ;
        pkmn:againstPoison {row['against_poison']} ;
        pkmn:againstPsychic {row['against_psychic']} ;
        pkmn:againstRock {row['against_rock']} ;
        pkmn:againstSteel {row['against_steel']} ;
        pkmn:againstWater {row['against_water']} ;
    """

    abilities = row['abilities'].strip('][').split(', ')
    if abilities:
        text += "    pkmn:hasAbility "
        text += " , ".join([f'{ability}' for ability in abilities])
        text += " ;"

    text += f"""
        pkmn:isLegendary {row['is_legendary']} .
    """


file.write(text)
file.close()

