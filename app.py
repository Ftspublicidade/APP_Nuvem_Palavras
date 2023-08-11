import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io
import base64

def generate_wordcloud(text):
    # Gera a nuvem de palavras
    wordcloud = WordCloud(width=800, height=800, background_color="white").generate(text)

    # Gera a imagem da nuvem de palavras
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)

    # Salva a imagem em um buffer
    image_buffer = io.BytesIO()
    plt.savefig(image_buffer, format="png")
    image_buffer.seek(0)
    return image_buffer

def main():
    st.title("Nuvem de Palavras a partir de Texto")

    # Upload do arquivo de texto
    uploaded_file = st.file_uploader("Faça o upload de um arquivo de texto", type=["txt"])

    if uploaded_file is not None:
        st.write("Arquivo carregado com sucesso!")

        # Lê o conteúdo do arquivo de texto
        text = uploaded_file.read().decode("utf-8")  # Decodifica os bytes em texto

        # Exibe o conteúdo do arquivo de texto
        st.subheader("Texto carregado:")
        st.write(text)

        # Verifica se o botão de geração da nuvem de palavras foi pressionado
        if st.button("Gerar Nuvem de Palavras"):
            # Gera a nuvem de palavras
            image_buffer = generate_wordcloud(text)

            # Exibe a nuvem de palavras gerada
            st.subheader("Nuvem de Palavras Gerada:")
            st.image(image_buffer, use_column_width=True, caption="Nuvem de Palavras")

            
            

if __name__ == "__main__":
    main()