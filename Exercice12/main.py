class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = []

    def add_book(self, book):
        """
        Ajoute un livre à la bibliothèque.

        Args:
            book (Book): Le livre à ajouter.
        """
        self.books.append(book)

    def remove_book(self, book_title):
        """
        Supprime un livre de la bibliothèque.

        Args:
            book_title (str): Le titre du livre à supprimer.
        """
        self.books = [book for book in self.books if book.title != book_title]

    def borrow_book(self, book_title):
        """
        Emprunte un livre de la bibliothèque.

        Args:
            book_title (str): Le titre du livre à emprunter.

        Raises:
            ValueError: Si le livre n'est pas disponible.
        """
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrowed_books.append(book)
                return
        raise ValueError("Le livre n'est pas disponible.")

    def return_book(self, book_title):
        """
        Rend un livre emprunté à la bibliothèque.

        Args:
            book_title (str): Le titre du livre à rendre.

        Raises:
            ValueError: Si le livre n'a pas été emprunté.
        """
        for book in self.borrowed_books:
            if book.title == book_title:
                self.borrowed_books.remove(book)
                self.books.append(book)
                return
        raise ValueError("Le livre n'a pas été emprunté.")

    def available_books(self):
        """
        Renvoie une liste des titres des livres disponibles.

        Returns:
            list: Les titres des livres disponibles.
        """
        return [book.title for book in self.books]

    def borrowed_books_list(self):
        """
        Renvoie une liste des titres des livres empruntés.

        Returns:
            list: Les titres des livres empruntés.
        """
        return [book.title for book in self.borrowed_books]

# Exemple d'utilisation des classes Book et Library

# Création de livres
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)
book3 = Book("Harry Potter à l'école des sorciers", "J.K. Rowling", 1997)

# Création de la bibliothèque
library = Library()

# Ajout des livres à la bibliothèque
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Affichage des livres disponibles
print("Livres disponibles :", library.available_books())

# Emprunt d'un livre
library.borrow_book("1984")
print("Livres disponibles après emprunt :", library.available_books())
print("Livres empruntés :", library.borrowed_books_list())

# Retour d'un livre
library.return_book("1984")
print("Livres disponibles après retour :", library.available_books())
print("Livres empruntés :", library.borrowed_books_list())

# Suppression d'un livre
library.remove_book("Le Petit Prince ")
print("Livres disponibles après suppression :", library.available_books())


