import streamlit as st

# Configuração da página
st.set_page_config(page_title="Gerador de Nomenclatura v10.4", layout="wide")

st.title("🏗️ Gerador de Nomenclatura v10.4")

# Inicialização de estados para o botão limpar funcionar corretamente
if 'semana' not in st.session_state: st.session_state.semana = 1
if 'versao' not in st.session_state: st.session_state.versao = 1

with st.container():
    # --- LINHA 1 (Campos 1, 2, 3) ---
    col1, col2, col3 = st.columns(3)
    with col1:
        num_semana = st.number_input("1. Número da Semana", min_value=1, max_value=53, step=1, key="semana")
        semana_formatada = f"W{int(num_semana):02d}Y26"
    with col2:
        copy = st.text_input("2. Sigla Copy (Até 3 letras)", max_chars=3, key="copy_input").upper()
    with col3:
        editor = st.text_input("3. Sigla Editor (Até 3 letras)", max_chars=3, key="editor_input").upper()

    # --- LINHA 2 (Campos 4, 5, 6) ---
    col4, col5, col6 = st.columns(3)
    with col4:
        conceito = st.text_input("4. Conceito (Ex: OFFER)", key="conceito_input").upper()
    with col5:
        versao_num = st.number_input("5. Número da Versão", min_value=1, step=1, key="versao")
        versao_formatada = f"V{int(versao_num)}"
    with col6:
        tipo_midia = st.selectbox("6. Tipo de Mídia", ["VID", "IMG", "CAR"], key="midia_input")

    # --- LINHA 3 (Campos 7, 8, 9) ---
    col7, col8, col9 = st.columns(3)
    with col7:
        produto = "POLI"
        st.text_input("7. Produto", value=produto, disabled=True)
    with col8:
        linguagem = st.selectbox("8. Linguagem", ["BR", "ES"], key="lang_input")
    with col9:
        formato = st.selectbox("9. Formato", ["V", "H"], key="formato_input")

    # --- LINHA 4 (Campo 10) ---
    mapa_anuncio = {
        "MODELAGEM DE CONCORRENTE EXPANDIDO": "MCE",
        "ESTRUTURA INVISÍVEL": "EIN",
        "CONCEITO ZERO": "CZO",
        "EXPANSÃO DE ÂNGULO VALIDADO": "EAV",
        "ITERAÇÕES": "ITE"
    }
    tipo_anuncio_nome = st.selectbox("10. Tipo de Anúncio", list(mapa_anuncio.keys()), key="tipo_anuncio")
    tipo_anuncio_sigla = mapa_anuncio[tipo_anuncio_nome]

    # --- LINHA 5 (Campo 11) ---
    descricao = st.text_input("11. Descrição (Texto Livre)", placeholder="Digite a descrição aqui...", key="desc_input")

# --- BOTÕES DE AÇÃO ---
st.markdown("---")
c_btn1, c_btn2, _ = st.columns([1, 1, 4])

with c_btn1:
    gerar = st.button("Gerar Nome ✅", type="primary")
with c_btn2:
    if st.button("Limpar Tudo 🗑️"):
        st.rerun() 

# --- RESULTADO FINAL ---
if gerar:
    if not copy or not editor or not conceito:
        st.error("⚠️ Por favor, preencha os campos de Copy, Editor e Conceito.")
    else:
        # Ordem: SEMANA_COPY_EDITOR_CONCEITO_VERSAO_MIDIA_POLI_LINGUAGEM_TIPO_FORMATO
        tags = [
            semana_formatada, 
            copy, 
            editor, 
            conceito, 
            versao_formatada, 
            tipo_midia, 
            produto, 
            linguagem, 
            tipo_anuncio_sigla, 
            formato
        ]
        
        resultado_base = "_".join(tags)
        resultado_final = f"{resultado_base} - {descricao}" if descricao else resultado_base

        st.success("Nomenclatura criada com sucesso!")
        st.code(resultado_final, language=None)
        
        if len(resultado_final) > 100:
            st.warning("Nota: O nome está bem longo. Verifique se o destino aceita esse comprimento.")

st.caption("v10.4 | Ordem: Midia > Poli > Lang > Tipo > Formato")
