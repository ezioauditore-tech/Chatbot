import streamlit as st
from gen import falcon_chain, extract_response
from text_to_speech import TextToSpeech
import config
import base64

# Initialize the Text-to-Speech engine
tts_engine = TextToSpeech()

# Define Streamlit App
def main():
    st.title("AI Chatbot")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Get user input
    user_input = st.chat_input("You:")
    
    if user_input:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
        
        # Generate AI response
        full_response = falcon_chain.run({"question": user_input})
        
        # Extract only the response using regex
        response = extract_response(full_response)
        
        # Add AI response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)
        
        # Generate and play speech
        speech_file = tts_engine.generate_speech(response)
        audio_bytes = open(speech_file, "rb").read()
        audio_base64 = base64.b64encode(audio_bytes).decode()
        audio_html = f"""
        <audio autoplay>
            <source src="data:audio/wav;base64,{audio_base64}" type="audio/wav">
        </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
