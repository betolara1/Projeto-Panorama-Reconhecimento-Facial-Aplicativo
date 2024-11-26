from py_cadastro import TCadastro
from py_principal import TPrincipal
from kivy.uix.screenmanager import ScreenManager
from kivy.app import App
from kivy import Config
from kivy.lang import Builder

#---CONFIGURAÇÃO DAS TELAS GRAFICAS---#
Config.set('graphics', 'resizable', True)
Config.set('kivy', 'exit_on_escape', '0')
Config.set('graphics', 'window_state', 'maximized')
'''Config.set('graphics', 'width', 1000)
Config.set('graphics', 'height', 600)'''

#---GERENCIA TODAS AS TELAS QUE VÃO APARECER---#
class GerenciadorTelas(ScreenManager):
    def __init__(self):
        super().__init__()
        self.tprincipal = TPrincipal()
        self.tcadastro = TCadastro()
        
        self.add_widget(self.tprincipal)
        self.add_widget(self.tcadastro)

class Kv_Main(App):

    title = 'Projeto Panorama'
    icon = '/assets/ImagesApp/logo.png'

    def build(self):
        Builder.load_file('kv_main.kv')
        return GerenciadorTelas()


if __name__ == '__main__':
    Kv_Main().run()
