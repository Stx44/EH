import sys
import os
from PyQt6.QtWidgets import (QApplication, QLabel, QPushButton, QVBoxLayout, 
                             QWidget, QStackedWidget, QFrame, QSpacerItem, QSizePolicy)
from PyQt6.QtCore import Qt

class TelaWelcome(QFrame):
    def __init__(self, stack):
        super().__init__() 
        self.stack = stack 
        self.setObjectName("tela1")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Spacers servem para empurrar o conteúdo para o centro vertical
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # 1. Texto de Boas-vindas
        self.label_titulo = QLabel('Bem-vindo')
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_titulo.setObjectName("textowelcome")
        layout.addWidget(self.label_titulo)

        # Pequeno subtítulo para preencher o espaço da imagem removida
        self.subtitulo = QLabel('Editors Helper • Pro Version')
        self.subtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subtitulo.setStyleSheet("color: #666; font-size: 14px; margin-bottom: 20px;")
        layout.addWidget(self.subtitulo)

        # 2. Botão de entrada
        self.botao = QPushButton('Entrar no Painel')
        self.botao.setObjectName("botao_entrar") 
        self.botao.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao.clicked.connect(self.irParaHome)
        layout.addWidget(self.botao, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

    def irParaHome(self):
        # Transição de tamanho para o padrão 1000x500
        self.stack.setFixedSize(1000, 500)
        self.stack.setCurrentIndex(1)

class TelaHome(QWidget):
    def __init__(self):
        super().__init__() 
        self.setObjectName("tela2")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel('Painel Principal')
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
    except FileNotFoundError:
        print("Aviso: Arquivo style.qss não encontrado.")

    # Configuração do Stack (Janela Principal)
    main_stack = QStackedWidget()
    main_stack.setWindowTitle('Editors Helper')
    
    # Tamanho inicial da Welcome (Pequena)
    main_stack.setFixedSize(800, 400) 

    main_stack.addWidget(TelaWelcome(main_stack)) # Índice 0
    main_stack.addWidget(TelaHome())              # Índice 1

    main_stack.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()