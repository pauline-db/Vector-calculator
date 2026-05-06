''' Canvas de la semestrielle de l'OC d'informatique qui est à  rendre 
    avant le 10 janvier 2021 minuit '''

    
''' ----------------------------------------------------------------------- '''
''' ------------------ Debut Partie Fonctions ----------------------------- '''
''' ----------------------------------------------------------------------- '''

'''1 Demander à l'utilisateur de rentrer un vecteur '''
def get_vecteur(nom_vecteur="u"):
    ''' nom_vecteur(str) : le nom du vecteur à afficher '''
    u = [0 for i in range(DIM)] #créer un vecteur vide
    for i in range(DIM):
        x = input("Quelle est la composante "+str(i+1)+" du vecteur " + str(nom_vecteur) + " : ")
        while not x.isdecimal(): #permet de vérifier que l'utilsateur entre des composantes décimales.
          print("composante invalide, réessayer")
          x = input("Quelle est la composante "+str(i+1)+" du vecteur " + nom_vecteur + " : ")
        u[i]=float(x)

    
    return u

'''2 Afficher le vecteur '''
def print_vecteur(u):
    msg = "("
    #créer un début de chaine de charactère
    for c in u:
        msg = msg +str(c) + "; "
    print(msg[:-2]+")")

'''3 Additionne les vecteur a et b '''
def add_vecteur(a, b):
    v = [0 for i in range(DIM)]
    # créer un vecteur vide 
    for i in range(DIM):
        v[i] = a[i] + b[i] #la ième composante du vecteur v est obtenu en additionnant la ième composante du vecteur a avec celle du vecteur b
    
    return v


'''4 Soustraire le vecteur b au vecteur a '''
def  substract_vecteur(a, b):
    v = [0 for i in range(DIM)]
    # créer un vecteur vide 
    for i in range(DIM):
        v[i] = a[i] - b[i] #la ième composante du vecteur v est obtenu en soustrayant la ième composante du vecteur a avec celle du vecteur b

    return v

'''5 multiplier le vecteur par un nombre'''
def multiply_vecteur(a):
  v = [0 for i in range(DIM)]
    # créer un vecteur vide 
  b= input('Par quel nombre voulez vous multiplier votre vecteur ? \n')
  while not b.isdecimal(): #permet de vérifier que l'utilisateur ne rentre qu'un chiffre décimal appartenant à ℝ
    print("nombre invalide, réessayer")
    b= input('Par quel nombre voulez vous multiplier votre vecteur ? \n')
  t=float(b)
  for i in range(DIM):
        v[i] = a[i] *  t # t multiplie la ième composante du vecteur a pour donner la ième composante du vecteur v

  return v

'''6 produit scalaire des vecteurs a et b '''
def produit_scalaire(a, b):
    v=0
    for i in range(DIM):
      v=a[i] * b[i] + v # v (le produit scalaire) est soumis à une boucle et est obtenu en multipliant symétriquement les ièmes composantes des vecteurs a et b puis en additionnant la précédente valeur de v.
    return v

'''7 norme du vecteur a '''
def norme(a):
    v=0
    for i in range(DIM): # v (la norme) dépend d'une boucle et prend la valeur de la ième composante du vecteur a élevé au carré additionné à la précédente valeur de v.
      v = a[i]**2 + v
    v = v**0.5

    return v

'''8 normalisé du vecteur a '''
def normalise(a):
    z=norme(a) #appel à une fonction réalisée précédemment

    n = list(range(DIM))
    if all(a[l]==0 for l in n): #permet de s'assurer que l'utilisateur n'entre pas un vecteur nul car une division par 0 est impossible.
      v = None 
      print("Le normalisé du vecteur n'existe pas lorsque le vecteur est nul.")
      return v
      
    z = 1/z

    v = [0 for i in range(DIM)]
    # créer un vecteur vide 
    for i in range(DIM):
        v[i] = a[i] * z # z multiplie la ième composante du vecteur a pour donner la ième composante du vecteur v normalisé.

    return v

