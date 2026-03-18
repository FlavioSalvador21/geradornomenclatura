import streamlit as st

# Configuração da página
st.set_page_config(page_title="Gerador de Nomenclatura v10.0", layout="wide")

st.title("🏗️ Gerador de Nomenclatura v10.0")
st.markdown("Preencha os campos abaixo para gerar o nome padronizado do criativo.")

# --- LÓGICA DE INTERFACE ---
with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        # 1 - Semana (Transforma número em WXXY26)
        num_semana = st.number_input("1. Número da Semana", min_value=1, max_value=53, step=1, value=1)
        semana_formatada = f"W{int(num_semana):02d}Y26"

        # 2 - Copy (Máximo 3 letras)
        copy = st.text_input("2. Sigla Copy (Ex: PFR)", max_chars=3).upper()

        # 3 - Editor (Máximo 3 letras)
        editor = st.text_input("3. Sigla Editor (Ex: ALX)", max_chars=3).upper()

        # 4 - Conceito
        conceito = st.text_input("4. Conceito (Ex: OFFER)").upper()

    with col2:
        # 5 - Versão (Número -> VX)
        versao_num = st.number_input("5. Número da Versão", min_value=1, step=1, value=1)
        versao_formatada = f"V{int(versao_num)}"

        # 6 - Tipo (VID / IMG / CAR)
        tipo_midia = st.selectbox("6. Tipo de Mídia", ["VID", "IMG", "CAR"])

        # 7 - Produto (Fixo POLI conforme solicitado)
        produto = "POLI"
        st.text_input("7. Produto", value=produto, disabled=True)

        # 8 - Linguagem
        linguagem = st.selectbox("8. Linguagem", ["BR", "ES"])

    with col3:
        # 9 - Formato
        formato = st.selectbox("9. Formato", ["V", "H"])

        # 10 - Tipo de Anúncio (Mapeamento de nomes para siglas)
        mapa_anuncio = {
            "MODELAGEM DE CONCORRENTE EXPANDIDO": "MCE",
            "ESTRUTURA INVISÍVEL": "EIN",
            "CONCEITO ZERO": "CZO",
            "EXPANSÃO DE ÂNGULO VALIDADO": "EAV",
            "ITERAÇÕES": "ITE"
        }
        tipo_anuncio_nome = st.selectbox("10. Tipo de Anúncio", list(mapa_anuncio.keys()))
        tipo_anuncio_sigla = mapa_anuncio[tipo_anuncio_nome]

        # 11 - Descrição
        descricao = st.text_input("11. Descrição do Vídeo").upper()

# --- MONTAGEM DA STRING FINAL ---
# O padrão solicitado: 1_2_3_4_5_6_7_8_9_10_11
# Note: Usamos colchetes para as tags e o separador " - " para a descrição se desejar manter o estilo anterior, 
# mas aqui segui rigorosamente o que você pediu: tudo separado por underline.

tags = [
    semana_formatada, copy, editor, conceito, 
    versao_formatada, tipo_midia, produto, 
    linguagem, formato, tipo_anuncio_sigla
]

# Filtra campos vazios para não gerar underlines duplos caso o usuário não tenha digitado algo ainda
nomenclatura_final = "_".join([str(t) for t in tags if t])

if descricao:
    nomenclatura_final += f" - {descricao}"

# --- EXIBIÇÃO DO RESULTADO ---
st.divider()
st.subheader("✅ Resultado Final:")

if not copy or not editor or not conceito:
    st.warning("⚠️ Preencha os campos obrigatórios (Copy, Editor e Conceito) para completar a nomenclatura.")

# Exibe o código em uma caixa que facilita a cópia
st.code(nomenclatura_final, language=None)

# Dica visual
st.info("Dica: Clique no ícone de prancheta no canto superior direito do código acima para copiar instantaneamente.")

# --- RODAPÉ ---
st.markdown(
    f"""
    <div style="background-color: #f1f1f1; padding: 10px; border-radius: 5px; border-left: 5px solid #2e6bef;">
        <strong>Resumo da estrutura:</strong><br>
        {semana_formatada} | {copy if copy else '??'} | {editor if editor else '??'} | {tipo_anuncio_sigla}
    </div>
    """, 
    unsafe_allow_html=True
)
