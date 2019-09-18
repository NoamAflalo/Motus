from random import randint


## q.1 Lmots

Lmots=["metisse","solidarite","partage","travail","musique","festif","vacances","etudier","programmes","annees"]


## q.2 fonction ChoixAlea

def ChoixAlea(liste):
    x=randint(0,(len(liste)-1))
    return liste[x]


## q.3 fonction Valide

def Valide(ch,k):
    c=ch.lower()
    p=0
    for i in range (len(ch)):
        if ch[i]==c[i]:
            p+=1
    if p==k:
        return True
    else:
        return False


## q.4 fonction Compare

def Compare(motADeviner,motPropose):
    c=""
    for i in range (len(motADeviner)):
        if motADeviner[i]==motPropose[i]:
            c=c+motADeviner[i]
        else:
            c=c+"*"
    return c

    
## q.5 fonction booléenne Essai

def Essai(n,motADeviner):
    c="Veuillez entrer un mot de " + str(len(motADeviner)) + " lettres en minuscules : "
    motPropose=input(c)
    V=Valide(motPropose,len(motADeviner))
    while V!=True:
        c="Le mot rentré ne respecte pas les critères, veuillez en rentrer un nouveau écrit en minuscule et de longueur " + str(len(motADeviner)) + " lettres : "
        motPropose=input(c)
        V=Valide(motPropose,len(motADeviner))
    reponse= Compare(motADeviner,motPropose)
    print(reponse)
    if reponse == motADeviner:
        return True
    else:
        return False


## q.7 lit le fichier Dico

def LireDico():
    f=open("mots.txt","r")
    L=[]
    s=f.readline()
    while s!="" :
        s=s.replace("\n","")
        if len(s)>=6 and len (s)<=10:
            for i in range(len(s)):
                x=0
                if s[i]=="-":
                    x+=1
            if x==0:
                L.append(s)
        s=f.readline()
    return L
    
    
## q.8 et q.6 exécution des fonctions

print("Vous allez jouer au jeu Motus ! L'ordinateur va choisir un mot de longueur comprise entre 6 et 10 lettres.", "\n\n")
rejoue="oui"
while rejoue == "oui":
    niveau = input("Quel niveau de difficulté souhaitez-vous (facile/difficile) ? ")

    if niveau == "facile":

        mot=ChoixAlea(Lmots)
        n=len(mot)
        k=0
        c="Vous avez "+str(n)+" essais."+"\n"
        print(c)
        reponse=Essai(n,mot)
        k+=1
        n-=1

        while reponse != True and n>0:
            c="il vous reste "+str(n)+" essais."+"\n"
            print(c)
            reponse=Essai(n,mot)
            k+=1
            n-=1

        if reponse == True:
            print("Bravo, vous avez réussi ! Vous avez utilisé ", k, " essais.","\n")
        else:
            print("Désolé, vous n'avez plus d'essais, le mot était : ",mot,"\n")


    else:

        liste=LireDico()
        mot=ChoixAlea(liste)
        n=len(mot)
        k=0
        c="Vous avez "+str(n)+" essais."+"\n"
        print(c)
        reponse=Essai(n,mot)
        k+=1
        n-=1

        while reponse != True and n>0:
            c="il vous reste "+str(n)+" essais."+"\n"
            print(c)
            reponse=Essai(n,mot)
            k+=1
            n-=1

        if reponse == True:
            print("Bravo, vous avez réussi ! Vous avez utilisé ", k, " essais.","\n")
        else:
            print("Désolé, vous n'avez plus d'essais, le mot était : ",mot,"\n")

    rejoue=input("Voulez-vous refaire une partie (oui/non) ?")
