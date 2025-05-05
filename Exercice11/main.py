class BankAccount:
    """
    Classe représentant un compte bancaire.
    """

    def __init__(self, account_holder, balance=0.0):
        """
        Initialise un compte bancaire avec un titulaire et un solde initial.

        Args:
            account_holder (str): Le nom du titulaire du compte.
            balance (float): Le solde initial du compte (par défaut 0.0).
        """
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """
        Dépose de l'argent sur le compte.

        Args:
            amount (float): Le montant à déposer.

        Raises:
            ValueError: Si le montant est négatif.
        """
        if amount < 0:
            raise ValueError("Le montant à déposer doit être positif.")
        self.balance += amount
        print(f"{amount} a été déposé sur le compte.")

    def withdraw(self, amount):
        """
        Retire de l'argent du compte.

        Args:
            amount (float): Le montant à retirer.

        Raises:
            ValueError: Si le montant est négatif ou si le solde est insuffisant.
        """
        if amount < 0:
            raise ValueError("Le montant à retirer doit être positif.")
        if amount > self.balance:
            raise ValueError("Fonds insuffisants pour effectuer ce retrait.")
        self.balance -= amount
        print(f"{amount} a été retiré du compte.")

    def display_balance(self):
        """
        Affiche le solde et le nom du titulaire du compte.
        """
        print(f"Titulaire du compte: {self.account_holder}, Solde: {self.balance}")



# Exemple d'utilisation

# Exemple d'utilisation de la classe BankAccount
account = BankAccount("Alice", 100.0)
account.display_balance()

account.deposit(50.0)
account.display_balance()

try:
    account.withdraw(200.0)
except ValueError as e:
    print(e)

account.withdraw(50.0)
account.display_balance()
