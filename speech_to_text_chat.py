# imports
import time
from transformers import AutoProcessor, SeamlessM4Tv2Model
import logging
import pyaudio
import numpy as np
import torch
import pyttsx3 as pyttsx3
from langchain_cohere import ChatCohere
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
import time
import eel

import speech_recognition as sr

load_dotenv() ## take environment variables from .env(langchain api key, cohere api key)


# ChatCohere llm
ChatCohere_llm = ChatCohere(cohere_api_key=os.environ["COHERE_API_KEY"], temperature=0.5)

chat_flow = [SystemMessage(content="You are a chatting AI assistant")] #store chat message history for a session

def get_ChatCohere_response(human_question):

    (chat_flow).append(HumanMessage(content=human_question))
    ai_answer = ChatCohere_llm(chat_flow)
    (chat_flow).append(AIMessage(content=ai_answer.content))

    return ai_answer.content

# speech to text processing model
# logging.info("seamless-m4t-v2.main()")

# processor = AutoProcessor.from_pretrained("facebook/seamless-m4t-v2-large")
# model = SeamlessM4Tv2Model.from_pretrained("facebook/seamless-m4t-v2-large")


# logging.basicConfig(level=logging.INFO, format='%(asctime)-15s %(levelname)s %(message)s')
@eel.expose
def welcome():
    print("Welcome, how can I help you?")
    eel.welcomeMessage("Welcome, how can I help you?")
    response_to_audio("Welcome, how can I help you?")

@eel.expose
def goodbye():
    print("Goodbye!")
    eel.goodbyeMessage("Goodbye!")


# @eel.expose
# def stopListening(is_running):
#     global is_listening 
#     is_listening = is_running


@eel.expose
def main():
    # print("main")
    # pass
#    while True:
#         eel.askMessage("Ask...")
#         time.sleep(2)
#         eel.assistantMessage("<h4>ASSISTANT</h4>response fron the personal assistant")
#         time.sleep(3)
#         eel.userMessage("<h4>YOU</h4>query asked by the user")
#         time.sleep(3)

    # sampling_rate = 16000
    # record_time_in_seconds = 5.0
    # number_of_samples = round(record_time_in_seconds * sampling_rate)
    # mic_stream = pyaudio.PyAudio().open(format=pyaudio.paInt16,
    #                                     channels=1,
    #                                     rate=sampling_rate,
    #                                     input=True,
    #                                     frames_per_buffer=number_of_samples)
    
    
    end_of_conversation = False
    while not end_of_conversation:
        # print("Ask!"
        # eel.askMessage("Ask...")
        # transcription = get_sentence(mic_stream, processor, model, sampling_rate)
        transcription = get_sentence()
        
        # if transcription.lower().replace('.', '').replace('!', '') == ("Thank you and goodbye").lower():
        if transcription.lower().replace('.', '').replace('!', '').replace(" ", "") == ("Thankyouandgoodbye").lower():
            logging.info(f"voice_assistant_service.main(): End of conversation")
            end_of_conversation = True
        else:
            sentence_is_gibberish = False
            if transcription[0] == '[':
                sentence_is_gibberish = True
            # for prefix in ["i'm going to ", "the first ", "it's a ", "hello", "it's ", "and "]:
            #     if transcription.lower().startswith(prefix):
            #         sentence_is_gibberish = True
            if len(transcription) > 15 and not sentence_is_gibberish:
                eel.userMessage(f"<h4>YOU</h4>{transcription}")
                response = get_ChatCohere_response(transcription)
                print("=="*40)
                print(f"Cohere Assistant : {response}")
                eel.assistantMessage(f"<h4>ASSISTANT</h4>{response}")
                response_to_audio(response)
                print("=="*40)

            time.sleep(1)              
    goodbye()

# @eel.expose
# def getSelectedLanguage(selected_language):
#     print(str(selected_language))
#     return str(selected_language).lower()

@eel.expose
def get_sentence():
    recognizer = sr.Recognizer()
    with sr.Microphone() as audio_source:
        print("Ask...")
        eel.askMessage("Ask...")
        audio = recognizer.listen(audio_source)
        try:
            # audio_to_text = recognizer.recognize_google(audio)
            transcription = recognizer.recognize_whisper(audio, language=str(eel.getSelectedLanguage()()).lower(), translate=True)
            if transcription:
                print(transcription)
                return(transcription)
            # else:
            #     print("end of convo")
        except Exception as e:
            print(e)


# def get_sentence(mic_stream, stt_processor, stt_model, sampling_rate):
#     chunks = []
#     speech_has_started = False
#     chunk_length = round(1.0 * sampling_rate)
#     #logging.info(f"voice_assistant_service.get_sentence(): chunk_length = {chunk_length}")
#     while not speech_has_started:
#         current_chunk_arr = np.frombuffer(mic_stream.read(chunk_length), dtype=np.int16)
#         std = np.std(current_chunk_arr)
#         if std >= 100:
#             speech_has_started = True
#             chunks.append(current_chunk_arr)

#     speech_has_stopped = False
#     while not speech_has_stopped:
#         current_chunk_arr = np.frombuffer(mic_stream.read(chunk_length), dtype=np.int16)
#         std = np.std(current_chunk_arr)
#         if std < 100:
#             chunks.append(current_chunk_arr)
#             speech_has_stopped = True
#         else:
#             chunks.append(current_chunk_arr)

#     logging.info(f"voice_assistant_service.get_sentence(): len(chunks) = {len(chunks)}")
#     speech_arr = np.concatenate(chunks)
#     speech_tsr = torch.from_numpy(speech_arr)

#     transcription = None
#     audio_inputs = stt_processor(audios=speech_tsr, return_tensors="pt")
#     output_tokens = stt_model.generate(**audio_inputs, tgt_lang="eng", generate_speech=False)
#     transcription = stt_processor.decode(output_tokens[0].tolist()[0], skip_special_tokens=True)
#     print("**"*40)
#     print(f"YOU : {transcription}")
#     # eel.userMessage(f"<h4>YOU</h4>{transcription}")
#     print("**"*40)
#     return transcription

@eel.expose
def response_to_audio(text):
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()

@eel.expose
def text_message_response(text_message):
    print(text_message)
    eel.userMessage(f"<h4>YOU</h4>{text_message}")
    response = get_ChatCohere_response(text_message)
    eel.assistantMessage(f"<h4>ASSISTANT</h4>{response}")
    # print(eel.getSelectedLanguage()())

     
# eel.init("web_copy_2")
# eel.start("index_copy_2.html")