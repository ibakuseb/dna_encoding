import hashlib

# Demander le mot de passe à l'utilisateur
password = input("Entrez votre mot de passe : ")

# Hasher le mot de passe en utilisant l'algorithme SHA256
hashed_password = hashlib.sha256(password.encode()).hexdigest()

# Afficher le mot de passe hashé
print("Votre mot de passe hashé en utilisant SHA256 est :", hashed_password)

