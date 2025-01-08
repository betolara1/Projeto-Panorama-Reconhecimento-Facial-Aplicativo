# 👤 Projeto Panorama - Reconhecimento Facial

## 📋 Sobre o Projeto

Sistema de reconhecimento facial desenvolvido em Python com interface gráfica em Kivy/KvLang para Windows. O projeto implementa funcionalidades de detecção e reconhecimento facial em tempo real.

## 🚀 Tecnologias Utilizadas

- **Python:** 60.1%
- **KvLang:** 39.9%
- **Banco de Dados:** SQLite
- **Interface Gráfica:** Kivy Framework

## 📁 Estrutura do Projeto
```plaintext
projeto-panorama/
├── assets/            # Recursos e ativos do projeto
├── database/         # Arquivos relacionados ao banco de dados
├── lib/              # Arquivos de biblioteca e dependências
├── project/          # Código-fonte principal do projeto
├── ponto.csv         # Arquivo de pontos de dados
├── requirements.txt  # Dependências do projeto
└── LICENSE.rst       # Arquivo de licença
```


## ⚙️ Pré-requisitos

- Python 3.7+
- Kivy
- OpenCV
- NumPy
- dlib
- face_recognition

## 🔧 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/betolara1/Projeto-Panorama-Reconhecimento-Facial-Aplicativo.git
   cd Projeto-Panorama-Reconhecimento-Facial-Aplicativo
```

2. Crie e ative um ambiente virtual:

```shellscript
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```


3. Instale as dependências:

```shellscript
pip install -r requirements.txt
```




## 💻 Funcionalidades

- Detecção facial em tempo real
- Reconhecimento facial
- Interface gráfica intuitiva
- Armazenamento de dados faciais
- Registro de pontos faciais
- Exportação de dados em CSV


## 🎯 Como Usar

1. Execute o aplicativo principal:

```shellscript
python project/main.py
```


2. Na interface do aplicativo:

1. Selecione a fonte de vídeo (webcam ou arquivo)
2. Aguarde a detecção facial
3. Siga as instruções na tela para cadastro/reconhecimento





## 📊 Pontos Faciais

O sistema utiliza o arquivo `ponto.csv` para armazenar os pontos faciais detectados. A estrutura do arquivo inclui:

- Coordenadas dos pontos faciais
- Timestamps
- Identificadores únicos


## 🔒 Segurança

- Os dados faciais são armazenados localmente
- Não há envio de dados para servidores externos
- Recomenda-se backup regular do banco de dados


## 🤝 Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas alterações (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request


## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE.rst` para mais detalhes.

## ⚠️ Requisitos de Sistema

- Sistema Operacional: Windows 7 ou superior
- Memória RAM: 4GB ou superior
- Webcam (para captura em tempo real)
- Processador: Intel Core i3 ou superior


## 🔍 Troubleshooting

Se encontrar problemas:

1. Verifique se todas as dependências estão instaladas
2. Confirme se sua webcam está funcionando corretamente
3. Verifique as permissões de acesso à câmera
4. Consulte os logs de erro em `project/logs`


## 👤 Autor

- GitHub: [@betolara1](https://github.com/betolara1)


## 📞 Suporte

Para suporte:

- Abra uma issue no GitHub
- Consulte a documentação em `docs/`
- Entre em contato com o desenvolvedor


---

⭐️ Se este projeto te ajudou, considere dar uma estrela no GitHub!
