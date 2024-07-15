# Foction qui prend en para une liste et retourn une nouvelle liste
# contenant que les nobres pairs

import streamlit as st

def filter_even_numbers(L) :
    M = []
    for nb in L :
        if nb % 2 == 0 :
            M.append(nb)
    return M

nombres_entrees = st.text_input("Entrez une liste de nombres séparés par une virgule: ")
Liste = []
if st.button("Terminer"):
    Liste = [float(i) for i in nombres_entrees.split(',')]
st.write("Votre nouvelle liste est :",filter_even_numbers(Liste))


