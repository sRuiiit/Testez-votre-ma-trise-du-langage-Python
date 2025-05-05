class Rectangle:
    """
    Classe pour représenter un rectangle avec une largeur et une longueur.

    Attributes:
        width (float): La largeur du rectangle.
        length (float): La longueur du rectangle.
    """

    def __init__(self, width, length):
        """
        Initialise un rectangle avec une largeur et une longueur.

        Args:
            width (float): La largeur du rectangle.
            length (float): La longueur du rectangle.
        """
        self.width = width
        self.length = length

    def calculate_area(self):
        """
        Calcule l'aire du rectangle.

        Returns:
            float: L'aire du rectangle.
        """
        return self.width * self.length

    def calculate_perimeter(self):
        """
        Calcule le périmètre du rectangle.

        Returns:
            float: Le périmètre du rectangle.
        """
        return 2 * (self.width + self.length)


# Test de la classe Rectangle
rectangle = Rectangle(5, 3)  # 5: largeur, 3: longueur
print("Largeur:", rectangle.width)
print("Longueur:", rectangle.length)
print("Aire:", rectangle.calculate_area())
print("Périmètre:", rectangle.calculate_perimeter())
