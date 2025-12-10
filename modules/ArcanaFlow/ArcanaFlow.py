# arcana_flow.py
import os
import datetime
from . import colors
from . import caller_info

class ArcanaFlow:
    def __init__(self, active=True):
        self.config = {
            "flag": True,
            "time": True,
            "file": False,
            "line": False,
            "entity": True,
            "message": True
        }
        self.active = active
        self.entities = {} # Par nome: cor

        # Mapeamento de strings para funções do módulo colors
        self.color_function = {
            "red": colors.red,
            "green": colors.green,
            "yellow": colors.yellow,
            "blue": colors.blue,
            "magenta": colors.magenta,
            "cyan": colors.cyan,
            "white": colors.white,
        }

        self.style_text = {
            "bold": colors.bold,
            "underline": colors.underline
        }

        self.flag_color_config = {
            "ACTION": "blue",
            "ERROR": "red",
            "NONE": "white",
            "WARNING": "yellow"
        }

        self.general_color_config = {
            "time": "green",
            "file": "cyan",
            "line": "cyan",
            "entity": "magenta",
            "message": "white",
            "custom": "green"
        }

        self.general_size_config = {
            "flag": 10,
            "time": 10,
            "file": 15,
            "line": 7,
            "entity": 15,
            "message": 80,
            "custom": 20
        }

    # Singleton settings / Configuration
    def set_config(self, config_key, value):
        if config_key in self.config:
            self.config[config_key] = value

    def set_active(self, active):
        self.active = active

    def add_entity(self, name, color):
        self.entities[name] = color

    # Render methods
    def fix_blank_space(self, text, value):
        text = str(text)
        if len(text) > value:
            # Corta e adiciona reticências mantendo o tamanho
            return text[:value - 3] + "..."
        # padEnd equivalente em Python
        return text.ljust(value, ' ')

    def paint(self, text, kind):
        clean_text = text.strip()
        
        if kind == "flag":
            color_name = self.flag_color_config.get(clean_text, "white")
            return self.color_function[color_name](text)
            
        if kind == "entity":
            # Verifica se é uma entidade customizada, senão usa cor padrão da config
            if clean_text in self.entities:
                color_name = self.entities[clean_text]
            else:
                color_name = self.general_color_config.get(kind, "white")
            return self.color_function[color_name](text)
        
        # Default fallback
        color_name = self.general_color_config.get(kind, "white")
        return self.color_function[color_name](text)

    def format_text(self, text, kind):
        # Nota: renomeei 'format' para 'format_text' pois format é built-in do python
        size = self.general_size_config.get(kind, 20)
        text = self.fix_blank_space(text, size)
        text = self.paint(text, kind)
        return text

    def load_header(self):
        if not self.active:
            return
        
        temp = ""
        for key, enabled in self.config.items():
            if enabled:
                size = self.general_size_config.get(key, 10)
                temp += self.fix_blank_space(key.upper(), size)
        print(temp)

    # Functional methods
    def action(self, entity=None, message=None):
        self.out(flag="ACTION", entity=entity, message=message)

    def error(self, entity=None, message=None):
        self.out(flag="ERROR", entity=entity, message=message)
    
    def warning(self, entity=None, message=None):
        self.out(flag="WARNING", entity=entity, message=message)

    def out(self, flag=None, entity=None, message=None, custom=None):
        # Verifica se está ativo
        if self.active:
            prepare_output = ""
            caller_data = caller_info.get_caller_info()

            if self.config.get("flag"):
                prepare_output += self.format_text(flag if flag else "NONE", "flag")

            if self.config.get("time"):
                now = datetime.datetime.now()
                now_str = now.strftime("%H:%M:%S")
                prepare_output += self.format_text(now_str, "time")

            if self.config.get("file"):
                filename = os.path.basename(caller_data['file'])
                prepare_output += self.format_text(filename, "file")

            if self.config.get("line"):
                line_str = str(caller_data['line'])
                prepare_output += self.format_text(line_str, "line")

            if self.config.get("entity"):
                entity_str = entity if entity else "-"
                prepare_output += self.format_text(entity_str, "entity")
            
            if custom:
                # Lógica para custom se necessário
                pass

            if self.config.get("message"):
                msg_str = str(message) if message else ""
                prepare_output += self.format_text(msg_str, "message")

            print(prepare_output)

# Instância Singleton
instance = ArcanaFlow()

# Exporta apenas a instância se for importado
if __name__ != "__main__":
    pass

# Bloco de teste se rodar o arquivo diretamente
if __name__ == "__main__":
    instance.load_header()
    instance.add_entity("DB", "yellow")
    instance.add_entity("SERVER", "magenta")
    
    instance.action("SERVER", "Servidor iniciado na porta 8080")
    instance.warning("DB", "Conexão lenta detectada")
    instance.error("AUTH", "Falha na validação do token")