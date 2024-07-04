
# AI Chatbot with Text-to-Speech

This project is a Streamlit-based AI chatbot that uses the Falcon-7B model for generating responses and SpeechT5 for text-to-speech conversion. The chatbot can automatically play audio responses after generating text responses.

## Features

- **Chat Interface**: A simple chat interface for user interaction.
- **AI Response Generation**: Uses the Falcon-7B model to generate responses to user queries.
- **Text-to-Speech**: Converts the generated text responses to speech using SpeechT5 and HiFi-GAN.

## Installation

1. Clone the repository.

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set your Hugging Face API key:
    ```sh
    export HUGGINGFACEHUB_API_TOKEN='your_hugging_face_api_key'  # On Windows use `set HUGGINGFACEHUB_API_TOKEN=your_hugging_face_api_key`
    ```

## Configuration

You can change the models in the `config.py` file in the root directory.
```python
# config.py

MODEL_NAME = "microsoft/speecht5_tts"
VOCODER_NAME = "microsoft/speecht5_hifigan"
EMBEDDINGS_DATASET = "Matthijs/cmu-arctic-xvectors"
SPEAKER_INDEX = 10
SAMPLERATE = 16000
OUTPUT_FILE = "speech.wav"
```
## Usage
Run the Streamlit app:

```
streamlit run streamlit-app.py
```
Open your web browser and navigate to http://localhost:8501.

Interact with the chatbot and listen to the automatic speech responses.

