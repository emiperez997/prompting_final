import streamlit as st
from openai import OpenAI
import dotenv
import os

dotenv.load_dotenv()
OpenAIKey = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OpenAIKey)

def generate_history(words, limit_words):
    # Generar el prompt
    prompt = f"Crea una historia con las siguientes palabras:\n{words}\n\n---\n\n"

    # Generar la respuesta
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        max_tokens=limit_words * 2,
    )

    # Obtener la respuesta
    response = response.choices[0].message.content

    # Cortar la respuesta hasta el ultimo punto
    if response:
        response = response.split(".")
        response = ".".join(response[:-1]) + "." # Agregar el punto final
        return response

    # Retornar la respuesta
    return response

def main():

    # Título
    st.title("Generador de historias")

    # Instrucciones de uso
    st.text("Instrucciones de uso:")
    st.text("1. Escribe algunas palabras")
    st.text("2. Selecciona el límite de palabras")
    st.text("3. Presiona el botón de generar")
    st.text("4. ¡Listo! Se generará una historia con las palabras dadas")

    # Divisor
    st.divider()


    st.text("Escribe algunas palabras y te ayudaré a generar una historia")
    # Obtener las palabras como maximo 5  
    words = st.text_input("Palabras", max_chars=80) 

    limit_words = st.slider("Límite de respuesta", 50, 100, 100)

    # Generar la historia
    if st.button("Generar"):
        story = generate_history(words, limit_words)
        st.write(story)

if __name__ == "__main__":
    main()
