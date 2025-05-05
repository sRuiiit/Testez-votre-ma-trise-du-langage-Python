words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

vowels = "aeiou"

# Créer une liste de compréhension avec des tuples (mot, nombre de voyelles)
word_vowel_counts = [(word, sum(1 for char in word if char in vowels)) for word in words]

# Afficher la liste créée
print(word_vowel_counts)

