import math          # Import du module math (utilisé pour infini)
import itertools
import time
import sys



cities = [
    'Algiers',
    'Constantine',
    'Batna',
    'Sétif',
    'Djelfa',
    'Annaba',
    'Sidi Aïssa',
    'Sidi Bel Abbès',
    'Biskra',
    'Tébessa',
    'Ouargla',
    'El Khroub',
    'Tiaret',
    'Bejaïa',
    'Tlemcen',
    'Bir el Djir',
    'Bordj Bou Arreridj',
    'Béchar',
    'Blida',
    'Skikda',
    'Souk Ahras',
    'Chlef',
    'El Eulma',
    'Bordj el Kiffan',
    'Mostaganem',
    'Touggourt',
    'Médéa',
    'Tizi Ouzou',
    'El Oued',
    'Laghouat',
    'M’Sila',
    'Jijel',
    'Relizane',
    'Saïda',
    'Baraki',
    'Guelma',
    'Ghardaïa',
    'Aïn Beïda',
    'Maghnia',
    'Bou Saâda',
    'Bou Saada',
    'Mascara',
    'Khenchela',
    'Barika',
    'Messaad',
    'Aflou',
    'Aïn Oussera',
    'Oran'
]

distance_matrix = [
    [0, 319, 309, 219, 232, 419, 114, 375, 320, 478, 572, 329, 219, 178, 445, 343, 170, 749, 37, 342, 440, 167, 244, 12, 281, 490, 60, 88, 511, 328, 177, 239, 251, 338, 10, 391, 478, 402, 480, 198, 135, 302, 395, 256, 290, 306, 145, 351],
    # (matrix unchanged – truncated here for readability in this message)
]

# --------------------------------------------------------------------
# Fonction utilitaire : affichage de progression (non utilisée ici)
# --------------------------------------------------------------------
def display_percentage(i, n, start_time):
    elapsed_percentage = (i + 1) * 100 / n
    remaining_percentage = 100 - elapsed_percentage
    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_percentage > 0:
        remaining_time = remaining_percentage * elapsed_time / elapsed_percentage

    sys.stdout.write(
        f"\rProgress: {elapsed_percentage:.2f}%, "
        f"Elapsed Time: {elapsed_time:.2f}s, "
        f"Remaining Time: {remaining_time:.2f}s"
    )
    sys.stdout.flush()

# --------------------------------------------------------------------
# Distance d’un cycle
# --------------------------------------------------------------------
def calculate_distance(route, distances):
    length = 0
    prev = 0
    for node in route:
        length += distances[prev][node]
        prev = node
    length += distances[prev][0]  # retour à Alger
    return length

# --------------------------------------------------------------------
# Question 1 : Brute Force TSP
# --------------------------------------------------------------------
def brute_force_tsp(distances, cities):
    n = len(cities)
    best_length = math.inf
    best_route = None

    for perm in itertools.permutations(range(1, n)):
        current_route = [0] + list(perm)
        length = calculate_distance(perm, distances)

        if length < best_length:
            best_length = length
            best_route = current_route

    return best_route, best_length

# --------------------------------------------------------------------
# Question 3 : Plus Proche Voisin (Nearest Neighbor)
# --------------------------------------------------------------------
def nearest_neighbor_tsp(distances, cities):
    n = len(cities)
    visited = [False] * n
    route = [0]
    visited[0] = True
    total_distance = 0
    current = 0

    for _ in range(n - 1):
        nearest = None
        min_dist = math.inf
        for j in range(n):
            if not visited[j] and distances[current][j] < min_dist:
                min_dist = distances[current][j]
                nearest = j

        route.append(nearest)
        visited[nearest] = True
        total_distance += min_dist
        current = nearest

    total_distance += distances[current][0]
    route.append(0)

    return route, total_distance

# --------------------------------------------------------------------
# Données du TP (10 villes)
# --------------------------------------------------------------------
cities1 = [
    "Alger","Batna","Oran","Sétif","Constantine",
    "Tlemcen","Ouargla","Annaba","Béchar","Tizi-Ouzou"
]

D = [
    [0,430,415,260,320,520,770,600,970,110],
    [430,0,798,100,120,620,420,300,950,350],
    [415,798,0,430,500,180,850,780,720,380],
    [260,100,430,0,115,500,620,310,800,250],
    [320,120,500,115,0,550,610,160,950,340],
    [520,620,180,500,550,0,1000,720,450,540],
    [770,420,850,620,610,1000,0,720,770,640],
    [600,300,780,310,160,720,720,0,1150,360],
    [970,950,720,800,950,450,770,1150,0,1160],
    [110,350,380,250,340,540,640,360,1160,0]
]

# --------------------------------------------------------------------
# Question 2 : temps et permutations
# --------------------------------------------------------------------
start_time = time.time()
best_route, best_length = brute_force_tsp(D, cities1)
end_time = time.time()

execution_time = end_time - start_time
total_permutations = math.factorial(len(cities1) - 1)

# --------------------------------------------------------------------
# Affichage résultats Brute Force
# --------------------------------------------------------------------
print("Best route (Brute Force):", best_route)
print("Best route length:", best_length)
print("Number of permutations examined:", total_permutations)
print("Execution time:", execution_time, "seconds")

# --------------------------------------------------------------------
# Résultat Plus Proche Voisin
# --------------------------------------------------------------------
nn_route, nn_length = nearest_neighbor_tsp(D, cities1)
print("Nearest Neighbor route:", nn_route)
print("Nearest Neighbor route length:", nn_length)
