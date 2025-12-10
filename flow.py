import datetime
starting_time = datetime.datetime.now().strftime("%H:%M:%S")

from modules import Nayahath
Nayahath.add_entity("Nayahath", "magenta")
Nayahath.add_entity("Transcripter", "green")
Nayahath.add_entity("Diarizer", "blue")
Nayahath.add_entity("Summarizer", "yellow")
Nayahath.set_config("line", False)
Nayahath.set_config("file", False)

from pathlib import Path
from modules import OutputManager, Synchronizer, TranscripterWhisper, DiarizerPyannote, SummarizerQwen3
from modules.Interfaces import DiarizerInterface, SummarizerInterface, TranscripterInterface
import zolt_config as config

# ! User inputs ==============
hugging_face_token = config.HUGGING_FACE_TOKEN
file = config.FILE_PATH
summarizer_model=config.SUMMARIZER_MODEL
timestamps=config.TIMESTAMPS
# ! ==========================

audio_file_path = Path(file)

# Creating output manager binded to a folder
om = OutputManager("./outputs")
om.create_timestamped_folder(custom_name=audio_file_path.name)

Nayahath.action("Nayahath", "Checking interfaces.")

DiarizerInterface.register(DiarizerPyannote)
Nayahath.action("Diarizer", "Contract signed.")
diarizer = DiarizerPyannote()

TranscripterInterface.register(TranscripterWhisper)
Nayahath.action("Transcripter", "Contract signed.")
transcripter = TranscripterWhisper()

SummarizerInterface.register(SummarizerQwen3)
Nayahath.action("Summarizer", "Contract signed.")
summarizer = SummarizerQwen3(model=summarizer_model)

speakers_dictionaries = diarizer.diarize(audio_file_path, hugging_face_token=hugging_face_token)

om.save_text_file(
    filename="diarization",
    content=str(speakers_dictionaries)
)

Nayahath.action("Nayahath", "Diarization completed, initializing transcription.")

transcription_segments = transcripter.transcript(audio_file_path)

Nayahath.action("Nayahath", "Transcription completed, syncing results.")

res = Synchronizer.sync(speakers_dictionary=speakers_dictionaries, transcription_segments=transcription_segments)

om.save_text_file("raw_transcription_timestamped_output", str(res))

temp = ""
timestamped_output = ""
untimestamped_output = ""

for time, data in res.items():
    timestamped_output+=f"({time}) {data["speaker"]}: {data["text"]}\n"
om.save_text_file("transcription_timestamped_output", str(timestamped_output))

    
for time, data in res.items():
    untimestamped_output+=f"{data["speaker"]}: {data["text"]}\n"
om.save_text_file("transcription_untimestamped_output", str(untimestamped_output))

if (timestamps):
    temp = timestamped_output
else:
    temp = untimestamped_output
    
# om.save_text_file("output", str(temp))

Nayahath.action("Summarizer", "Starting first processing.")
summarized_output = summarizer.summarize(str(temp))
om.save_text_file("summarized_output", str(summarized_output))

Nayahath.action("Nayahath", "Pipeline completed.")

ending_time = datetime.datetime.now().strftime("%H:%M:%S")

om.save_text_file("pipeline_config", f'''Timestamps: {timestamps}
Diarization model checkpoint: pyannote/speaker-diarization-community-1 
Transcription model: Whisper (turbo)
Summarization model: {summarizer_model}
Starts at: {starting_time}
Ends at: {ending_time}

Operational System: Ubuntu 22.04 (WSL2)
Python version: 3.12.3 (RUNNING IN VIRTUAL ENVIRONMENT)

Processor: Ryzen 5 4600G
RAM: 16GB
                  ''')

