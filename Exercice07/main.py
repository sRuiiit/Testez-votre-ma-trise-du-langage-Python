def square(value):
    """
    Calcule le carré d'un nombre.

    Args:
        value (int ou float): Le nombre à mettre au carré.

    Returns:
        int ou float: Le carré du nombre si le paramètre est valide.
        None: Si le paramètre n'est pas un nombre.
    """
    if not isinstance(value, (int, float)):
        print("Le paramètre doit être un nombre !")
        return None
    return value ** 2

# Demander à l'utilisateur de saisir un nombre
try:
    user_input = float(input("Entrez un nombre : "))
    result = square(user_input)
    print("Résultat :", result)
except ValueError:
    print("Le paramètre doit être un nombre valide !")
