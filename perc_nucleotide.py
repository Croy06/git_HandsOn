#!/usr/bin/env python

# ESTE ES LA PRIMERA VERSIÓN DEL CÓDIGO

def nucleotide_percentage():
    # Solicitar al usuario que introduzca una secuencia
    sequence = input("Introduzca una secuencia: ")

    # Crear un diccionario para almacenar los conteos de nucleótidos
    nucleotide_counts = {"A": 0, "C": 0, "G": 0, "T": 0, "U": 0}

    # Contar los nucleótidos en la secuencia
    for nucleotide in sequence:
        if nucleotide in nucleotide_counts:
            nucleotide_counts[nucleotide] += 1

    # Calcular los porcentajes
    total = len(sequence)
    nucleotide_percentages = {nucleotide: count / total * 100 for nucleotide, count in nucleotide_counts.items()}

    return nucleotide_percentages

# Prueba la función
print(nucleotide_percentage())
