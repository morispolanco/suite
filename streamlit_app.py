import streamlit as st
import openai

def generar_texto(prompt, api_key):
    openai.api_key = api_key
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.7
    )
    
    return response.choices[0].text.strip()

def corrector_estilo():
    st.title("Corrector de estilo de español")
    texto = st.text_area("Ingresa el texto a corregir")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Corregir") and api_key:
        prompt = f"Corrige el siguiente texto:\n\n{texto}"
        correccion = generar_texto(prompt, api_key)
        
        st.success("Texto corregido:")
        st.write(correccion)

def clasificar_longitud(respuesta):
    longitud = len(respuesta)
    
    if longitud < 50:
        return "Corta"
    elif longitud < 150:
        return "Mediana"
    else:
        return "Larga"

def generador_emails():
    st.title("Generador de e-mails")
    prompt = st.text_area("Ingresa el inicio del e-mail")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    correo_respuesta = st.text_input("Ingresa el correo al que quieres responder")
    
    intencion_respuesta = st.text_input("Ingresa la intención de la respuesta")
    
    if st.button("Generar e-mail") and api_key:
        prompt += f"\n\nResponder a: {correo_respuesta}\nIntención de la respuesta: {intencion_respuesta}"
        email = generar_texto(prompt, api_key)
        longitud_respuesta = clasificar_longitud(email)
        
        st.success("E-mail generado:")
        st.write(email)
        st.write(f"Longitud de la respuesta: {longitud_respuesta}")

def main():
    st.sidebar.title("Aplicaciones")
    app = st.sidebar.selectbox(
        "Selecciona una aplicación",
        ("Generador de e-mails",)
    )
    
    if app == "Generador de e-mails":
        generador_emails()

def generador_post_blog():
    st.title("Generador de post de blog")
    prompt = st.text_area("Ingresa el inicio del post de blog")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Generar post") and api_key:
        post = generar_texto(prompt, api_key)
        
        st.success("Post generado:")
        st.write(post)

def generador_mensajes_facebook():
    st.title("Generador de mensajes de Facebook")
    prompt = st.text_area("Ingresa el inicio del mensaje")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Generar mensaje") and api_key:
        mensaje = generar_texto(prompt, api_key)
        
        st.success("Mensaje generado:")
        st.write(mensaje)

def generador_mensajes_instagram():
    st.title("Generador de mensajes de Instagram")
    prompt = st.text_area("Ingresa el inicio del mensaje")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Generar mensaje") and api_key:
        mensaje = generar_texto(prompt, api_key)
        
        st.success("Mensaje generado:")
        st.write(mensaje)

def generador_mensajes_twitter():
    st.title("Generador de mensajes de Twitter")
    prompt = st.text_area("Ingresa el inicio del mensaje")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Generar mensaje") and api_key:
        mensaje = generar_texto(prompt, api_key)
        
        st.success("Mensaje generado:")
        st.write(mensaje)

def generador_mensajes_linkedin():
    st.title("Generador de mensajes de LinkedIn")
    prompt = st.text_area("Ingresa el inicio del mensaje")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Generar mensaje") and api_key:
        mensaje = generar_texto(prompt, api_key)
        
        st.success("Mensaje generado:")
        st.write(mensaje)

def generador_articulos():
    st.title("Generador de artículos")
    prompt = st.text_area("Ingresa el inicio del artículo")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Generar artículo") and api_key:
        articulo = generar_texto(prompt, api_key)
        
        st.success("Artículo generado:")
        st.write(articulo)

def generador_columnas_periodisticas():
    st.title("Generador de columnas periodísticas")
    prompt = st.text_area("Ingresa el inicio de la columna periodística")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Generar columna") and api_key:
        columna = generar_texto(prompt, api_key)
        
        st.success("Columna generada:")
        st.write(columna)

def generador_ensayos_libres():
    st.title("Generador de ensayos libres")
    prompt = st.text_area("Ingresa el inicio del ensayo")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Generar ensayo") and api_key:
        ensayo = generar_texto(prompt, api_key)
        
        st.success("Ensayo generado:")
        st.write(ensayo)

def main():
    st.sidebar.title("Aplicaciones")
    app = st.sidebar.selectbox(
        "Selecciona una aplicación",
        ("Corrector de estilo", "Generador de e-mails", "Generador de post de blog",
         "Generador de mensajes de Facebook", "Generador de mensajes de Instagram",
         "Generador de mensajes de Twitter", "Generador de mensajes de LinkedIn",
         "Generador de artículos", "Generador de columnas periodísticas", "Generador de ensayos libres")
    )
    
    if app == "Corrector de estilo":
        corrector_estilo()
    elif app == "Generador de e-mails":
        generador_emails()
    elif app == "Generador de post de blog":
        generador_post_blog()
    elif app == "Generador de mensajes de Facebook":
        generador_mensajes_facebook()
    elif app == "Generador de mensajes de Instagram":
        generador_mensajes_instagram()
    elif app == "Generador de mensajes de Twitter":
        generador_mensajes_twitter()
    elif app == "Generador de mensajes de LinkedIn":
        generador_mensajes_linkedin()
    elif app == "Generador de artículos":
        generador_articulos()
    elif app == "Generador de columnas periodísticas":
        generador_columnas_periodisticas()
    elif app == "Generador de ensayos libres":
        generador_ensayos_libres()

if __name__ == "__main__":
    main()
