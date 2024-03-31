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
    def iterative_deepening_search(cls, start_species_name, target_species_name, max_depth):
        iter = 1
        while True:
            if cls.depth_limited_search(start_species_name, target_species_name, max_depth):
                return True, iter
            max_depth += 1
            iter += 1

    @classmethod
    def path_iterative_deepening_search(cls, species, target_species_name, max_depth):
        while True:
            path = cls.path_depth_limited_search(species, target_species_name, max_depth)
            if path:
                return path
            max_depth += 1
    
def calculate_graph_depth(real_depth:int):
    depth_dict = {
        20: 1, 40: 2, 60: 3, 80: 4, 100: 5, 120: 6, 140: 7, 160: 8, 180: 9, 200: 10,
        220: 11, 250: 12, 300: 13, 350: 14, 400: 15, 450: 16, 500: 17, 550: 18, 600: 19, 650: 20,
        700: 21, 800: 22, 900: 23, 1000: 24, 1150: 25, 1300: 26, 1450: 27, 1600: 28, 1800: 29, 2000: 30,
        2200: 31, 2600: 32, 3000: 33, 3400: 34, 3800: 35, 4300: 36, 4800: 37, 5300: 38, 6300: 39, 6301: 40 
    }
    
    closest_depth = min(depth_dict.keys(), key=lambda x: abs(x - real_depth))
    return depth_dict[closest_depth]