import hashlib

# Fonction pour convertir une chaîne de caractères en sa représentation binaire
def string_to_binary(string):
    binary = ""
    for char in string:
        binary += format(ord(char), '08b')
    return binary

# Fonction pour convertir une chaîne de caractères en une séquence ACGT
def string_to_acgt(string):
    acgt = ""
    for char in string:
        binary = format(ord(char), '08b')
        acgt += binary.replace("00", "A").replace("01", "C").replace("10", "G").replace("11", "T")
    return acgt

# Récupération du nom d'utilisateur
username = input("Entrez votre nom d'utilisateur : ")

# Génération du hash de l'utilisateur
hash = hashlib.sha256(username.encode()).hexdigest()

# Conversion du hash en binaire puis en ACGT
binary_hash = string_to_binary(hash)
acgt_hash = string_to_acgt(binary_hash)

# Brin d'ADN commun en ASCII
tux_dna = '''
                 .88888888:.
                88888888.88888.
              .8888888888888888.
              888888888888888888
              88' _`88'_  `88888
              88 88 88 88  88888
              88_88_::_88_:88888
              88:::,::,:::::8888
              88`:::::::::'`8888
             .88  `::::'    8:88.
            8888            `8:888.
          .8888'             `888888.
         .8888:..  .::.  ...:'8888888:.    Welcome to CryptoDraw ;)
        .8888.'     :'     `'::`88:88888
       .8888        '         `.888:8888.
      888:8         .           888:88888
    .888:88        .:           888:88888:
    8888888.       ::           88:888888
    `.::.888.      ::          .88888888
   .::::::.888.    ::         :::`8888'.:.
  ::::::::::.888   '         .::::::::::::
  ::::::::::::.8    '      .:8::::::::::::.
 .::::::::::::::.        .:888:::::::::::::
 :::::::::::::::88:.__..:88888:::::::::::'
  `'.:::::::::::88888888888.88:::::::::'
        `':::_:' -- '' -'-' `':_::::'`
'''

# Ajout du hash de l'utilisateur dans le Tux ASCII
acgt_tux_dna = tux_dna[:-1] + acgt_hash + "\n" + tux_dna[-1]

# Affichage du Tux ASCII avec le hash de l'utilisateur
print(acgt_tux_dna)

