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

def presentacion():
    st.title("Suite de aplicaciones de lenguaje")
    st.write("¡Bienvenido a la Suite de aplicaciones de lenguaje!")
    st.write("Esta suite contiene varias aplicaciones de procesamiento de lenguaje natural para ayudarte con diferentes tareas.")
    st.write("- Generador de e-mails nuevos: Genera e-mails nuevos con un asunto, tono y longitud personalizados.")
    st.write("- Responder a e-mails: Genera respuestas a e-mails recibidos con una intención, tono y longitud personalizados.")
    st.write("- Corrector de estilo: Corrige el estilo de un texto para mejorarlo.")
    st.write("- Generador de mensajes de Facebook: Genera mensajes para publicaciones en Facebook.")
    st.write("- Generador de mensajes de Twitter: Genera mensajes para publicaciones en Twitter.")
    st.write("- Generador de mensajes de Instagram: Genera mensajes para publicaciones en Instagram.")
    st.write("- Generador de mensajes de LinkedIn: Genera mensajes para publicaciones en LinkedIn.")
    st.write("- Generador de ensayos: Genera ensayos con un título personalizado.")
    st.write("- Expansor: Expande un texto para hacerlo más largo.")
    st.write("- Parafraseador: Parafrasea un texto para expresarlo de manera diferente.")
    
def generador_emails_nuevos():
    st.title("Generador de e-mails nuevos")
    asunto = st.text_input("Ingresa el asunto del e-mail")
    tono = st.selectbox("Selecciona el tono del e-mail", ("Formal", "Informal"))
    longitud = st.slider("Selecciona la longitud del e-mail", 50, 500, 150)
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Generar e-mail") and api_key:
        prompt = f"Asunto del e-mail: {asunto}\nTono del e-mail: {tono}\nLongitud del e-mail: {longitud}"
        max_tokens = 0
        if longitud == "Corto":
            max_tokens = 100
        elif longitud == "Mediano":
            max_tokens = 200
        elif longitud == "Largo":
            max_tokens = 300
        email = generar_texto(prompt, api_key, max_tokens=max_tokens)
        
        st.success("E-mail generado:")
        st.write(email)

def responder_emails():
    st.title("Responder a e-mails")
    prompt = st.text_area("Ingresa el e-mail recibido")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    intencion_respuesta = st.text_input("Ingresa la intención de la respuesta")
    tono_respuesta = st.selectbox("Selecciona el tono de la respuesta", ("Formal", "Informal"))
    longitud_respuesta = st.slider("Selecciona la longitud de la respuesta", 50, 500, 150)
    
    if st.button("Responder al e-mail") and api_key:
        prompt += f"\n\nIntención de la respuesta: {intencion_respuesta}\nTono de la respuesta: {tono_respuesta}\nLongitud de la respuesta: {longitud_respuesta}"
        max_tokens = 0
        if longitud_respuesta == "Corta":
            max_tokens = 100
        elif longitud_respuesta == "Mediana":
            max_tokens = 200
        elif longitud_respuesta == "Larga":
            max_tokens = 300
        respuesta = generar_texto(prompt, api_key, max_tokens=max_tokens, temperature=0.5)
        
        st.success("Respuesta generada:")
        st.write(respuesta)


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
