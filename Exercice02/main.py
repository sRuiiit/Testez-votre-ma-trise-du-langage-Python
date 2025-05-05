# Dictionnaire contenant les informations des étudiants et leurs notes
etudiants = {
    "Alice": {"Mathématiques": 15, "Physique": 14, "Chimie": 16},
    "Bob": {"Mathématiques": 12, "Physique": 10, "Chimie": 11},
    "Charlie": {"Mathématiques": 18, "Physique": 17, "Chimie": 19}
}

# Demander le nom de l'étudiant
nom_etudiant = input("Entrez le nom de l’étudiant :  ")

# Vérifier si l'étudiant existe dans le dictionnaire
if nom_etudiant in etudiants:
    print(f"Notes de {nom_etudiant} :")
    notes = etudiants[nom_etudiant]
    total_notes = 0
    for matiere, note in notes.items():
        print(f"{matiere} : {note}")
        total_notes += note
    moyenne = total_notes / len(notes)
    print(f"Moyenne de {nom_etudiant} : {moyenne:.2f}")
else:
    print(f"L'étudiant {nom_etudiant} n'existe pas dans la liste.")
