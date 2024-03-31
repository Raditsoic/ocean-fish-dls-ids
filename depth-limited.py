from species import SpeciesGraph, calculate_graph_depth
import json
      
with open(r'sea-animal-graph.json', 'r') as f:
    species_data = json.load(f)

species_graph = SpeciesGraph(species_data)

print("Feature: \n1. Depth Limited Traversal\n2. Depth Limited Search")
feature = int(input("Which feature do you want to use? (1/2): "))
      
if feature == 1:
    print("=" * 30)
    depth_meter = int(input("How deep do you want to search from the Surface? (meters) "))
    print(f"Depth-Limited Traversal Results (Depth Limit: {depth_meter}m)")
    graph_depth = calculate_graph_depth(depth_meter)
    species_graph.depth_limited_traversal(species_graph.species_dict["Surface"], depth_limit=graph_depth)
elif feature == 2:
    species_search = "Surface"
    print("=" * 30)
    target_species = input("What species do you want to search?: ")
    depth_meter = int(input("How deep do you want to search from the Surface?: "))
    
    graph_depth = calculate_graph_depth(depth_meter) + 1
    print(graph_depth)

    print("=" * 30)
    print(f"Path Depth-Limited Search for {target_species} with Depth Limit {depth_meter}m:")
    if SpeciesGraph.depth_limited_search(species_graph.species_dict[species_search], target_species, graph_depth):
        print("Species Found!! :)")
        path = SpeciesGraph.path_depth_limited_search(species_graph.species_dict[species_search], target_species, graph_depth)
        if path:
            print("Path:", ' -> '.join(species.name for species in path))
    else:
        print("We couldn't find the Species...")