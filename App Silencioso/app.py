
import streamlit as st
import tempfile
import os
from processador_faturas import processar_pdfs_com_visao_geral

st.set_page_config(page_title="Processador de Faturas", layout="centered")

st.title("📄 Processador de Faturas em PDF")
st.markdown("Faça o upload de múltiplas faturas de cartão de crédito em PDF e baixe um Excel com todas as informações formatadas.")

# ✅ Ignora validação interna de tipo
uploaded_files_raw = st.file_uploader("📤 Envie os arquivos PDF aqui", type=None, accept_multiple_files=True)

# ✅ Aplica validação manual da extensão
uploaded_files = []
if uploaded_files_raw:
    for f in uploaded_files_raw:
        if f.name.lower().strip().endswith(".pdf"):
            uploaded_files.append(f)
        else:
            st.warning(f"⚠️ Arquivo ignorado (extensão inválida): {f.name}")

if uploaded_files:
    with tempfile.TemporaryDirectory() as tmpdir:
        for f in uploaded_files:
            with open(os.path.join(tmpdir, f.name), "wb") as temp_file:
                temp_file.write(f.read())

        output_path = os.path.join(tmpdir, "faturas_processadas.xlsx")

        with st.spinner("⏳ Processando faturas..."):
            processar_pdfs_com_visao_geral(tmpdir, output_path)

        with open(output_path, "rb") as f:
            st.success("✅ Arquivo gerado com sucesso!")
            st.download_button("⬇️ Baixar Excel Processado", f, file_name="faturas_processadas.xlsx")
