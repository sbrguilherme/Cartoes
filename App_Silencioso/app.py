
import streamlit as st
import tempfile
import os
from processador_faturas import processar_pdfs_com_visao_geral

st.set_page_config(page_title="📄 Processador de Faturas", layout="centered")

st.title("📄 Processador de Faturas em PDF")
st.markdown("Envie faturas em PDF e receba uma planilha Excel com abas e visão geral.")

if "arquivos" not in st.session_state:
    st.session_state.arquivos = []

with st.form("upload_form"):
    uploaded_files = st.file_uploader("📤 Envie os PDFs", type=["pdf"], accept_multiple_files=True)
    submitted = st.form_submit_button("Processar Faturas")

    if submitted and uploaded_files:
        st.session_state.arquivos = uploaded_files

if st.session_state.arquivos:
    with st.spinner("⏳ Processando faturas..."):
        with tempfile.TemporaryDirectory() as tmpdir:
            for f in st.session_state.arquivos:
                with open(os.path.join(tmpdir, f.name), "wb") as temp_file:
                    temp_file.write(f.read())

            output_path = os.path.join(tmpdir, "faturas_processadas.xlsx")
            processar_pdfs_com_visao_geral(tmpdir, output_path)

            with open(output_path, "rb") as f:
                st.success("✅ Arquivo gerado com sucesso!")
                st.download_button("⬇️ Baixar Excel", f, file_name="faturas_processadas.xlsx")
