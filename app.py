import streamlit as st

# Configuração da página
st.set_page_config(page_title="Gerador de Nomenclatura v10.2", layout="wide")

st.title("🏗️ Gerador de Nomenclatura v10.2")
st.markdown("Preencha os campos abaixo. A descrição agora tem espaço ampliado!")

# Função para resetar o estado (Limpar Campos)
def limpar_campos():
    for key in st.session_state.keys():
        del st.session_state[key]

# Uso de formulário para organizar os inputs e o botão de reset
with st.form("gerador_form", clear_on_submit=False):
    
    # --- LINHA 1: CAMPOS TÉCNICOS ---
    col1, col2, col3 = st.columns(3)

    with col1:
        num_semana = st.number_input("1. Número da Semana", min_value=1, max_value=53, step=1, value=1, key="semana")
        semana_formatada = f"W{int(num_semana):02d}Y26"

        copy = st.text_input("2. Sigla Copy (Ex: PFR)", max_chars=3, key="copy").upper()
        editor = st.text_input("3. Sigla Editor (Ex: ALX)", max_chars=3, key="editor").upper()

    with col2:
        conceito = st.text_input("4. Conceito (Ex: OFFER)", key="conceito").upper()
        
        versao_num = st.number_input("5. Número da Versão", min_value=1, step=1, value=1, key="versao")
        versao_formatada = f"V{int(versao_num)}"

        tipo_midia = st.selectbox("6. Tipo de Mídia", ["VID", "IMG", "CAR"], key="midia")

    with col3:
        # Produto Fixo
        st.text_input("7. Produto", value="POLI", disabled=True)
        
        linguagem = st.selectbox("8. Linguagem", ["BR", "ES"], key="lang")
        formato = st.selectbox("9. Formato", ["V", "H"], key="formato")

    # --- LINHA 2: TIPO DE ANÚNCIO (Largura total ou parcial) ---
    mapa_anuncio = {
        "MODELAGEM DE CONCORRENTE EXPANDIDO": "MCE",
        "ESTRUTURA INVISÍVEL": "EIN",
        "CONCEITO ZERO": "CZO",
        "EXPANSÃO DE ÂNGULO VALIDADO": "EAV",
        "ITERAÇÕES": "ITE"
    }
    tipo_anuncio_nome = st.selectbox("10. Tipo de Anúncio", list(mapa_anuncio.keys()), key="tipo_anuncio")
    tipo_anuncio_sigla = mapa_anuncio[tipo_anuncio_nome]

    # --- LINHA 3: DESCRIÇÃO AMPLIADA ---
    # Usando text_area para permitir mais texto se necessário, ou text_input para linha única longa
    descricao = st.text_input("11. Descrição do Vídeo (Mantém maiúsculas/minúsculas)", placeholder="Digite aqui o nome amigável do vídeo...", key="desc")

    # --- BOTÕES ---
    c1, c2 = st.columns([1, 10])
    with c1:
        btn_gerar = st.form_submit_button("Gerar ✅")
    with c2:
        btn_limpar = st.form_submit_button("Limpar Campos 🗑️", on_click=limpar_campos)

# --- LÓGICA DE MONTAGEM ---
if btn_gerar:
    tags = [
        semana_formatada, copy, editor, conceito, 
        versao_formatada, tipo_midia, "POLI", 
        linguagem, formato, tipo_anuncio_sigla
    ]

    # Validação simples
    if not copy or not editor or not conceito:
        st.error("❌ Erro: Os campos Copy, Editor e Conceito são obrigatórios!")
    else:
        # Montagem final
        nome_base = "_".join([str(t) for t in tags if t])
        nomenclatura_final = f"{nome_base} - {descricao}" if descricao else nome_base

        st.divider()
        st.subheader("📋 Nome Gerado:")
        st.code(nomenclatura_final, language=None)
        st.balloons()

st.info("💡 Basta clicar no ícone de cópia no canto direito da caixa cinza acima.")

# Rodapé
st.caption("v10.2 | Layout Otimizado | Descrição preservada")
