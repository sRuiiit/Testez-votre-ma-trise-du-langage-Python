def log_decorator(func):
    """
    Décorateur qui affiche un message avant et après l'exécution d'une fonction.

    Args:
        func (function): La fonction à enrouler.

    Returns:
        function: La fonction enroulée.
    """
    def wrapper():
        print("Avant l'exécution de la fonction.")
        func()
        print("Après l'exécution de la fonction.")
    return wrapper

@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")

function_test()
