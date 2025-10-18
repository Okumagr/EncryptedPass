🔐 EncryptedPass

EncryptedPass é uma ferramenta de linha de comando (CLI) que gera senhas seguras e reproduzíveis a partir de uma senha base e de um salt.

Ela utiliza PBKDF2-HMAC-SHA256 e transforma o resultado em uma senha legível e fácil de usar.
Perfeita para quem quer segurança sem perder praticidade.

🎨 Recursos

Senha reproduzível: mesmos inputs → mesma saída

Formato legível e seguro

Visual elegante com cores no terminal (via colorama)

Copia automaticamente para o clipboard (via pyperclip)

Pode ser usado diretamente como executável (.exe) via PyInstaller

⚙️ Estrutura do projeto
EncryptedPass/
├─ EncryptedPass.py      # Arquivo principal da aplicação CLI
├─ build/                # Arquivos temporários do PyInstaller
├─ dist/                 # Executável pronto para rodar (EncryptedPass.exe)
├─ venv/                 # Ambiente virtual (opcional)
├─ *.spec                # Configuração do PyInstaller
└─ README.md             # Este arquivo

⚠️ O executável direto para rodar a aplicação fica dentro da pasta dist/ após rodar o PyInstaller.

💻 Instalação

Clone o repositório:

git clone https://github.com/USERNAME/EncryptedPass.git
cd EncryptedPass

(Opcional) Crie e ative o ambiente virtual:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

Instale as dependências:

pip install -r requirements.txt

🚀 Como usar
1️⃣ Executando pelo Python:
python EncryptedPass.py --password "SuaSenhaBase" --salt "SeuSalt"

2️⃣ Executando o executável (mais fácil para qualquer pessoa):

Windows:

dist\EncryptedPass.exe

Linux / Mac:

./dist/EncryptedPass

O executável já contém tudo o que precisa, não é necessário Python instalado para rodar.
