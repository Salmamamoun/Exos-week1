# Fonction qui prend en compte une matrice et et retourne 
# une liste contenant la somme de chaque ligne

import streamlit as st
def sum_matrix_rows(Matrice) :
    L = [] # Liste contenant la somme de chaque ligne de Matrice
    for ligne in Matrice :
        somme = 0
        for nb in ligne :
            somme += nb
        L.append(somme)
    return L 

# on aura une matrice composée que de 2 lignes 
ligne1 = st.text_input("Entrez la 1ère ligne de votre matrice (exp: 1,2,3) :")
ligne2 = st.text_input("Entrez la 2ème ligne de votre matrice (exp: 1,2,3) :")
Liste1 = []
Liste2 = []

if st.button("Terminer"):
    Liste1 = [float(i) for i in ligne1.split(',')]
    Liste2 = [float(i) for i in ligne2.split(',')]
    L = [Liste1,Liste2]
    st.write("Votre nouvelle liste est :",sum_matrix_rows(L))



        


