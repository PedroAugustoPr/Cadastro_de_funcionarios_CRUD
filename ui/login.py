import customtkinter as ctk
import db
from ui import service
from PIL import Image
from pathlib import Path


def TelaLogin(function, container):
    # "l_a" = "Login automático".
    l_a = ctk.BooleanVar(value=False)
    
    # Verifica se as informações de login informadas pelo usuário são verdadeiras.
    def fazer_login():
        user_name = zone1.get()
        password = zone2.get()
        x = l_a.get()
        y = db.login(user_name, password)
        if len(y) == 0:
            function('home')
            if x:
                db.remember_me(user_name)
            else:
                db.clear_session()
        else:
            if y[0] == 'incorrect_username':
                service.Username_Dont_Exist(error_txt1, zone1, V=True)
            else:
                service.Incorrect_Password(error_txt1, zone2, V=True)
    
    
    # SESSION : UI
    frame1 = ctk.CTkFrame(container, width=680, height=440, corner_radius=20, fg_color='black')
    frame1.place(relx=0.5, rely=0.5, anchor='center')
    frame1.grid_propagate(False)

    frame1.grid_columnconfigure(0, weight=1)
    
    UI_PATH = Path(__file__).resolve().parent

    bg_pil = Image.open(UI_PATH / 'images' / 'login_bg.png')
    bg_image = ctk.CTkImage(light_image=bg_pil, dark_image=bg_pil, size=(1920, 1080))

    bg_label = ctk.CTkLabel(container, image=bg_image, text='')
    bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    txt_pill = Image.open(UI_PATH / 'images' / 'login_text.png')
    img_txt = ctk.CTkImage(light_image=txt_pill, dark_image=txt_pill, size=(400, 200))

    img_txt_label1 = ctk.CTkLabel(frame1, image=img_txt, text='')
    img_txt_label1.grid(row=0, column=0, pady=(0, 270))

    error_txt1 = ctk.CTkLabel(frame1, font=('Roboto', 14), text='', text_color='red')
    error_txt1.grid(row=0, column=0, pady=(0, 140))

    zone1 = ctk.CTkEntry(frame1, width=400, height=40, placeholder_text='Nome de Usuário')
    zone1.grid(row=0, column=0, pady=(0, 70))

    zone2 = ctk.CTkEntry(frame1, width=400, height=40, placeholder_text='Senha', show='*')
    zone2.grid(row=0, column=0, pady=(40, 0))

    btn1 = ctk.CTkButton(frame1, width=400, height=40, text='Entrar', corner_radius=10, command=lambda: fazer_login())
    btn1.grid(row=0, column=0, pady=(150, 0))

    cbx1 = ctk.CTkCheckBox(frame1, width=20, height=20, text='Efetuar o login automaticamente.', fg_color='009DFF', variable=l_a)
    cbx1.grid(row=0, column=0, pady=(240, 0))

    txt2 = ctk.CTkLabel(frame1, font=('Roboto', 12), text='Você ainda não possui um cadastro ativo?')
    txt2.grid(row=0, column=0, pady=(300, 0), padx=(0, 90))

    btn2 = ctk.CTkButton(frame1, width=30, height=10, text='Cadastrar-se', command=lambda: function('cadastrar-se'))
    btn2.grid(row=0, column=0, pady=(300, 0), padx=(240, 0))

    frame_box1 = ctk.CTkFrame(frame1, width=400, height=90, corner_radius=15, fg_color="#414446")

    return frame1