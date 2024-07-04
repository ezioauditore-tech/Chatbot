from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import soundfile as sf
import config

class TextToSpeech:
    def __init__(self):
        self.processor = SpeechT5Processor.from_pretrained(config.MODEL_NAME)
        self.model = SpeechT5ForTextToSpeech.from_pretrained(config.MODEL_NAME)
        self.vocoder = SpeechT5HifiGan.from_pretrained(config.VOCODER_NAME)
        self.embeddings_dataset = load_dataset(config.EMBEDDINGS_DATASET, split="validation")
        self.speaker_embeddings = torch.tensor(self.embeddings_dataset[config.SPEAKER_INDEX]["xvector"]).unsqueeze(0)

    def generate_speech(self, text):
        inputs = self.processor(text=text, return_tensors="pt")
        speech = self.model.generate_speech(inputs["input_ids"], self.speaker_embeddings, vocoder=self.vocoder)
        sf.write(config.OUTPUT_FILE, speech.numpy(), samplerate=config.SAMPLERATE)
        
        return config.OUTPUT_FILE
