import customtkinter as ctk


def U_or_E_Alredy_Used(error_txt1, camp1, camp2, V):
    if V:  
        camp1.configure(fg_color='red', placeholder_text_color='black')
        camp2.configure(fg_color='red', placeholder_text_color='black')
        error_txt1.configure(text='Você inseriu um nome de usuário ou email já cadastrados.')


def Username_Dont_Exist(error_txt1, camp1, V):
    if V:
        camp1.configure(fg_color='red', placeholder_text_color='black')
        error_txt1.configure(text='Você inseriu um nome de usuário inválido!')


def Incorrect_Password(error_txt1, camp2, V):
    if V:
        camp2.configure(fg_color='red', placeholder_text_color='black')
        error_txt1.configure(text='Você inseriu uma senha incorreta!')


def Dont_Accept_T(error_txt1, camp2, V):
    if V:
        camp2.configure(fg_color='red', text_color='red', border_color='red')
        error_txt1.configure(text='Você precisa aceitar os termos primeiro!')
