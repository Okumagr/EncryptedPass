# 🔐 EncryptedPass

**EncryptedPass** é uma ferramenta de linha de comando (CLI) que gera **senhas seguras e reproduzíveis** a partir de uma senha padrão e de um salt.  

Ela utiliza **PBKDF2-HMAC-SHA256** e transforma o resultado em uma senha legível e fácil de usar.  
Perfeita para quem quer segurança sem perder praticidade.

---

## 🎨 Recursos

- Senha reproduzível: mesmos inputs → mesma saída
- Formato legível e seguro
- Visual elegante com cores no terminal (via `colorama`)
- Copia automaticamente para o clipboard (via `pyperclip`)
- Compatível com `.exe` usando PyInstaller

---

## ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/USERNAME/EncryptedPass.git
cd EncryptedPass
