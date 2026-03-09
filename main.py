import customtkinter as ctk
from ui import start, cadastro, login, home
import db

frames = dict()

def ExibirFrame(frame):
    print(frame)
    next_frame = frames[frame]
    next_frame.tkraise()

ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.title('')
app.geometry('1920x1080')
app.minsize(width=700, height=450)

app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

container = ctk.CTkFrame(app, fg_color="#009DFF")
container.grid(row=0, column=0, sticky='nsew')

frames['fazer-login'] = login.TelaLogin(ExibirFrame, container)
frames['cadastrar-se'] = cadastro.TelaCadastro(ExibirFrame, container)
frames['home'] = home.TelaPrincipal(ExibirFrame, container, app)

ExibirFrame('fazer-login')

IsTrueOrFalse = db.check_remember_me()


app.mainloop()
