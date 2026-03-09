import bcrypt as bc
from email_validator import validate_email, EmailNotValidError

def hide_errors(error_txt, camp, old_color):
        camp.configure(fg_color=old_color, placeholder_text_color='white')
        error_txt.configure(text='')


def show_errors(error_txt, camp, label_text):
    old_c = camp.cget('fg_color')
    camp.configure(fg_color='red', placeholder_text_color='black')
    error_txt.configure(text=label_text)
    camp.after(5000, lambda: hide_errors(error_txt, camp, old_c))


def validar_cadastro(email, user_name, password, error_txt, camp2, camp3, camp4):
    if len(user_name) < 4:
        show_errors(error_txt, camp2, 'Você inseriu um nome de usuário muito curto!')
        return False
    elif len(password) < 8:
        show_errors(error_txt, camp4, 'Você inseriu uma formatação de senha inválida!')
        return False
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