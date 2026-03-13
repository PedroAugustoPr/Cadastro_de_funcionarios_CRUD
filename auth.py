import bcrypt as bc
from email_validator import validate_email, EmailNotValidError

def hide_errors(error_txt, camp, old_color, old_ctxt):
        camp.configure(fg_color=old_color, placeholder_text_color=old_ctxt)
        error_txt.configure(text='')


def show_errors(error_txt, camp, label_text):
    global show_all_errors
    def show_all_errors(error_txt, camp2, camp3, camp4, label_text):
        camp = list()
        camp.append(camp2)
        camp.append(camp3)
        camp.append(camp4)

        for c in range(0, 3):
            old_c = camp[c].cget('fg_color')
            old_ctxt = camp[c].cget('placeholder_text_color')
            camp[c].configure(fg_color='red', placeholder_text_color='black')
            error_txt.configure(text=label_text)
            camp[c].after(5000, lambda: hide_errors(error_txt, camp, old_c, old_ctxt))
    
    old_c = camp.cget('fg_color')
    old_ctxt = camp.cget('placeholder_text_color')
    camp.configure(fg_color='red', placeholder_text_color='black')
    error_txt.configure(text=label_text)
    camp.after(5000, lambda: hide_errors(error_txt, camp, old_c, old_ctxt))


def validar_cadastro(email, user_name, password, error_txt, camp2, camp3, camp4):
    Have_Letter = any(c.isalpha() for c in password)
    Have_Number = any(c.isdigit() for c in password)
    Have_SpecialS = any(not c.isalnum() for c in password)
    Have_UpperL = any(c.isupper for c in password)
    Have_LowerL = any(c.islower() for c in password)

    #   SESSION : USER_NAME
    if len(user_name) < 4:
        show_errors(error_txt, camp2, 'Você inseriu um nome de usuário muito curto!')
        return False
    
    #   SESSION : NOT ANSWERS
    if not email and not password and not user_name:
        show_all_errors(error_txt, camp2, camp3, camp4, 'Você precisa responder a todos os campos!')
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


def pw_hash(pw_b):
    h = bc.hashpw(pw_b, bc.gensalt(12))
    h_str = h.decode('utf-8')
    return h_str


def verificar_pw(password_b, hashed_password):
    if isinstance(hashed_password, bytes):
        t_f = bc.checkpw(password_b, hashed_password)
        return t_f
    else:
        h_pw_b = hashed_password.encode('utf-8')
        t_f = bc.checkpw(password_b, h_pw_b)
        return t_f