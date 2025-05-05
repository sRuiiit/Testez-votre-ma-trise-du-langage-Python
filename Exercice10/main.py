class Person:
    """
    Classe représentant une personne avec un nom et un âge.
    """

    def __init__(self, name, age):
        """
        Initialise une personne avec un nom et un âge.

        Args:
            name (str): Le nom de la personne.
            age (int): L'âge de la personne.
        """
        self.name = name
        self.age = age

    def display_details(self):
        """
        Affiche les détails de la personne.
        """
        print(f"Nom: {self.name}, Âge: {self.age}")


class Employee(Person):
    """
    Classe représentant un employé, héritant de la classe Person.
    """

    def __init__(self, name, age, salary):
        """
        Initialise un employé avec un nom, un âge et un salaire.

        Args:
            name (str): Le nom de l'employé.
            age (int): L'âge de l'employé.
            salary (float): Le salaire de l'employé.
        """
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        """
        Affiche les détails de l'employé, y compris son salaire.
        """
        super().display_details()
        print(f"Salaire: {self.salary}")

# exemple l'utilisation

# Exemple d'utilisation des classes
person = Person("Alice", 30)
person.display_details()

employee = Employee("Bob", 40, 50000)
employee.display_details()


