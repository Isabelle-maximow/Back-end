import streamlit as st
from _controllers._usuario_controller import criar_usuario, listar_usuario

st.title("Sistema Usuarios MVC (ORM + PY + ST)")

#FORMULARIO:
st.subheader("Adicionar Usuario")
nome = st.text_input("Nome: ")
email = st.text_input("E-mail: ")

if st.button ("Salvar usuário"):
    criar_usuario(nome, email)
    st.sucess("Usuario Cadastrado.")

# listar usuario:
st.subheader("Usuarios cadastrados: ")
usuario = listar_usuario()
for i in usuario:
    st.writte(f"ID: {i.id} NOME: {i.nome} E-MAIL: {i.email}")