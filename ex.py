import sys
import os
from PyQt6.QtWidgets import (QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, 
                             QWidget, QStackedWidget, QFrame, QButtonGroup, QGridLayout, QScrollArea)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap


class PaginaPlugins(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("pagina_interna")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(15)
        
        titulo = QLabel("GERENCIADOR DE PLUGINS")
        titulo.setObjectName("titulo_pagina")
        layout.addWidget(titulo)

        scroll = QScrollArea()
        scroll.setObjectName("scroll_plugins")
        scroll.setWidgetResizable(True)
        
        container_widget = QWidget()
        container_widget.setObjectName("container_plugins")
        container_widget.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        container_layout = QVBoxLayout(container_widget)
        container_layout.setContentsMargins(0, 0, 15, 0)
        container_layout.setSpacing(10)

        meus_plugins = [
            {"nome": "RSMB", "versao": "v6.4.0", "desc": "ReelSmart Motion Blur - Desfoque natural."},
            {"nome": "BCC", "versao": "2024", "desc": "Boris Continuum Complete - Pacote VFX."},
            {"nome": "Optical Flares", "versao": "v1.3.8", "desc": "Video Copilot - Lentes e flares."},
            {"nome": "Magic Bullet Looks", "versao": "v16.1.0", "desc": "Color grading profissional."},
            {"nome": "Sapphire Add-ons", "versao": "v2023.5", "desc": "Filtros e transições."},
            {"nome": "Twixtor Pro", "versao": "v7.5.3", "desc": "Câmera lenta ultra suave."},
            {"nome": "Deep Glow", "versao": "v1.4.5", "desc": "Brilho fisicamente preciso."}
        ]

        for plugin in meus_plugins:
            card = QFrame()
            card.setObjectName("card_item")
            h_layout = QHBoxLayout(card)
            h_layout.setContentsMargins(25, 20, 25, 20)
            
            info_vbox = QVBoxLayout()
            info_vbox.setSpacing(4)
            nome_label = QLabel(plugin["nome"])
            nome_label.setObjectName("plugin_nome_label")
            desc_label = QLabel(f"{plugin['versao']} • {plugin['desc']}")
            desc_label.setObjectName("plugin_desc_label")
            
            info_vbox.addWidget(nome_label)
            info_vbox.addWidget(desc_label)
            
            btn = QPushButton("INSTALAR")
            btn.setObjectName("btn_acao_plugin")
            btn.setFixedSize(100, 35)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)

            h_layout.addLayout(info_vbox)
            h_layout.addStretch()
            h_layout.addWidget(btn)
            container_layout.addWidget(card)

        container_layout.addStretch()
        scroll.setWidget(container_widget)
        layout.addWidget(scroll)

