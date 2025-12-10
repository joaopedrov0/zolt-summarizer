# Utilitário para dividir um áudio em partes iguais de tamanho fixo com ffmpeg

from modules.AudioSplitter import AudioSplitter

tempo = 30 * 60  # 30 minutos em segundos

AudioSplitter.split("caminho_para_seu_audio.wav", 60*30)