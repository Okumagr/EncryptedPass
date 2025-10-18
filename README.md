# 🔐 EncryptedPass

EncryptedPass é uma ferramenta de linha de comando (CLI) que gera **senhas seguras e reproduzíveis** a partir de uma senha base e de um salt.  
Ela usa **PBKDF2-HMAC-SHA256** e transforma o resultado em um formato legível, prático e seguro.

> Ideal para gerar senhas fortes que podem ser reproduzidas sempre que necessário (mesmos inputs → mesma saída).

---

## 🎯 Recursos

- Senha reproduzível: mesmos inputs → mesma saída  
- Formato legível e seguro (alfanumérico com símbolos selecionados)  
- Visual elegante no terminal (via **colorama**)  
- Copia automaticamente para o clipboard (via **pyperclip**)  
- Disponível como executável (`.exe`) gerado com **PyInstaller** (opção “onefile”)

---

## 📁 Estrutura do projeto

EncryptedPass/
├─ EncryptedPass.py # Arquivo principal da aplicação CLI
├─ requirements.txt # Dependências Python
├─ dist/ # Executável pronto (EncryptedPass.exe) — gerado pelo PyInstaller
├─ build/ # Arquivos temporários do PyInstaller
├─ EncryptedPass.spec # .spec gerado/opcional do PyInstaller
└─ README.md # Este arquivo

> ⚠️ Após rodar o PyInstaller, o executável ficará em `dist/EncryptedPass` (Windows: `dist\EncryptedPass.exe`).

---

## 🛠️ Requisitos

- Python 3.8+ (somente se for usar o script `.py`)  
- `colorama`, `pyperclip` (ou equivalente)  
- (Opcional) PyInstaller para gerar o executável

Instalação das dependências:
```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```
## 🚀 Como usar

1) Executando pelo Python

```bash
python EncryptedPass.py --password "SuaSenhaBase" --salt "SeuSalt"
Executável
Windows:

powershell
Copiar código
dist\EncryptedPass.exe --password "SuaSenhaBase" --salt "SeuSalt"
Linux / macOS:

bash
Copiar código
./dist/EncryptedPass --password "SuaSenhaBase" --salt "SeuSalt"

./dist/EncryptedPass --password "SuaSenhaBase" --salt "SeuSalt"
```
