from species import Species, SpeciesGraph
import json
      
with open(r'C:\soic\uni\semester4\ai\ids-dls\data\sea-animal-graph.json', 'r') as f:
    species_data = json.load(f)

species_graph = SpeciesGraph(species_data)

print("Feature: \n1. Depth Limited Traversal\n2. Depth Limited Search")
feature = int(input("Which feature do you want to use? (1/2): "))
      
if feature == 1:
    print("=" * 30)
    depth = int(input("How deep do you want to search from the Surface? "))
    print(f"Depth-Limited Traversal Results (Depth Limit: {depth})")
    species_graph.depth_limited_traversal(species_graph.species_dict["Surface"], depth_limit=depth)
elif feature == 2:
    species_search = "Surface"
    print("=" * 30)
    target_species = input("What species do you want to search?: ")
    depth = int(input("How deep do you want to search from the Surface?: "))

    print("=" * 30)
    print(f"Path Depth-Limited Search for {target_species} with Depth Limit {depth}:")
    if SpeciesGraph.depth_limited_search(species_graph.species_dict[species_search], target_species, depth):
        print("Found!")
        path = SpeciesGraph.path_depth_limited_search(species_graph.species_dict[species_search], target_species, depth)
        if path:
            print("Path:", ' -> '.join(species.name for species in path))
    else:
        print("Not Found!")