''' 9 projeté orthogonal du vecteur a sur le vecteur b'''
def projete_orthogonal(a, b):
    count_b=0 #variable pour compter le nombre de composantes égales à 0 dans le vecteur w
    for i in range(DIM):
      if b[i]==0: 
        count_b = count_b +1 #on ajoute 1 au nombre de zero si la composante i est égale à 0
      if count_b==DIM:
        print("Le projeté orthogonal est impossible si le vecteur w est nul.") #si le vecteur w est nul, et donc lorsque toutes les composantes sont nulles, alors le projeté orthogonal est impossible à calculer, il n'existe pas
        v = None #il n'y a donc pas de réponse
        return v

    x= produit_scalaire(a, b) #fait appel à une fonction réalisée précédemment

    y = norme(a) #fait appel à une fonction réalisée précédemment

    z = x/y #rapport entre le produit scalaire et la norme

    v = [0 for i in range(DIM)]
    # créer un vecteur vide 
    for i in range(DIM):
        v[i] = b[i] * z # z multiplie la ième composante du vecteur b pour donner la ième composante du vecteur v.
    
    return v

'''10 angle entre les vecteur a et b '''
from math import acos 
from math import pi
# utilisation du module mathématique pour utiliser π et acos.

def angle_vecteur(a, b):
   
    x= produit_scalaire(a, b) #appel à une fonction réalisée précédemment
    
    y= norme(a) #fait appel à une fonction réalisée précédemment
    
    z= norme(b) #fait appel à une fonction réalisée précédemment
    
    if y==0 or z==0:#permet de vérifier qu'aucun des vecteurs n'est nul car une division par 0 est impossible
      v= None
      print("Impossible de calculer l'angle entre ces deux vecteur si l'un des vecteurs est nul")
      return v
    v = acos(x/(y*z))

    v = (180*v)/pi #convertis en degré le résultat précédent où la fonction acos a retourné une valeur en radians

    return v



'''11 si le vecteur a est unitaire '''
def unitaire(a):
    v= norme(a) #trouve la norme de a en utilisant une fonction crée précédemment

    if v ==1:
      v = True
    #si la norme est égale à 1, le vecteur est unitaire et donc on renvoie la valeur v en booléen comme True
    else:
      v = False
    #le vecteur n'est pas unitaire et on renvoie la valeur v en booléen comme False
    return v
    

'''12 si les vecteurs a et b sont colinéaires '''
def colineaire(a, b):
    zero=[] #liste vide qui contiendra les indexs des composantes qui sont égales à 0

    for h in range (DIM):
      if a[h]==b[h]==0:
        zero.append(h) 
        #ajouter tous les indexs des composantes qui sont égales à 0 dans v et w

    zero.reverse() #inverser la liste pour ne pas changer les indexs précédents au fur et à mesure qu'on enlève des valeurs
    for q in zero:
      a.pop(q)
      b.pop(q)
      #enlever les 0 communs aux deux vecteurs
      
    zero = len(zero)
    n = DIM -  zero #nombre de valeurs dans la liste après avoir enlevé les 0 communs
    x = [0 for i in range(n)]

    for t in range (n):
      if b[t]==0:
        v=False
        return v
        # si une composante de w est égale à 0 mais pas celle du vecteur v, alors l'étape suivante (la division) sera impossible donc on peut déjà retourner False qui affichera que les vecteurs ne sont pas colinéaires

      else:
       x[t] = a[t] / b[t] #le rapport de a par rapport à b pour chaque composante

    if all(l==x[0] for l in x):
        v=True
    # si les solutions de toutes les divisions(x) sont égales, alors les vecteurs v et w sont colinéaires
    else:
      v = False

    return v


'''13 si les vecteurs a et b sont orthogonaux '''
def orthogonaux(a, b):
  x= produit_scalaire(a, b) # appel à une fonction réalisée précédemment

  if x == 0: #si le produit scalaire vaut 0 alors les vecteurs a et b sont orthogonaux et on renvoie la valeur x en booléen comme True
    v = True

  else:
    v = False # sinon les vecteurs ne sont pas orthogonaux et on renvoie la valeur v en booléen comme False

  return v

