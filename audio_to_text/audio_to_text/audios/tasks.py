import whisper
from celery import shared_task


@shared_task
def transcribe_audio(audio_file_path):
    model = whisper.load_model("base")
    transcription = model.transcribe(audio_file_path, fp16=False)
    return transcription['text']
