import streamlit as st
import openai

def generar_texto(prompt, api_key, max_tokens=4096, temperature=0.8):
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
    asunto = st.text_input("Ingresa el asunto del e-mail")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Generar e-mail") and api_key:
        prompt = f"Asunto del e-mail: {asunto}"
        email = generar_texto(prompt, api_key, max_tokens=3950)
        
        st.success("E-mail generado:")
        st.write(email)

def responder_emails():
    st.title("Responder a e-mails")
    prompt = st.text_area("Ingresa el e-mail recibido")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Responder al e-mail") and api_key:
        email = generar_texto(prompt, api_key, max_tokens=3950, temperature=0.5)
        
        st.success("Respuesta generada:")
        st.write(email)

def corrector_estilo():
    st.title("Corrector de estilo")
    prompt = st.text_area("Ingresa el texto a corregir")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Corregir estilo") and api_key:
        correccion = generar_texto(prompt, api_key, max_tokens=3950)
        
        st.success("Texto corregido:")
        st.write(correccion)

def generador_mensajes_facebook():
    st.title("Generador de mensajes de Facebook")
    prompt = st.text_area("Ingresa el título del mensaje")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Generar mensaje") and api_key:
        mensaje = generar_texto(prompt, api_key, max_tokens=3950)
        
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
    prompt = st.text_area("Ingresa el título del mensaje")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Generar mensaje") and api_key:
        mensaje = generar_texto(prompt, api_key, max_tokens=2200)
        
        st.success("Mensaje generado:")
        st.write(mensaje)

def generador_mensajes_linkedin():
    st.title("Generador de mensajes de LinkedIn")
    prompt = st.text_area("Ingresa el inicio del mensaje")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Generar mensaje") and api_key:
        mensaje = generar_texto(prompt, api_key, max_tokens=280)
        
        st.success("Mensaje generado:")
        st.write(mensaje)

def generador_ensayos():
    st.title("Generador de ensayos")
    prompt = st.text_area("Ingresa el título del ensayo")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Generar ensayo") and api_key:
        prompt += "\n\nLongitud del ensayo: Largo"
        ensayo = generar_texto(prompt, api_key, max_tokens=4000)
        
        st.success("Ensayo generado:")
        st.write(ensayo)

def expansor():
    st.title("Expansor")
    prompt = st.text_area("Ingresa el texto a expandir")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Expandir texto") and api_key:
        texto_expandido = generar_texto(prompt, api_key, max_tokens=4000)
        
        st.success("Texto expandido:")
        st.write(texto_expandido)

def parafraseador():
    st.title("Parafraseador")
    prompt = st.text_area("Ingresa el texto a parafrasear")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Parafrasear texto") and api_key:
        texto_parafraseado = generar_texto(prompt, api_key, max_tokens=4000)
        
        st.success("Texto parafraseado:")
        st.write(texto_parafraseado)

def main():
    st.sidebar.title("Aplicaciones")
    app = st.sidebar.selectbox(
        "Selecciona una aplicación",
        ("Generador de e-mails nuevos", "Responder a e-mails", "Corrector de estilo", "Generador de mensajes de Facebook", "Generador de mensajes de Twitter", "Generador de mensajes de Instagram", "Generador de mensajes de LinkedIn", "Generador de ensayos", "Expansor", "Parafraseador")
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
    elif app == "Generador de mensajes de LinkedIn":
        generador_mensajes_linkedin()
    elif app == "Generador de ensayos":
        generador_ensayos()
    elif app == "Expansor":
        expansor()
    elif app == "Parafraseador":
        parafraseador()

if __name__ == "__main__":
    main()
