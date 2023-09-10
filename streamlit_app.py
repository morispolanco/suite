import streamlit as st
import openai

def generar_texto(prompt, api_key, max_tokens=4096, temperature=0.7):
    openai.api_key = api_key
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens - 20,
        n=1,
        stop=None,
        temperature=temperature
    )
    
    return response.choices[0].text.strip()

def clasificar_longitud(respuesta):
    longitud = len(respuesta)
    
    if longitud < 50:
        return "Corta"
    elif longitud < 150:
        return "Mediana"
    else:
        return "Larga"

def clasificar_extension(respuesta):
    palabras = respuesta.split()
    num_palabras = len(palabras)
    
    if num_palabras < 10:
        return "Breve"
    elif num_palabras < 20:
        return "Moderada"
    else:
        return "Extensa"

def generador_emails_nuevos():
    st.title("Generador de e-mails nuevos")
    prompt = st.text_area("Ingresa el asunto del e-mail")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    asunto_respuesta = st.text_input("Ingresa el asunto de la respuesta")
    
    tono_respuesta = st.selectbox("Selecciona el tono de la respuesta", ("Formal", "Informal"))
    
    if st.button("Generar e-mail") and api_key:
        prompt += f"\n\nAsunto de la respuesta: {asunto_respuesta}\nTono de la respuesta: {tono_respuesta}"
        email = generar_texto(prompt, api_key)
        longitud_respuesta = clasificar_longitud(email)
        extension_respuesta = clasificar_extension(email)
        
        st.success("E-mail generado:")
        st.write(email)
        st.write(f"Asunto de la respuesta: {asunto_respuesta}")
        st.write(f"Tono de la respuesta: {tono_respuesta}")
        st.write(f"Longitud de la respuesta: {longitud_respuesta}")
        st.write(f"Extensión de la respuesta: {extension_respuesta}")

def responder_emails():
    st.title("Responder a e-mails")
    prompt = st.text_area("Ingresa el e-mail recibido")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    intencion_respuesta = st.text_input("Ingresa la intención de la respuesta")
    
    tono_respuesta = st.selectbox("Selecciona el tono de la respuesta", ("Formal", "Informal"))
    
    if st.button("Responder al e-mail") and api_key:
        prompt += f"\n\nIntención de la respuesta: {intencion_respuesta}\nTono de la respuesta: {tono_respuesta}"
        email = generar_texto(prompt, api_key, max_tokens=4096, temperature=0.5)
        longitud_respuesta = clasificar_longitud(email)
        extension_respuesta = clasificar_extension(email)
        
        st.success("Respuesta generada:")
        st.write(email)
        st.write(f"Intención de la respuesta: {intencion_respuesta}")
        st.write(f"Tono de la respuesta: {tono_respuesta}")
        st.write(f"Longitud de la respuesta: {longitud_respuesta}")
        st.write(f"Extensión de la respuesta: {extension_respuesta}")

def corrector_estilo():
    st.title("Corrector de estilo")
    prompt = st.text_area("Ingresa el texto a corregir")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Corregir estilo") and api_key:
        correccion = generar_texto(prompt, api_key, max_tokens=4096)
        
        st.success("Texto corregido:")
        st.write(correccion)

def generador_mensajes_facebook():
    st.title("Generador de mensajes de Facebook")
    prompt = st.text_area("Ingresa e título del mensaje")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Generar mensaje") and api_key:
        mensaje = generar_texto(prompt, api_key, max_tokens=4096)
        
        st.success("Mensaje generado:")
        st.write(mensaje)

def generador_mensajes_twitter():
    st.title("Generador de mensajes de Twitter")
    prompt = st.text_area("Ingresa el inicio del mensaje")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Generar mensaje") and api_key:
        mensaje = generar_texto(prompt, api_key, max_tokens=280)
        
        st.success("Mensaje generado:")
        st.write(mensaje)

def generador_mensajes_instagram():
    st.title("Generador de mensajes de Instagram")
    prompt = st.text_area("Ingresa el títuo del mensaje")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Generar mensaje") and api_key:
        mensaje = generar_texto(prompt, api_key, max_tokens=2200)
        
        st.success("Mensaje generado:")
        st.write(mensaje)

def generador_columnas_periodisticas():
    st.title("Generador de columnas periodísticas")
    prompt = st.text_area("Ingresa el título de la columna")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Generar columna") and api_key:
        columna = generar_texto(prompt, api_key, max_tokens=8192)
        
        st.success("Columna generada:")
        st.write(columna)

def generador_articulos():
    st.title("Generador de artículos")
    prompt = st.text_area("Ingresa el titulo del artículo")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Generar artículo") and api_key:
        articulo = generar_texto(prompt, api_key, max_tokens=8192)
        
        st.success("Artículo generado:")
        st.write(articulo)

def generador_ensayos():
    st.title("Generador de ensayos")
    prompt = st.text_area("Ingresa el título del ensayo")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Generar ensayo") and api_key:
        ensayo = generar_texto(prompt, api_key, max_tokens=8192)
        
        st.success("Ensayo generado:")
        st.write(ensayo)

def main():
    st.sidebar.title("Aplicaciones")
    app = st.sidebar.selectbox(
        "Selecciona una aplicación",
        ("Generador de e-mails nuevos", "Responder a e-mails", "Corrector de estilo", "Generador de mensajes de Facebook", "Generador de mensajes de Twitter", "Generador de mensajes de Instagram", "Generador de columnas periodísticas", "Generador de artículos", "Generador de ensayos")
    )
    
    if app == "Generador de e-mails nuevos":
        generador_emails_nuevos()
    elif app == "Responder a e-mails":
        responder_emails()
    elif app == "Corrector de estilo":
        corrector_estilo()
    elif app == "Generador de mensajes de Facebook":
        generador_mensajes_facebook()
    elif app == "Generador de mensajes de Twitter":
        generador_mensajes_twitter()
    elif app == "Generador de mensajes de Instagram":
        generador_mensajes_instagram()
    elif app == "Generador de columnas periodísticas":
        generador_columnas_periodisticas()
    elif app == "Generador de artículos":
        generador_articulos()
    elif app == "Generador de ensayos":
        generador_ensayos()

if __name__ == "__main__":
    main()
