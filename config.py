import os

# Set up your HuggingFace API key
os.environ['API_KEY'] = 'YOUR_API_KEY'

# Falcon-7B-Instruct model configuration
model_id = 'tiiuae/falcon-7b-instruct'
model_kwargs = {"temperature": 0.8, "max_new_tokens": 2000}

# Text-to-Speech configuration
MODEL_NAME = "microsoft/speecht5_tts"
VOCODER_NAME = "microsoft/speecht5_hifigan"
EMBEDDINGS_DATASET = "Matthijs/cmu-arctic-xvectors"
SPEAKER_INDEX = 10
SAMPLERATE = 16000
OUTPUT_FILE = "speech.wav"
