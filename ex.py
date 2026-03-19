import sys
import os
from PyQt6.QtWidgets import (QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QStackedWidget, QFrame)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class Teste(QFrame):
    def __init__(self, stack):
        super().__init__() 
        self.stack = stack 
        
        # Define o ID da TELA (self) para o QSS
        self.setObjectName("tela1")
        
        # Força o QFrame a aceitar o background do QSS
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1. Texto de Boas-vindas
        self.label_titulo = QLabel('Bem-vindo')
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_titulo.setObjectName("textowelcome")

        # 2. Configuração da Imagem
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Lógica para encontrar o caminho da imagem corretamente
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_imagem = os.path.join(diretorio_atual, "img", "claquete.png")
        
        pixmap = QPixmap(caminho_imagem)
        
        if not pixmap.isNull():
            self.image_label.setPixmap(pixmap.scaled(
                100, 100, 
                Qt.AspectRatioMode.KeepAspectRatio, 
                Qt.TransformationMode.SmoothTransformation
            ))
        else:
            self.image_label.setText("Imagem não encontrada")
            print(f"Erro: Verifique se a imagem existe em: {caminho_imagem}")

        # 3. Botão de entrada
        self.botao = QPushButton('Entrar')
        self.botao.setObjectName("botao_entrar") 
        self.botao.setFixedSize(200, 50) 
        self.botao.clicked.connect(self.irParaHome)

        # ADICIONANDO OS WIDGETS AO LAYOUT (A ordem aqui define a posição na tela)
        layout.addWidget(self.label_titulo)
        layout.addWidget(self.image_label)
        layout.addWidget(self.botao, alignment=Qt.AlignmentFlag.AlignCenter)

    def irParaHome(self):
        self.stack.setCurrentIndex(1)

class Teste2(QWidget):
    def __init__(self):
        super().__init__() 
        self.setObjectName("tela2")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel('Você trocou de tela! (Tela 2)')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter) 

        layout.addWidget(label)

def main():
    app = QApplication(sys.argv)

    # Carregamento do Estilo
    diretorio = os.path.dirname(os.path.abspath(__file__))
    caminho_qss = os.path.join(diretorio, "style.qss")

    try:
        with open(caminho_qss, "r", encoding="utf-8") as file:
            app.setStyleSheet(file.read())
            print("Estilo carregado com sucesso!")
    except FileNotFoundError:
        print(f"Aviso: Arquivo {caminho_qss} não encontrado. Usando estilo padrão.")

    # Configuração do Stack
    main_stack = QStackedWidget()
    main_stack.setWindowTitle('Editors Helper')
    main_stack.setFixedSize(1000, 600) 

    tela1 = Teste(main_stack)
    tela2 = Teste2()

    main_stack.addWidget(tela1) # Índice 0
    main_stack.addWidget(tela2) # Índice 1

    main_stack.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()