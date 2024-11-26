from kivy.app import App
from kivy.uix.screenmanager import Screen
from script.db import *
from script.detection import *
from script.training import *

import sys
import os

# Add the project directory to the Python path
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_dir)

class TCadastro(Screen):
    def __init__(self, **kwargs):
        super(TCadastro, self).__init__(**kwargs)
        self.blank_user_id = None

    def on_enter(self):
        self.create_blank_user()

    def create_blank_user(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuario (nome, telefone, endereco, cidade) VALUES ('', '', '', '')")
            self.blank_user_id = cursor.lastrowid
            conn.commit()
            conn.close()
            print(f"Blank user created with ID: {self.blank_user_id}")
        except Exception as e:
            print(f"Error creating blank user: {e}")

    def register_foto(self):
        if self.blank_user_id is not None:
            try:
                captura(self.blank_user_id)
            except Exception as e:
                print(f"Error capturing photos: {e}")
        else:
            print("Error: No blank user created. Cannot register photos.")

    def register_data(self):
        self.txt_login = self.ids.login.text
        self.txt_telefone = self.ids.telefone.text
        self.txt_endereco = self.ids.endereco.text
        self.txt_cidade = self.ids.cidade.text

    def insert_values_in_dabatase(self):
        self.register_data()
        
        if not all([self.txt_login, self.txt_telefone, self.txt_endereco, self.txt_cidade]):
            self.ids.login.text = "Os campos não podem ser vazios."
            return

        if self.blank_user_id is None:
            self.ids.login.text = "Erro: Usuário não inicializado."
            return

        try:
            # Conectar ao banco de dados
            conn = get_db_connection()
            cursor = conn.cursor()

            # Atualizar os dados na tabela
            cursor.execute('''
                UPDATE usuario 
                SET nome = %s, telefone = %s, endereco = %s, cidade = %s
                WHERE cod = %s
            ''', (self.txt_login, self.txt_telefone, self.txt_endereco, self.txt_cidade, self.blank_user_id))

            conn.commit()
            conn.close()

            self.clean_input_values()
            self.manager.current = 'tprincipal'
            treinar_reconhecedor()
            
        except Exception as e:
            print(f"Erro ao atualizar no banco de dados: {e}")
            self.ids.login.text = "Erro ao cadastrar. Tente novamente."

    def clean_input_values(self): 
        self.ids.login.text = ''
        self.txt_telefone = ''
        self.txt_endereco = ''
        self.txt_cidade = ''
        self.blank_user_id = None

class LoginApp(App):
    def build(self):
        return TCadastro()

if __name__ == '__main__':
    LoginApp().run()