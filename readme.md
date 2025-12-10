# 🔔 Zolt Summarizer

Ferramenta de sumarização de áudios usando Whisper para transcrição, pyannote para diarização e modelos de LLM através de Ollama para sumarização.

## Requisitos

- Docker
- FFmpeg


## Como usar

Construir a imagem Python a partir do Dockerfile, baixar a imagem oficial do Ollama e subir os dois em modo "detached" (em segundo plano)

```
docker-compose up -d --build
```

Depois disso, inicie e teste o Ollama (dê um oi pro modelo que você quer de sumarizador)

```
docker exec -it ollama_backend ollama run llama3
```

![alt text](./readme_images/image.png)

> Você pode trocar `llama3` pelo modelo que você quer usar.

Saia do container encerrando a conversa com o seguinte comando:

```
/bye
```

Em seguida entre no container com o zolt, é aqui que você vai executar o pipeline.

```
docker exec -it zolt_summarizer /bin/bash
```

Garanta que todas as bibliotecas estão instaladas:

```bash
pip install -r requirements.txt
```

> Se você quiser fazer a extração de áudio de um vídeo com ffmpeg, basta entrar no local onde o vídeo está (pasta) através do terminal e usar este comando do ffmpeg:
>```
> ffmpeg -i "seuvideo.mp4" -vn -acodec pcm_s16le -ar 16000 -ac 1 "seuaudio.wav"
>```
>
> Troque `seuvideo.mp4` pelo caminho para o seu vídeo e `seuaudio.wav` para o caminho do seu áudio

Adicione suas variáveis de configuração no arquivo `zolt_config.py`, os nomes são bem descritivos. Ele se parece com isso aqui:

```python
HUGGING_FACE_TOKEN="SEU_TOKEN"
FILE_PATH="./CAMINHO_PRO_SEU_AUDIO.wav"
SUMMARIZER_MODEL="qwen3:1.7b" # o modelo que você quer usar
TIMESTAMPS=False # se quer que ele use as transcrições com ou sem timestamps (ambas serão salvas)
```

## Tudo pronto?

Se você conseguiu, basta rodar executar esse comando para o pipeline principal:

```
python flow.py
```

E pronto! agora é só assistir eles preparando seu resumo.

Pode demorar um tempinho (provavelmente vai), então talvez você queira entender o que está acontecendo no seu terminal, pra saber o quão próximo seu resumo está de ficar pronto.

Pra começar, temos 4 entidades principais que fazem isso acontecer.

- Nayahath
- Diarizer
- Transcripter
- Summarizer

### Nayahath

Ela é basicamente a "coordenadora" das demais. Ela é uma instância do módulo ArcanaFlow, que desenha esse log bonitinho que você ta vendo no terminal.

Ela inicia o pipeline dizendo que eles estão verificando as interfaces.

Isso porque você pode implementar sua própria versão de diarizador, transcritor e sumarizador, a pasta `./modules/Interfaces` pode te ajudar a conseguir mais instruções sobre isso.

### Diarizer

O papel dele é basicamente identificar no seu áudio "quem está falando o que". Ele vai fazer o que chamamos de "diarização" que é a separação dos falantes do áudio por características extraídas da voz.

A versão padrão dele usa pyannote, mas como eu falei, você pode implementar uma versão sua se quiser.

### Transcripter

O papel dele transcrever o seu áudio. Ele não está preocupado com "quem falou o que" mas sim com **o que foi dito**. Ele vai anotar as falas e os tempos, pra depois conversar com o diarizer e descobrir algo muito importante: "**Quem** falou **o que**".

Depois dessa conversa dos dois, eles vão preparar uma entrada pra próxima entidade.

### Summarizer

O papel do Summarizer é pegar o que o Diarizer e o Transcripter escreveram juntos, ler e criar um resumo. Os summarizers vêm do Ollama, você pode escolher outro modelo de lá se quiser testar outro.

Caso você tenha feito o pipeline inteiro, mas quiser testar os mesmos valores com outro summarizer, não precisa rodar tudo denovo. Basta editar e executar o arquivo `teste_ollama.py`, ele permite executar **só o summarizer** direto, sem o resto do pessoal. Assim você pode fazer testes mais rápidos, só colando o texto que você quer no valor da variável.