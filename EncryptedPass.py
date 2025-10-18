#!/usr/bin/env python3
"""
Pass.py - EncryptedPassword (CLI Decorado)
"""
import os, sys, time, hashlib, base64, binascii
from getpass import getpass
from colorama import Fore, Style, init

# Inicializa cores
init(autoreset=True)

# Constantes
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_#@$%&"
ITERATIONS = 300_000
DKLEN = 32
OUTPUT_LENGTH = 20


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def try_copy(text: str) -> bool:
    try:
        import pyperclip
        pyperclip.copy(text)
        return True
    except Exception:
        return False


def derive_pbkdf2(passphrase: str, salt_bytes: bytes, iterations: int = ITERATIONS, dklen: int = DKLEN) -> bytes:
    return hashlib.pbkdf2_hmac("sha256", passphrase.encode("utf-8"), salt_bytes, iterations, dklen)


def map_to_human(dk: bytes, alphabet: str = ALPHABET, out_len: int = OUTPUT_LENGTH) -> str:
    L = len(alphabet)
    return ''.join(alphabet[b % L] for b in dk[:out_len])


def parse_salt(salt_input: str) -> bytes:
    s = salt_input.strip()
    maybe_b64 = all(c.isalnum() or c in "-_=" for c in s) and (2 <= len(s) <= 88)
    if maybe_b64:
        try:
            padding = '=' * ((4 - len(s) % 4) % 4)
            return base64.urlsafe_b64decode(s + padding)
        except Exception:
            pass
    return s.encode('utf-8')


def show_intro():
    clear()
    print(Fore.CYAN + Style.BRIGHT + "=" * 60)
    print(
        Fore.MAGENTA + Style.BRIGHT +
        "           🔐  E N C R Y P T E D   P A S S W O R D  🔐"
    )
    print(Fore.CYAN + "=" * 60 + "\n")
    print(Fore.WHITE + "Bem-vindo — esta ferramenta gera uma senha segura e reproduzível\n"
          "a partir da sua senha padrão e de um salt de segurança usando PBKDF2-HMAC-SHA256.\n")
    print(Fore.YELLOW + "Resumo:")
    print(Fore.WHITE + "  1) Informe sua senha padrão (privada)")
    print(Fore.WHITE + "  2) Informe seu salt (texto ou base64)")
    print(Fore.WHITE + "  3) O programa gera uma senha legível e única\n")
    print(Fore.LIGHTBLACK_EX + "Observação: mesmos inputs => mesma saída (determinístico).\n")


def menu():
    print(Fore.CYAN + "╔══════════════════════════════════════════╗")
    print(Fore.CYAN + "║" + Fore.WHITE + "  [1]" + Fore.YELLOW + " Descobrir minha senha criptografada " + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.WHITE + "  [2]" + Fore.YELLOW + " Sair                               " + Fore.CYAN + " ║")
    print(Fore.CYAN + "╚══════════════════════════════════════════╝\n")


def prompt_passphrase() -> str:
    try:
        p = getpass(Fore.YELLOW + "Digite sua senha padrão (entrada oculta): " + Fore.WHITE).strip()
        if not p:
            p = input(Fore.RED + "Senha vazia — digite visivelmente: " + Fore.WHITE).strip()
    except Exception:
        p = input(Fore.YELLOW + "Digite sua senha padrão: " + Fore.WHITE).strip()
    return p


def prompt_salt() -> str:
    return input(Fore.YELLOW + "Digite seu salt (texto ou base64 urlsafe): " + Fore.WHITE).strip()


def run_discover():
    clear()
    print(Fore.MAGENTA + "=== Descobrir senha criptografada ===\n")
    p = prompt_passphrase()
    s_input = prompt_salt()
    salt_bytes = parse_salt(s_input)
    derived = derive_pbkdf2(p, salt_bytes)
    human = map_to_human(derived)
    hex_out = binascii.hexlify(derived).decode()
    b64_out = base64.b64encode(derived).decode()

    print(Fore.GREEN + "\nSua senha criptografada (formato legível):\n")
    print(Fore.WHITE + Style.BRIGHT + "  >>> " + Fore.CYAN + human + Fore.WHITE + " <<<\n")
    print(Fore.LIGHTBLACK_EX + "(PBKDF2 hex): " + hex_out)
    print(Fore.LIGHTBLACK_EX + "(PBKDF2 base64): " + b64_out)

    if try_copy(human):
        print(Fore.GREEN + "\n✔ Senha copiada para o clipboard!")
    else:
        print(Fore.RED + "\n⚠ Instale 'pyperclip' para copiar automaticamente (pip install pyperclip).")

    print(Fore.LIGHTBLACK_EX + "\nPressione Enter para voltar ao menu...")
    try:
        input()
    except KeyboardInterrupt:
        pass


def main_loop():
    while True:
        show_intro()
        menu()
        choice = input(Fore.CYAN + "Escolha [1-2]: " + Fore.WHITE).strip()
        if choice == '1':
            run_discover()
        elif choice == '2':
            print(Fore.LIGHTRED_EX + "\nEncerrando... Até mais! 👋")
            time.sleep(1)
            return
        else:
            print(Fore.RED + "\nOpção inválida. Pressione Enter para tentar novamente.")
            try:
                input()
            except KeyboardInterrupt:
                return


if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        print(Fore.RED + "\nInterrompido. Tchau!")
        sys.exit(0)
