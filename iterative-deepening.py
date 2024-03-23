from species import SpeciesGraph
import json

with open(r'C:\soic\uni\semester4\ai\ids-dls\data\sea-animal-graph.json', 'r') as f:
    species_data = json.load(f)

species_graph = SpeciesGraph(species_data)

start_species_name = "Surface"
target_species_name = "Killer Whale"
max_depth = 3

print(f"Iterative Deepening Search for {target_species_name} (Max Depth: {max_depth}):")
result = SpeciesGraph.iterative_deepening_search(species_graph.species_dict[start_species_name], target_species_name, max_depth)
if result:
    print("Found!")
    path = SpeciesGraph.path_iterative_deepening_search(species_graph.species_dict[start_species_name], target_species_name, max_depth)
    if path:
        print("Path:", [species.name for species in path])
else:
    print("Not Found!")