om.save_text_file("python_dependencies", '''aiohappyeyeballs==2.6.1
aiohttp==3.13.2
aiosignal==1.4.0
alembic==1.17.2
annotated-types==0.7.0
anyio==4.12.0
asteroid-filterbanks==0.4.0
attrs==25.4.0
certifi==2025.11.12
cffi==2.0.0
charset-normalizer==3.4.4
click==8.3.1
colorlog==6.10.1
contourpy==1.3.3
cycler==0.12.1
einops==0.8.1
ffmpeg-python==0.2.0
filelock==3.20.0
fonttools==4.61.0
frozenlist==1.8.0
fsspec==2025.10.0
future==1.0.0
googleapis-common-protos==1.72.0
greenlet==3.2.4
grpcio==1.76.0
h11==0.16.0
hf-xet==1.2.0
httpcore==1.0.9
httpx==0.28.1
huggingface_hub==1.1.7
idna==3.11
importlib_metadata==8.7.0
Jinja2==3.1.6
joblib==1.5.2
julius==0.2.7
kiwisolver==1.4.9
lightning==2.6.0
lightning-utilities==0.15.2
llvmlite==0.45.1
Mako==1.3.10
markdown-it-py==4.0.0
MarkupSafe==3.0.3
matplotlib==3.10.7
mdurl==0.1.2
more-itertools==10.8.0
mpmath==1.3.0
multidict==6.7.0
networkx==3.6
numba==0.62.1
numpy==2.3.5
nvidia-cublas-cu12==12.8.4.1
nvidia-cuda-cupti-cu12==12.8.90
nvidia-cuda-nvrtc-cu12==12.8.93
nvidia-cuda-runtime-cu12==12.8.90
nvidia-cudnn-cu12==9.10.2.21
nvidia-cufft-cu12==11.3.3.83
nvidia-cufile-cu12==1.13.1.3
nvidia-curand-cu12==10.3.9.90
nvidia-cusolver-cu12==11.7.3.90
nvidia-cusparse-cu12==12.5.8.93
nvidia-cusparselt-cu12==0.7.1
nvidia-nccl-cu12==2.27.3
nvidia-nvjitlink-cu12==12.8.93
nvidia-nvshmem-cu12==3.3.20
nvidia-nvtx-cu12==12.8.90
ollama==0.6.1
openai-whisper==20250625
opentelemetry-api==1.39.0
opentelemetry-exporter-otlp==1.39.0
opentelemetry-exporter-otlp-proto-common==1.39.0
opentelemetry-exporter-otlp-proto-grpc==1.39.0
opentelemetry-exporter-otlp-proto-http==1.39.0
opentelemetry-proto==1.39.0
opentelemetry-sdk==1.39.0
opentelemetry-semantic-conventions==0.60b0
optuna==4.6.0
packaging==25.0
pandas==2.3.3
pillow==12.0.0
primePy==1.3
propcache==0.4.1
protobuf==6.33.1
pyannote-audio==4.0.2
pyannote-core==6.0.1
pyannote-database==6.1.0
pyannote-metrics==4.0.0
pyannote-pipeline==4.0.0
pyannoteai-sdk==0.3.0
pycparser==2.23
pydantic==2.12.5
pydantic_core==2.41.5
Pygments==2.19.2
pyparsing==3.2.5
python-dateutil==2.9.0.post0
pytorch-lightning==2.6.0
pytorch-metric-learning==2.9.0
pytz==2025.2
PyYAML==6.0.3
regex==2025.11.3
requests==2.32.5
rich==14.2.0
safetensors==0.7.0
scikit-learn==1.7.2
scipy==1.16.3
semantic-version==2.10.0
setuptools==80.9.0
setuptools-rust==1.12.0
shellingham==1.5.4
six==1.17.0
sortedcontainers==2.4.0
soundfile==0.13.1
SQLAlchemy==2.0.44
sympy==1.14.0
threadpoolctl==3.6.0
tiktoken==0.12.0
torch==2.8.0
torch-audiomentations==0.12.0
torch_pitch_shift==1.2.5
torchaudio==2.8.0
torchcodec==0.7.0
torchmetrics==1.8.2
tqdm==4.67.1
triton==3.4.0
typer-slim==0.20.0
typing-inspection==0.4.2
typing_extensions==4.15.0
tzdata==2025.2
urllib3==2.5.0
yarl==1.22.0
zipp==3.23.0
                  ''')