'''14 produit vectoriel des vecteurs a et b '''
def produit_vectoriel(a, b):
    v = [0 for i in range(3)] #créer un vecteur vide
    v[0]= a[1]*b[2] - a[2]*b[1] 
    v[1]= b[0]*a[2] - b[2]*a[0]
    v[2]= a[0]*b[1] - a[1]*b[0]
    # affecter à chaque élément de la liste des composante la valeur trouvée grâce à la formule
    return v


''' ----------------------------------------------------------------------- '''
''' ----------------- Debut Partie code principal-------------------------- '''
''' ----------------------------------------------------------------------- '''

''' DIM est une variable globale qui vaut 2 ou 3 en fonction du nombre de 
    dimensions avec lequel on travaille                                    '''
DIM = int(input("Dans quelle dimension désirez-vous travailler (2 ou 3) ? "))


''' Les variables globales: les listes qui représentes les coefficients des 
vecteurs  '''
if DIM == 2:
    v = [0, 0]
    w = [0, 0]
elif DIM == 3:
    v = [0, 0, 0]
    w = [0, 0, 0]
while DIM!=2 and DIM!=3:
    print("dimension invalide, réessayez")
    DIM = int(input("Dans quelle dimension désirez-vous travailler (2 ou 3) ? "))
    
    
MSG="""\nChoix 1:  Entrer/modifier un des vecteur donnés. \n
Choix 2:  Afficher un des vecteurs.\n
Choix 3:  Additionner les vecteurs v et w et afficher le résultat.\n
Choix 4: Soustraire le vecteur w au vecteur v et afficher le résultat.\n
Choix 5: Demander un nombre à l'utilisateur, puis  effectuer la multiplication d'un des vecteurs par ce nombre et afficher le résultat.\n
Choix 6: Calculer le produit scalaire v · w et afficher le résultat.\n
Choix 7: Calculer la norme d'un des vecteurs et afficher le résultat.\n
Choix 8: Normaliser un des vecteurs et afficher le résultat.\n
Choix 9: Calculer le projeté orthogonal du vecteur v sur le vecteur w et afficher le résultat.\n
Choix 10: Calculer l'angle (compris entre 0◦et 180◦) entre les vecteurs v et w et afficher le résultat.\n
Choix 11: Afficher si un vecteur est unitaire ou non.\n
Choix 12: Afficher si les vecteurs v et w sont colinéaires ou non.\n
Choix 13: Afficher si les vecteurs v et w sont orthogonaux ou non.\n
Choix 14: Calculer le produit vectoriel v × w et afficher le résultat (seulement pour les vecteurs de dimension 3) \n
Choix 15: Quitter le programme \n"""



