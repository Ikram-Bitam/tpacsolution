import math          # Import du module math (utilisé pour infini)
import itertools     # Import pour générer les permutations (brute force)
import time          # Pour mesurer le temps d'exécution


# --------------------------------------------------------------------
# Fonction à compléter : brute force TSP
# --------------------------------------------------------------------
def brute_force_tsp(distances):
    """
    distances : matrice NxN des distances entre les villes
    Retour attendu : (best_route, best_length)

    Les étudiants doivent :
    1. Fixer le point de départ (index 0 = Alger)
    2. Générer toutes les permutations des autres villes (1..n-1)
    3. Calculer la distance de chaque route
    4. Trouver la route minimale
    """

    n = len(distances)
    start = 0
    others = list(range(1, n))

    best_length = math.inf
    best_route = None

    permutation_count = 0
    start_time = time.time()

    # --------------- BRUTE FORCE ---------------
    for perm in itertools.permutations(others):
        permutation_count += 1

        route = (start,) + perm + (start,)     # cycle Hamiltonien
        total = 0

        # Calculer la distance totale du cycle
        for i in range(len(route) - 1):
            total += distances[route[i]][route[i+1]]

        # Mise à jour du minimum
        if total < best_length:
            best_length = total
            best_route = route

    exec_time = time.time() - start_time

    # Affichage demandé dans le PDF
    print("\nNombre total de permutations examinées :", permutation_count)
    print("Temps d'exécution :", round(exec_time, 4), "secondes\n")

    return best_route, best_length


# --------------------------------------------------------------------
# Liste des 10 villes
# --------------------------------------------------------------------
cities = [
    "Alger","Batna","Oran","Sétif","Constantine",
    "Tlemcen","Ouargla","Annaba","Béchar","Tizi-Ouzou"
]


# --------------------------------------------------------------------
# Matrice des distances entre les villes (symétrique)
# --------------------------------------------------------------------
D = [
    [0,   430, 415, 260, 320, 520, 770, 600, 970, 110],
    [430,   0, 798, 100, 120, 620, 420, 300, 950, 350],
    [415, 798,   0, 430, 500, 180, 850, 780, 720, 380],
    [260, 100, 430,   0, 115, 500, 620, 310, 800, 250],
    [320, 120, 500, 115,   0, 550, 610, 160, 950, 340],
    [520, 620, 180, 500, 550,   0,1000, 720, 450, 540],
    [770, 420, 850, 620, 610,1000,   0, 720, 770, 640],
    [600, 300, 780, 310, 160, 720, 720,   0,1150, 360],
    [970, 950, 720, 800, 950, 450, 770,1150,   0,1160],
    [110, 350, 380, 250, 340, 540, 640, 360,1160,   0]
]


# --------------------------------------------------------------------
# Appel de la fonction brute force
# --------------------------------------------------------------------
best_route, best_length = brute_force_tsp(D)


# --------------------------------------------------------------------
# Affichage du résultat (uniquement les noms des villes)
# --------------------------------------------------------------------
print("Meilleur cycle (villes)  :", " → ".join(cities[i] for i in best_route))
print("Longueur totale du cycle :", best_length, "km")
