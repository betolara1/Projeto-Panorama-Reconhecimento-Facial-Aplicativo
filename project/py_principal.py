from kivy.uix.screenmanager import Screen
from py_cadastro import *
import os
from script.training import *

class TPrincipal(Screen):
    title = 'SISTEMA'
    icon = '/assets/ImagesApp/logo.png'
    
    def eigen(self):
        os.system('python project/script/eigen.py')
