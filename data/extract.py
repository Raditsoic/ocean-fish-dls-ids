from bs4 import BeautifulSoup
import json
from species import Species

with open('sea.html', 'r') as f:
    html_content = f.read()
    
soup = BeautifulSoup(html_content, 'html.parser')
animal_names = soup.find_all('div', class_= 'animal-name')

species_dict = {}
for animal in animal_names:
    name = animal.text
    species_dict[name] = Species(name)

def species_to_json(species):
    json_dict = {
        "name": species.name,
        "next": []
    }
    return json_dict

graph_json = [species_to_json(species_dict[name]) for name in species_dict]

with open('sea-animal-graph.json', 'w') as json_file:
    json.dump(graph_json, json_file, indent=4)
    