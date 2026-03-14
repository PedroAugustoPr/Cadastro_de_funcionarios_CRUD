import bcrypt as bc
from email_validator import validate_email, EmailNotValidError


# Oculta a mensagem de erro e volta a cor do campo de entrada para a sua cor original.
def hide_errors(error_txt, camp, old_color, old_ctxt):
        camp.configure(fg_color=old_color, placeholder_text_color=old_ctxt)
        error_txt.configure(text='')


# Exibe uma mensagem de erro e muda as cores dos campos de entrada incorretos para vermelho.
def show_errors(error_txt, camp, label_text):
    old_c = camp.cget('fg_color')
    old_ctxt = camp.cget('placeholder_text_color')
    camp.configure(fg_color='red', placeholder_text_color='black')
    error_txt.configure(text=label_text)
    camp.after(5000, lambda: hide_errors(error_txt, camp, old_c, old_ctxt))


# Valida ou invalida o cadastro do usuário. Essa função é chamada exclusivamente pelo arquivo "cadastro.py".
def validar_cadastro(email, user_name, password, error_txt, camp1, camp2, camp3, camp4):
    Have_Letter = any(c.isalpha() for c in password)
    Have_Number = any(c.isdigit() for c in password)
    Have_SpecialS = any(not c.isalnum() for c in password)
    Have_UpperL = any(c.isupper() for c in password)
    Have_LowerL = any(c.islower() for c in password)
    
    
    #   SESSION : WITHOUT ANSWERS
    def without_answers(error_txt, *camp):
        for c in range(0, 4):
            old_c = camp[c].cget('fg_color')
            old_ctxt = camp[c].cget('placeholder_text_color')
            camp[c].configure(fg_color='red', placeholder_text_color='black')
            error_txt.configure(text='Você precisa preencher todos os campos!')
            camp[c].after(5000, lambda zone = camp[c], old_color = old_c, old_color_txt = old_ctxt: hide_errors(error_txt, zone, old_color, old_color_txt))
    
    
    if not email.strip() or not password.strip() or not user_name.strip():
        without_answers(error_txt, camp1, camp2, camp3, camp4)
        return False
    
    #   SESSION : USER_NAME
    if len(user_name) < 4:
        show_errors(error_txt, camp2, 'Você inseriu um nome de usuário muito curto!')
        return False
    
    #   SESSION : PASSWORD
    if len(password) < 8:
        show_errors(error_txt, camp4, 'Você inseriu uma senha muito curta!')
        return False
    
    elif len(password) > 30:
        show_errors(error_txt, camp4, 'Você inseriu uma senha muito grande!')
        return False
    
    elif not Have_Letter:
        show_errors(error_txt, camp4, 'A senha precisa conter pelo menos uma letra!')
        return False
    
    elif not Have_Number:
        show_errors(error_txt, camp4, 'A senha precisa conter pelo menos um número!')
        return False
    
    elif not Have_SpecialS:
        show_errors(error_txt, camp4, 'A senha precisa conter pelo menos um caractere especial!')
        return False
    
    elif not Have_UpperL:
        show_errors(error_txt, camp4, 'A senha precisa conter pelo menos uma letra maiúscula!')
        return False
    
    elif not Have_LowerL:
        show_errors(error_txt, camp4, 'A senha precisa conter pelo menos uma letra minúscula!')
        return False
    
    #   SESSION : E-MAIL
    try:
        validate_email(email, check_deliverability=True)
    except EmailNotValidError:
        show_errors(error_txt, camp3, 'Você inseriu um e-mail inválido!')
        return False
    else:
        return True


# Transforma a senha já encriptada (em bytes) em um hash. Essa função é chamada exclusivamente pelo arquivo "db.py".
def pw_hash(pw_b):
    h = bc.hashpw(pw_b, bc.gensalt(12))
    h_str = h.decode('utf-8')
    return h_str


# Verifica a senha inserida pelo usuário na parte do login (com a senha já encriptada) e a compara com a "hashed_password", senha em formato "hash" armazenada no arquivo "base_de_dados.db"
def verificar_pw(password_b, hashed_password):
    if isinstance(hashed_password, bytes):
        t_f = bc.checkpw(password_b, hashed_password)
        return t_f
    else:
        h_pw_b = hashed_password.encode('utf-8')
        t_f = bc.checkpw(password_b, h_pw_b)
        return t_f