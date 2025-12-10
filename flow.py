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
                  ''')