class PaginaSoftware(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("pagina_interna")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(40, 40, 40, 40)
        
        titulo = QLabel("SOFTWARES SUPORTADOS")
        titulo.setObjectName("titulo_pagina")
        layout_principal.addWidget(titulo)

        grade = QGridLayout()
        grade.setSpacing(25)

        base_path = os.path.dirname(os.path.abspath(__file__))

        softwares = [
            {"nome": "After Effects", "img": "img/AE.png"},
            {"nome": "Premiere Pro", "img": "img/PR.png"},
            {"nome": "Photoshop", "img": "img/PS.png"},
            {"nome": "Media Encoder", "img": "img/ME.png"},
            {"nome": "HandBrake", "img": "img/hb.png"},
            {"nome": "Topaz", "img": "img/topaz.jpeg"}
        ]

        for i, soft in enumerate(softwares):
            btn = QPushButton()
            btn.setObjectName("card_software")
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setFixedSize(165, 165)
            
            # Criamos um layout interno para o botão
            btn_layout = QVBoxLayout(btn)
            btn_layout.setContentsMargins(10, 20, 10, 15)
            btn_layout.setSpacing(10)

            # Imagem do Software
            img_label = QLabel()
            caminho_img = os.path.join(base_path, soft["img"])
            pixmap = QPixmap(caminho_img)
            
            if not pixmap.isNull():
                img_label.setPixmap(pixmap.scaled(75, 75, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
            else:
                img_label.setText("[Icon]") # Caso a imagem falhe
            
            img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            img_label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

            # Texto embaixo
            txt_label = QLabel(soft["nome"])
            txt_label.setObjectName("label_software_btn")
            txt_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            txt_label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

            btn_layout.addWidget(img_label)
            btn_layout.addWidget(txt_label)
            
            grade.addWidget(btn, i // 2, i % 2)

        layout_principal.addLayout(grade)
        layout_principal.addStretch()


class PaginaPresets(QFrame): 
    def __init__(self):
        super().__init__()
        self.setObjectName("pagina_interna")
        
        # Layout principal da página
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(15)
        # Alinha o conteúdo no Topo e Centro conforme você pediu
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        
        titulo = QLabel("GERENCIADOR DE PRESETS")
        titulo.setObjectName("titulo_pagina")
        layout.addWidget(titulo)

        # Scroll Area para os cards
        scroll = QScrollArea()
        scroll.setObjectName("scroll_plugins")
        scroll.setWidgetResizable(True)
        
        container_widget = QWidget()
        container_widget.setObjectName("container_plugins")
        container_widget.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        container_layout = QVBoxLayout(container_widget)
        container_layout.setContentsMargins(0, 0, 15, 0)
        container_layout.setSpacing(10)

        # LISTA CORRIGIDA (Agora com todas as chaves para não dar KeyError)
        meus_presets = [
            {"nome": "Preset de Shake", "versao": "v1.0", "desc": "Efeito de tremor suave."},
            {"nome": "Preset de Texto", "versao": "v2.1", "desc": "Animações de entrada/saída."},
            {"nome": "Preset de Twixtor", "versao": "v1.5", "desc": "Configurações de Slow Motion."},
            {"nome": "Preset de One Frames", "versao": "v1.0", "desc": "Flash branco de 1 frame."},
            {"nome": "Preset de Transições", "versao": "v3.0", "desc": "Pack de transições variadas."},
            {"nome": "Preset de CC", "versao": "v4.2", "desc": "Color Correction cinematográfico."},
        ]

        for preset in meus_presets:
            card = QFrame()
            card.setObjectName("card_item")
            h_layout = QHBoxLayout(card)
            h_layout.setContentsMargins(25, 20, 25, 20)
            
            info_vbox = QVBoxLayout()
            info_vbox.setSpacing(4)
            
            nome_label = QLabel(preset["nome"])
            nome_label.setObjectName("plugin_nome_label")
            
            # Aqui estava o erro! Agora 'versao' e 'desc' existem na lista acima.
            desc_text = f"{preset['versao']} • {preset['desc']}"
            desc_label = QLabel(desc_text)
            desc_label.setObjectName("plugin_desc_label")
            
            info_vbox.addWidget(nome_label)
            info_vbox.addWidget(desc_label)
            
            btn = QPushButton("INSTALAR") # Alterado para fazer mais sentido em presets
            btn.setObjectName("baixar")   # Usando o ID que você criou no QSS
            btn.setFixedSize(100, 35)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)

            h_layout.addLayout(info_vbox)
            h_layout.addStretch()
            h_layout.addWidget(btn)
            container_layout.addWidget(card)

        container_layout.addStretch()
        scroll.setWidget(container_widget)
        layout.addWidget(scroll)

class PaginaTutoriais(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("pagina_interna")
        h_layout = QVBoxLayout(self)
        h_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        h_layout.setContentsMargins(40, 40, 40, 40)
        h_layout.setSpacing(15)

        titulo = QLabel("Ajuda para iniciantes")
        titulo.setObjectName("Titulo_tuto")
        titulo.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        h_layout.addWidget(titulo)

        


class TelaWelcome(QFrame):
    def __init__(self, stack):
        super().__init__() 
        self.stack = stack 
        self.setObjectName("tela1")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        layout = QVBoxLayout(self)
        layout.addStretch()
        
        self.label_titulo = QLabel('Bem-vindo')
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_titulo.setObjectName("textowelcome")
        layout.addWidget(self.label_titulo)

        self.subtitulo = QLabel('EDITORS HELPER • PREMIUM ACCESS')
        self.subtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subtitulo.setObjectName("subtitulo")
        layout.addWidget(self.subtitulo)

        self.botao = QPushButton('INICIAR SESSÃO')
        self.botao.setObjectName("botao_entrar") 
        self.botao.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao.clicked.connect(self.irParaHome)
        layout.addWidget(self.botao, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()

    def irParaHome(self):
        self.stack.setFixedSize(1000, 600)
        self.stack.setCurrentIndex(1)

class TelaHome(QWidget):
    def __init__(self):
        super().__init__() 
        self.setObjectName("tela2")
        layout_principal = QHBoxLayout(self)
        layout_principal.setContentsMargins(0, 0, 0, 0)
        layout_principal.setSpacing(0)

        self.sidebar = QFrame()
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setFixedWidth(220)
        layout_sidebar = QVBoxLayout(self.sidebar)
        layout_sidebar.setContentsMargins(0, 40, 0, 10)

        self.grupo_botoes = QButtonGroup(self)
        self.grupo_botoes.setExclusive(True)

        self.paginas_internas = QStackedWidget()
        self.paginas_internas.setObjectName("stack_paginas")

        self.telas = [PaginaPlugins(), PaginaSoftware(), PaginaPresets(), PaginaTutoriais()]
        nomes = ["PLUGINS", "SOFTWARES", "PRESETS", "TUTORIAIS"]

        for i, tela in enumerate(self.telas):
            if isinstance(tela, QLabel):
                tela.setAlignment(Qt.AlignmentFlag.AlignCenter)
                tela.setStyleSheet("color: #444; font-size: 20px; background-color: #0a0a0a;")
            
            self.paginas_internas.addWidget(tela)
            
            btn = QPushButton(nomes[i])
            btn.setProperty("class", "btn_sidebar")
            btn.setCheckable(True)
            if i == 0: btn.setChecked(True)
            btn.clicked.connect(lambda checked, index=i: self.paginas_internas.setCurrentIndex(index))
            self.grupo_botoes.addButton(btn)
            layout_sidebar.addWidget(btn)

        layout_sidebar.addStretch()
        layout_principal.addWidget(self.sidebar)
        layout_principal.addWidget(self.paginas_internas)

def main():
    app = QApplication(sys.argv)
    diretorio = os.path.dirname(os.path.abspath(__file__))
    caminho_qss = os.path.join(diretorio, "style.qss")
    if os.path.exists(caminho_qss):
        with open(caminho_qss, "r", encoding="utf-8") as file:
            app.setStyleSheet(file.read())

    main_stack = QStackedWidget()
    main_stack.setWindowTitle('Editors Helper Pro')
    main_stack.setFixedSize(800, 450) 
    main_stack.addWidget(TelaWelcome(main_stack))
    main_stack.addWidget(TelaHome())

    main_stack.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()