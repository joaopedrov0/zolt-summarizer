# colors.py
import sys

# Códigos ANSI
ANSI_CODES = {
    # Cores de Texto (Brilhantes/Bold)
    'BLACK': '\033[90m',
    'RED': '\033[91m',
    'GREEN': '\033[92m',
    'YELLOW': '\033[93m',
    'BLUE': '\033[94m',
    'MAGENTA': '\033[95m',
    'CYAN': '\033[96m',
    'WHITE': '\033[97m',
    
    # Estilos
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m',
    
    # Reset
    'RESET': '\033[0m',
}

def colorize(text, color_name):
    """Aplica uma cor ou estilo a uma string."""
    code = ANSI_CODES.get(color_name.upper())
    if code:
        return f"{code}{text}{ANSI_CODES['RESET']}"
    return text

# Funções de conveniência
def red(text): return colorize(text, 'red')
def green(text): return colorize(text, 'green')
def yellow(text): return colorize(text, 'yellow')
def blue(text): return colorize(text, 'blue')
def magenta(text): return colorize(text, 'magenta')
def cyan(text): return colorize(text, 'cyan')
def white(text): return colorize(text, 'white')
def bold(text): return colorize(text, 'bold')
def underline(text): return colorize(text, 'underline')

# Bloco de demonstração
if __name__ == "__main__":
    print(f"Teste do módulo {__file__}")
    print(red('Texto em Vermelho - ERROS'))
    print(yellow('Texto em Amarelo - WARNINGS'))
    print(green('Texto em Verde - SUCESSO'))
    print(bold(cyan('Texto Ciano em Negrito')))