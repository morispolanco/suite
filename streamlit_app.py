import streamlit as st
import openai

def generar_texto(prompt, api_key, max_tokens=4096, temperature=0.7):
    openai.api_key = api_key
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=temperature
    )
    
    return response.choices[0].text.strip()

def resumir_texto(texto, api_key):
    prompt = f"Resumir el siguiente texto:\n\n{texto}"
    resumen = generar_texto(prompt, api_key, max_tokens=512, temperature=0.5)
    
    return resumen

def expandir_texto(texto, api_key):
    prompt = f"Expandir el siguiente texto:\n\n{texto}"
    expansion = generar_texto(prompt, api_key, max_tokens=4000, temperature=0.7)
    
    return expansion

def parafrasear_texto(texto, api_key):
    prompt = f"Parafrasear el siguiente texto:\n\n{texto}"
    parafraseo = generar_texto(prompt, api_key, max_tokens=4000, temperature=0.7)
    
    return parafraseo

def generador_ensayos():
    st.title("Generador de ensayos")
    prompt = st.text_area("Ingresa el título del ensayo")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Generar ensayo") and api_key:
        ensayo = generar_texto(prompt, api_key, max_tokens=4000)
        
        st.success("Ensayo generado:")
        st.write(ensayo)

        if st.checkbox("Resumir ensayo"):
            resumen = resumir_texto(ensayo, api_key)
            st.success("Resumen del ensayo:")
            st.write(resumen)

        if st.checkbox("Expandir ensayo"):
            expansion = expandir_texto(ensayo, api_key)
            st.success("Expansión del ensayo:")
            st.write(expansion)

        if st.checkbox("Parafrasear ensayo"):
            parafraseo = parafrasear_texto(ensayo, api_key)
            st.success("Parafraseo del ensayo:")
            st.write(parafraseo)

def generador_columnas_periodisticas():
    st.title("Generador de columnas periodísticas")
    prompt = st.text_area("Ingresa el título de la columna")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Generar columna") and api_key:
        columna = generar_texto(prompt, api_key, max_tokens=4000)
        
        st.success("Columna generada:")
        st.write(columna)

        if st.checkbox("Resumir columna"):
            resumen = resumir_texto(columna, api_key)
            st.success("Resumen de la columna:")
            st.write(resumen)

        if st.checkbox("Expandir columna"):
            expansion = expandir_texto(columna, api_key)
            st.success("Expansión de la columna:")
            st.write(expansion)

        if st.checkbox("Parafrasear columna"):
            parafraseo = parafrasear_texto(columna, api_key)
            st.success("Parafraseo de la columna:")
            st.write(parafraseo)

def generador_articulos():
    st.title("Generador de artículos")
    prompt = st.text_area("Ingresa el título del artículo")
    
    api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
    
    if st.button("Generar artículo") and api_key:
        articulo = generar_texto(prompt, api_key, max_tokens=4000)
        
        st.success("Artículo generado:")
        st.write(articulo)

        if st.checkbox("Resumir artículo"):
            resumen = resumir_texto(articulo, api_key)
            st.success("Resumen del artículo:")
            st.write(resumen)

        if st.checkbox("Expandir artículo"):
            expansion = expandir_texto(articulo, api_key)
            st.success("Expansión del artículo:")
            st.write(expansion)

        if st.checkbox("Parafrasear artículo"):
            parafraseo = parafrasear_texto(articulo, api_key)
            st.success("Parafraseo del artículo:")
            st.write(parafraseo)

def main():
    st.sidebar.title("Aplicaciones")
    app = st.sidebar.selectbox(
        "Selecciona una aplicación",
        ("Generador de ensayos", "Generador de columnas periodísticas", "Generador de artículos")
    )
    
    if app == "Generador de ensayos":
        generador_ensayos()
    elif app == "Generador de columnas periodísticas":
        generador_columnas_periodisticas()
    elif app == "Generador de artículos":
        generador_articulos()

if __name__ == "__main__":
    main()
