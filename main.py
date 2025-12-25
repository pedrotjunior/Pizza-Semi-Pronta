import sys
from PySide6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QMessageBox
)
from PySide6.QtCore import Qt

class Login(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login - Pizzaria Semi-Pronta")
        self.resize(420, 580)

        # Layout principal
        layout = QVBoxLayout(self)

        # Título
        titulo = QLabel("PIZZARIA DELÍCIA")
        titulo.setStyleSheet("font-size: 28px; font-weight: bold; color: #d32f2f;")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(titulo)

        layout.addSpacing(40)

        # Usuário
        layout.addWidget(QLabel("Usuário:"))
        self.campo_usuario = QLineEdit()
        self.campo_usuario.setPlaceholderText("digite seu usuário")
        layout.addWidget(self.campo_usuario)

        # Senha
        layout.addWidget(QLabel("Senha:"))
        self.campo_senha = QLineEdit()
        self.campo_senha.setPlaceholderText("digite sua senha")
        self.campo_senha.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.campo_senha)

        layout.addSpacing(30)

        # Botão
        btn = QPushButton("ENTRAR NO SISTEMA")
        btn.clicked.connect(self.check)
        layout.addWidget(btn)

        layout.addStretch()
        rodape = QLabel("© 2025 Pizzaria Semi-Pronta")
        rodape.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(rodape)

    def check(self):
        usuario = self.campo_usuario.text().strip()
        senha = self.campo_senha.text()

        if usuario == "admin" and senha =="123":
            QMessageBox.information(self, "Sucesso", "Login realizado com sucesso!")
            self.accept()
        else:
            QMessageBox.critical(self, "Erro", "Usuário ou senha incorretos!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Login()
    janela.show()
    sys.exit(app.exec())