class Species:
    def __init__(self, name):
        self.name = name
        self.next = []
        
    def add_next(self, species):
        self.next.append(species)
    
class SpeciesGraph:
    def __init__(self, species_data):
        self.species_dict = {}
        for species_info in species_data:
            name = species_info['name']
            self.species_dict[name] = Species(name)

        for species_info in species_data:
            current_species = self.species_dict[species_info['name']]
            for next_species_name in species_info["next"]:
                next_species = self.species_dict[next_species_name]
                current_species.add_next(next_species)

    @classmethod
    def depth_limited_traversal(cls, species, depth_limit, visited=None, depth=0):
        if visited is None:
            visited = set()
        visited.add(species)
        print(f"{species.name} (Depth: {depth})")
        if depth < depth_limit:
            for next_species in species.next:
                if next_species not in visited:
                    cls.depth_limited_traversal(next_species, depth_limit, visited, depth + 1)
    
    @classmethod
    def depth_limited_search(cls, species, target_species_name, depth):
        if depth == 0:
            return False 
        if species.name == target_species_name:
            return True
        else:
            for next_species in species.next:
                result = cls.depth_limited_search(next_species, target_species_name, depth - 1)
                if result:
                    return True
        return False
    
    @classmethod
    def path_depth_limited_search(cls, species, target_species_name, depth):
        if depth == 0:
            return None
        if species.name == target_species_name:
            return [species]
        else:
            for next_species in species.next:
                path = cls.path_depth_limited_search(next_species, target_species_name, depth - 1)
                if path is not None:
                    return [species] + path
        return None

    @classmethod
    def iterative_deepening_search(cls, species, target_species_name, max_depth):
        for depth_limit in range(max_depth + 1):
            if cls.depth_limited_search(species, target_species_name, depth_limit):
                return True
        return False

    @classmethod
    def path_iterative_deepening_search(cls, species, target_species_name, max_depth):
        for depth_limit in range(max_depth + 1):
            path = cls.path_depth_limited_search(species, target_species_name, depth_limit)
            if path:
                return path
        return None