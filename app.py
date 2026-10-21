import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Principal primeiro; o reserva só é usado se o principal falhar (ex.: 503 em horário de pico)
MODELOS = ["gemini-3.8-flash", "gemini-3.5-flash"]


def perguntar_ia(pergunta):
    """Tenta cada modelo em ordem. Devolve (texto, modelo) ou (None, None) se todos falharem."""
    for modelo in MODELOS:
        try:
            resposta = client.models.generate_content(model=modelo, contents=pergunta)
            return resposta.text, modelo
        except Exception as erro:
            # Aparece só no terminal, para quem está desenvolvendo
            print(f"[IA] {modelo} falhou: {erro}")
    return None, None


st.title("Teste HackaRun")
pergunta = st.text_input("Pergunte algo para a IA")
if pergunta:
    with st.spinner("Pensando..."):
        texto, modelo = perguntar_ia(pergunta)
    if texto:
        st.write(texto)
        st.caption(f"Respondido por {modelo}")
    else:
        st.error("A IA está indisponível no momento. Tente de novo em alguns segundos.")
