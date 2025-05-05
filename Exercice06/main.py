def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)# Fonction calculate_average
 
# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", average)

