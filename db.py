import sqlite3 as sql
import auth
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / 'base_de_dados.db'

with sql.connect(DB_PATH) as conn:
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            user_name TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL           
        );
        """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS session (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE NOT NULL,
            remember_me INTEGER NOT NULL
        )
        """)


def cadastrar_usuário(name, user_name, email, senha):
    with sql.connect(DB_PATH) as conn:
        cur = conn.cursor()
        pw_b = senha.encode('utf-8')
        h_str = auth.pw_hash(pw_b)
        try:
            cur.execute('INSERT INTO users (name, user_name, email, password_hash) VALUES (?, ?, ?, ?)', (name, user_name, email, h_str))
            conn.commit()
        except sql.IntegrityError:
            return False
        else:
            return True


def login(user_name, password):
    with sql.connect(DB_PATH) as conn:
        cur = conn.cursor()
        errors = list()
        password_b = password.encode('utf-8')
        cur.execute('SELECT password_hash FROM users WHERE user_name = ?', (user_name,))
        h_pw = cur.fetchone()
        if h_pw == None: 
            errors.append('incorrect_username')
            return errors
        else:
            t_f = auth.verificar_pw(password_b, h_pw[0])
            if t_f == False:
                errors.append('incorrect_password')
            return errors


def remember_me(user_name):
    with sql.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT id FROM users WHERE user_name = ?", (user_name,))
        ID = cur.fetchone()
        cur.execute("INSERT OR REPLACE INTO session (user_id, remember_me) VALUES (?, ?)", (ID[0], 1))
        conn.commit()


def check_remember_me():
    with sql.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT remember_me FROM session;")
        T_or_F = cur.fetchone()
        if T_or_F is None:
            return False
        else:
            if T_or_F[0] == 1:
                return True
            else:
                return False


def clear_session():
    with sql.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM session;")
        conn.commit()