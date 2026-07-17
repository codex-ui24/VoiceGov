import os
import sounddevice as sd
from scipy.io.wavfile import write
from sarvamai import SarvamAI

API_KEY = os.getenv("SARVAM_API_KEY")

client = SarvamAI(api_subscription_key=API_KEY)

FS = 16000
SECONDS = 8


def record_audio():

    filename = "complaint.wav"

    input("Press Enter and start speaking...")

    print("Recording...")

    recording = sd.rec(
        int(FS * SECONDS),
        samplerate=FS,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    write(filename, FS, recording)

    print("Recording completed.")

    return filename


def transcribe_audio(audio_path):

    with open(audio_path, "rb") as audio:

        response = client.speech_to_text.transcribe(
            file=audio,
            model="saaras:v3",
            mode="transcribe",
            language_code=None,
            input_audio_codec="wav"
        )

    return response.transcript