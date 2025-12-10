import ffmpeg
import os
from pathlib import Path


class AudioSplitter:
    @staticmethod
    def split(audio_path: str, interval_seconds: int) -> list:
        """
        Divide um áudio em vários arquivos menores usando ffmpeg.

        :param audio_path: Caminho do arquivo de áudio original.
        :param interval_seconds: Duração de cada pedaço (em segundos).
        :return: Lista de caminhos dos arquivos gerados.
        """

        # Garantir que o arquivo existe
        audio_path = Path(audio_path)
        if not audio_path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {audio_path}")

        # Pasta de saída (mesmo local do arquivo, pasta "chunks")
        output_dir = audio_path.parent / "chunks"
        output_dir.mkdir(exist_ok=True)

        # Nome base para os arquivos
        out_pattern = str(output_dir / "chunk_%03d.wav")

        # Execução do ffmpeg para split
        (
            ffmpeg
            .input(str(audio_path))
            .output(
                out_pattern,
                f="segment",
                segment_time=interval_seconds,
                reset_timestamps=1
            )
            .run()
        )

        # Retornar os arquivos gerados
        return sorted(output_dir.glob("chunk_*.wav"))
