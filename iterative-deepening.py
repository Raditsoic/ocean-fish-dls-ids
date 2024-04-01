from species import SpeciesGraph, calculate_graph_depth
import json

with open(r'sea-animal-graph.json', 'r') as f:
    species_data = json.load(f)

species_graph = SpeciesGraph(species_data)

print(f"Welcome to ocean-fish!!\n{'=' * 30}")
start_species_name = "Surface"
target_species_name = input("Which Species do you want to find?: ")
max_depth = int(input("How deep do you want to do in each iteration? (meter): "))
graph_depth = calculate_graph_depth(max_depth)

print(f"Iterative Deepening Search for {target_species_name} (Max Depth per iteration: {max_depth}m):")
result, iteration = SpeciesGraph.iterative_deepening_search(species_graph.species_dict[start_species_name], target_species_name, graph_depth)
if result:
    print("=" * 30)
    print("Species Found!")
    print(f"We Found {target_species_name} within {iteration} tries...")
    path = SpeciesGraph.path_iterative_deepening_search(species_graph.species_dict[start_species_name], target_species_name, max_depth)
    if path:
        print("Path:", ' -> '.join(species.name for species in path))
else:
    print("We couldn't find the Species...")