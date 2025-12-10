import os
from datetime import datetime

class OutputManager:
    def __init__(self, base_path="."):
        self.base_path = base_path
        self.current_folder = None

    def create_timestamped_folder(self, custom_name: str):
        """
        Cria uma pasta com o formato: YYYY-MM-DD_HH-MM-SS_customname
        """
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        folder_name = f"{timestamp}_{custom_name}"
        folder_path = os.path.join(self.base_path, folder_name)

        os.makedirs(folder_path, exist_ok=True)
        self.current_folder = folder_path

        return folder_path

    def save_text_file(self, filename: str, content: str, folder: str = None):
        """
        Salva um arquivo .txt com o conteúdo especificado.
        Se folder não for fornecida, usa a última pasta criada.
        """
        target_folder = folder or self.current_folder
        if target_folder is None:
            raise ValueError("Nenhuma pasta definida. Crie uma pasta primeiro ou informe uma explicitamente.")

        file_path = os.path.join(target_folder, f"{filename}.txt")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        return file_path
