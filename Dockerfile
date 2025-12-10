FROM python:3.12.3-slim

ENV DEBIAN_FRONTEND=noninteractive

# Instala ffmpeg e git (necessários para libs de audio)
RUN apt-get update && \
    apt-get install -y ffmpeg git && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

# Configuração do venv
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Instala dependências Python
RUN pip install --upgrade pip && \
    pip install torch torchaudio torchcodec pyannote-audio ollama

# Copia o código
COPY . /workspace

# Mantém o container rodando para você poder entrar nele
CMD ["tail", "-f", "/dev/null"]