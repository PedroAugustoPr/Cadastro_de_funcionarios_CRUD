import customtkinter as ctk

def TelaPrincipal(function, container, app):
    frame1 = ctk.CTkFrame(container, width=680, height=440, corner_radius=10, fg_color='black')
    frame1.place(relx=0.5, rely=0.5, anchor='center')
    frame1.grid_propagate(False)

    frame1.grid_columnconfigure(0, weight=1)

    txt1 = ctk.CTkLabel(frame1, font=('Roboto', 50), text='HOME')
    txt1.grid(row=0, column=0, pady=(0, 220))

    error_txt1 = ctk.CTkLabel(frame1, font=('Roboto', 14), text='', text_color='red')
    error_txt1.grid(row=0, column=0, pady=(0, 155))

    return frame1