print("\n\n\n")
while True:
   print(MSG)
   
   choix = input("Entrez votre choix:")
   
   while not choix.isdecimal(): # vérifie que l'utilsateur entre un chiffre décimal
     print("Entrée invalide, entrez un nombre de 1 à 15.")
     choix = input("Entrez votre choix:")
   
   t=int(choix)
   while not t>=1 or not t<=15: #vérifie que l'utilsateur entre un chiffre entre 1 et 15 compris.
     print("Entrée invalide, entrez un nombre de 1 à 15.")
     choix = input("Entrez votre choix:")
     t=int(choix)
   
   if choix == "1":
      choix_vecteur = input("Quel vecteur voulez-vous modifier [v/w] : ").lower()
      if choix_vecteur == "v":
          v = get_vecteur("v")
          
      elif choix_vecteur == "w":
          w = get_vecteur("w")
          
      else:
          print("Votre choix n'est pas compréhensible, utiliser la lettre 'v' ou 'w'")
          
   elif choix == "2":
      choix_vecteur = input("Quel vecteur voulez-vous afficher [v/w] : ").lower()
      if choix_vecteur == "v":
          print_vecteur(v)
      elif choix_vecteur == "w":
          print_vecteur(w)
      else:
          print("Votre choix n'est pas compréhensible, utiliser la lettre 'v' ou 'w'")
          
   elif choix == "3":
      u = add_vecteur(v, w) #appel à une fonction réalisée précédemment
      print("La somme des deux vecteurs vaut : ")
      print_vecteur(u)
       
   elif choix == "4":
      u = substract_vecteur(v,w) #appel à une fonction réalisée précédemment
      print("La soustraction des deux vecteurs vaut : ")
      print_vecteur(u)
      
   
   elif choix == "5":
    x=input("Quel est le vecteur que vous voulez multiplier par un nombre? (v/w) : ").lower()
    while x!="v" and x!="w": #boucle permettant de s'assurer que l'utilisateur entre les vecteurs v ou w.
      print("entrée invalide, écrivez v ou w")
      x=input("Quel est le vecteur que vous voulez mulltiplier par un nombre? (v/w) : ")
    if x=="v":
      y=v
    if x=="w":
       y=w
    u = multiply_vecteur(y) #appel à une fonction réalisée précédemment
    print("La multiplication du vecteur et du nombre vaut : ")
    print_vecteur(u)
      
  
   elif choix == "6":
      u = produit_scalaire(v,w) #appel à une fonction réalisée précédemment
      print("le produit scalaire des deux vecteurs vaut:")
      print(u)

      
   elif choix == "7":
      x=input("quel est le vecteur dont vous voulez la norme : ").lower()
      while x!="v" and x!="w": #boucle permettant de s'assurer que l'utilisateur entre les vecteurs v ou w.
        print("entrée invalide, écrivez v ou w")
        x=input("quel est le vecteur dont vous voulez la norme : ")
      if x=="v":
        y=v
      if x=="w":
       y=w
      u = norme(y) #appel à une fonction réalisée précédemment
      print(u)

       
   elif choix == "8":
      x=input("quel est le vecteur que vous voulez normaliser : ").lower()
      while x!="v" and x!="w": #boucle permettant de s'assurer que l'utilisateur entre les vecteurs v ou w.
        print("entrée invalide, écrivez v ou w")
        x=input("quel est le vecteur que vous voulez normaliser : ")
      if x=="v":
        y=v
      if x=="w":
       y=w
      u = normalise(y) #appel à une fonction réalisée précédemment
      print("le vecteur normalisé vaut: ")
      print(u)
  
   elif choix == "9":
      u = projete_orthogonal(v,w) #appel à une fonction réalisée précédemment
      print("Le projeté orthogonal de v sur w vaut: ")
      print(u)
    
   elif choix == "10":
      u = angle_vecteur(v, w) #appel à une fonction réalisée précédemment
      print("L'angle entre les deux vecteurs vaut : ")
      print(u, "°")

     
   elif choix == "11":
     x=input("Quel est le vecteur dont vous voulez savoir s'il est unitaire? (v/w) : ").lower()
     while x!="v" and x!="w": #boucle permettant de s'assurer que l'utilisateur entre les vecteurs v ou w.
      print("Entrée invalide, écrivez v ou w.")
      x=input("Quel est le vecteur dont vous voulez savoir s'il est unitaire? (v/w) : ").lower()
     if x=="v":
        y=v
     if x=="w":
       y=w
     u = unitaire(y) #appel à une fonction réalisée précédemment
     if u==True:
       print("Le vecteur est unitaire.")
     elif u==False:
       print("Le vecteur n'est pas unitaire.")
      
   elif choix == "12":
      u = colineaire(v,w) #appel à une fonction réalisée précédemment
      if u:
        print("Les deux vecteurs sont colinéaires.")
      else:
        print("Les deux vecteurs ne sont pas colinéaires.")
   
   elif choix == "13":
      u = orthogonaux(v, w) #appel à une fonction réalisée précédemment
      if u==True:
        print("Les deux vecteurs sont orthogonaux.")
      if u==False:
        print("Les deux vecteurs ne sont pas orthogonaux.")
    
   elif choix == "14" and DIM==3:
      u = produit_vectoriel(v, w) #appel à une fonction réalisée précédemment
      print("Le produit vectoriel de v et w vaut: ")
      print(u)

   elif choix == "14" and DIM==2: #si l'utilisateur choisit de travailler avec une dimension 2, il ne peut pas faire le choix 14.
      print("Choix invalide pour les vecteurs de deuxième dimension.")
      
   elif choix == "15":
     print("Vous avez quitté la calculatrice.")
     break #fin du programme