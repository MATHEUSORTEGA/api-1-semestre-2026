import sys
import subprocess
import importlib

def verificar_modulo(nome_modulo, nome_pacote_pip=None):
    """
    Tenta importar um módulo. Se falhar, faz a instalação via pip automaticamente.
    
    :param nome_modulo: Nome usado no código para o import (ex: 'pandas', 'dotenv')
    :param nome_pacote_pip: Nome usado no pip install. Se vazio, assume que é igual ao nome_modulo.
    """
    # Se o nome no pip não for informado, assume que é o mesmo do import
    if nome_pacote_pip is None:
        nome_pacote_pip = nome_modulo
        
    try:
        # importlib faz o papel do "import X" mas recebendo uma string
        importlib.import_module(nome_modulo)
        print(f"[Config] O módulo '{nome_modulo}' já esta instalado. ✅")
        
    except ImportError:
        print(f"[Config] ⚠️ Módulo '{nome_modulo}' não encontrado. ⬇️ Instalando pacote '{nome_pacote_pip}'...")
        
        # Executa o pip install silenciosamente (ou mostrando no terminal)
        subprocess.check_call([sys.executable, "-m", "pip", "install", nome_pacote_pip])
        
        print(f"[Config] ⬇️ Instalação de '{nome_pacote_pip}' concluída com sucesso! ✅\n")

def verificacao_ambiente():
    print("====[config.py]=============================== ")
    print("🔍 Iniciando verificação do ambiente... \n")
    verificar_modulo("telebot")
    verificar_modulo("dspy")
    verificar_modulo("dotenv")
    
    print("\n[Config] Todos os módulos validados. Ambiente pronto! 🚀\n")