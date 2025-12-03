import time
import sys
import os

# Changer le répertoire courant vers celui où se trouve le script.
os.chdir(os.path.dirname(__file__))

#############################################################################################################################
# QUESTION 1 – Lecture du fichier
#############################################################################################################################

def read_file(file_name):
    file = open(file_name, 'r')
    values = []
    for line in file:
        values.append(int(line.strip()))
    file.close()
    return values


#############################################################################################################################
# QUESTION 2 & 3 – Comptage des occurrences O(n²) + analyse + chronométrage
#############################################################################################################################

def nombre_occurrences(values_list):
    iterations = 0
    start_time = time.time()
    occurrences = dict()
    remaining_time = 0

    for i in range(n):
        iterations += 1
        count = 0
        for j in range(n):
            iterations += 1
            if values_list[j] == values_list[i]:
                count += 1
            occurrences[values_list[i]] = count

        elapsed_percentage   = (i + 1) * 100 / n
        remaining_percentage = 100 - elapsed_percentage

        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_percentage > 0:
            remaining_time = remaining_percentage * elapsed_time / elapsed_percentage

        sys.stdout.write(f"\rProgress: {elapsed_percentage:.2f}%, Elapsed Time: {elapsed_time:.2f}s, Remaining: {remaining_time:.2f}s")
        sys.stdout.flush()

    end_time = time.time()
    print(f"\n⏱ Durée totale du comptage : {end_time - start_time:.5f} secondes")
    print(f"Nombre total d’itérations : {iterations}")
    return occurrences


#############################################################################################################################
# QUESTION 4 – Version améliorée O(n)
#############################################################################################################################

def nombre_occurrences_ameliore(values_list):
    start_time = time.time()
    iterations = 0
    occurrences = dict()

    for value in values_list:
        iterations += 1
        if value in occurrences:
            occurrences[value] += 1
        else:
            occurrences[value] = 1

    end_time = time.time()

    print("\n---- VERSION AMÉLIORÉE (O(n)) ----")
    print(f"⏱ Durée totale : {end_time - start_time:.5f} sec")
    print(f"Nombre d’itérations : {iterations}")
    print("Complexité : O(n)")
    return occurrences


#############################################################################################################################
# QUESTION 5 – Tri par sélection (Selection Sort)
#############################################################################################################################

def selection_sort(values_list):
    tab = values_list.copy()
    n = len(tab)
    iterations = 0
    start_time = time.time()

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            iterations += 1
            if tab[j] < tab[min_index]:
                min_index = j
        tab[i], tab[min_index] = tab[min_index], tab[i]

    end_time = time.time()

    print("\n---- TRI PAR SÉLECTION ----")
    print("Complexité : O(n²)")
    print(f"Nombre d’itérations : {iterations}")
    print(f"⏱ Durée : {end_time - start_time:.5f} sec")
    return tab


#############################################################################################################################
# QUESTION 6 – Tri par fusion (Merge Sort)
#############################################################################################################################

merge_iterations = 0

def merge(left, right):
    global merge_iterations
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        merge_iterations += 1
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(tab):
    global merge_iterations
    merge_iterations = 0
    start_time = time.time()

    def divide(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        return merge(divide(arr[:mid]), divide(arr[mid:]))

    sorted_tab = divide(tab)

    end_time = time.time()

    print("\n---- TRI PAR FUSION ----")
    print("Complexité : O(n log n)")
    print(f"Nombre d’itérations : {merge_iterations}")
    print(f"⏱ Durée : {end_time - start_time:.5f} sec")

    return sorted_tab


#############################################################################################################################
# QUESTION 7 – Sauvegarde du tableau trié
#############################################################################################################################

def write_to_file(tab):
    with open("valeurs_aleatoires_tries.txt", "w") as f:
        for value in tab:
            f.write(str(value) + "\n")
    print("\n📄 Fichier 'valeurs_aleatoires_tries.txt' enregistré avec succès.")


#############################################################################################################################
# SCRIPT PRINCIPAL
#############################################################################################################################

valeurs_aleatoires_list = read_file('valeurs_aleatoires.txt')
n = len(valeurs_aleatoires_list)

print("Valeurs lues :", valeurs_aleatoires_list[:10], "...")
print("Longueur de la liste :", n)

# QUESTION 2 & 3
occurrences_on2 = nombre_occurrences(valeurs_aleatoires_list)

# QUESTION 4
# occurrences_on = nombre_occurrences_ameliore(valeurs_aleatoires_list)

# QUESTION 5
# sorted_selection = selection_sort(valeurs_aleatoires_list)

# QUESTION 6
# sorted_merge = merge_sort(valeurs_aleatoires_list)

# QUESTION 7
# write_to_file(sorted_merge)
