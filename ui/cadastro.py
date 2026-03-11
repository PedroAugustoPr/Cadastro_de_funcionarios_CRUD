import customtkinter as ctk
import db
from ui import service
from pathlib import Path
from PIL import Image
import auth
from ui import login


def TelaCadastro(function, container):
    a_t = ctk.BooleanVar(value=False)
    
    def cadastrar_se():
        name = zone1.get()
        user_name = zone2.get()
        email = zone3.get()
        senha = zone4.get()
        
        z = a_t.get()
        
        v = auth.validar_cadastro(email, user_name, senha, error_txt1, zone2, zone3, zone4)
        if v:
            if z:
                x = db.cadastrar_usuário(name, user_name.strip(), email.strip(), senha.strip())
                if x:
                    function('fazer-login')
                else:
                    service.U_or_E_Alredy_Used(error_txt1, zone2, zone3, True)
            else:
                service.Dont_Accept_T(error_txt1, cbx1, V=True)

    
    def Hide_Patterns(function):
        function('fazer-login')

        login.frame.destroy()


    IMG_PATH = Path(__file__).resolve().parent

    frame1 = ctk.CTkFrame(container, width=680, height=440, corner_radius=20, fg_color='black')
    frame1.place(relx=0.5, rely=0.5, anchor='center')
    frame1.grid_propagate(False)
    frame1.grid_columnconfigure(0, weight=1)

    txt_pill = Image.open(IMG_PATH / 'images' / 'cadastro_text.png')
    img_txt = ctk.CTkImage(light_image=txt_pill, dark_image=txt_pill, size=(400, 200))
    img_txt_label = ctk.CTkLabel(frame1, image=img_txt, text='')
    img_txt_label.grid(row=0, column=0, pady=(0, 280))

    error_txt1 = ctk.CTkLabel(frame1, font=('Roboto', 14), text='', text_color='red')
    error_txt1.grid(row=0, column=0, pady=(0, 155))

    zone1 = ctk.CTkEntry(frame1, width=400, height=25, placeholder_text='Nome')
    zone1.grid(row=0, column=0, pady=(0, 100))

    zone2 = ctk.CTkEntry(frame1, width=400, height=25, placeholder_text='Nome de Usuário')
    zone2.grid(row=0, column=0, pady=(20, 0))

    zone3 = ctk.CTkEntry(frame1, width=400, height=25, placeholder_text='E-mail')
    zone3.grid(row=0, column=0, pady=(0, 40))

    zone4 = ctk.CTkEntry(frame1, width=400, height=25, placeholder_text='Senha', show='*')
    zone4.grid(row=0, column=0, pady=(80, 0))

    btn1 = ctk.CTkButton(frame1, width=400, height=40, text='Cadastrar-se', corner_radius=10, command=lambda: cadastrar_se())
    btn1.grid(row=0, column=0, pady=(150, 0))

    cbx1 = ctk.CTkCheckBox(frame1, width=20, height=20, text='Você concorda com os termos?', fg_color='009DFF', variable=a_t)
    cbx1.grid(row=0, column=0, pady=(240, 0))

    txt2 = ctk.CTkLabel(frame1, font=('Roboto', 12), text='Você já possui um cadastro ativo?')
    txt2.grid(row=0, column=0, pady=(300, 0), padx=(0, 40))

    btn2 = ctk.CTkButton(frame1, width=30, height=10, text='Entrar', command=lambda: Hide_Patterns(function))
    btn2.grid(row=0, column=0, pady=(300, 0), padx=(210, 0))

    return frame1