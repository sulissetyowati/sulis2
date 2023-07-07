import streamlit as st
import pandas as pd

st.title("Hello Welcome To My Bio")
st.image("sulis.png", use_column_width=True)
st.info("SULIS SETYOWATI")
st.write("Saya adalah lulusan dari universitas karangturi, saya juga pernah mengikuti magang dirumah sakit terkenal pada semester 4, saya juga aktif berorganisani selain itu saya juga berpengalaman dibidang rekam medis selama 4 tahun ")
st.info("NOMER INDUK MAHASISWA")
st.write(" B01.022.001")
st.info("PROGRAM STUDI")
st.write("Menejemen Informasi Kesehatan di Universitas Karangturi")

data_input = st.text_area("PENGALAMN", "2 tahun di RS sehat\n2 tahun di RS budi sehat\nProgram magang di Rs karangturi")
data_input = st.text_area("SKILLS", "kemampuan dibidang IT\nmampu mengolah data\nMampu mengkoding penyakit maupun komputer") 
st.info("KONTAK PERSON")
st.write("Click Link [WhatsApp](https://wa.me/6287814363312)")
st.write("Clink Link [Instagram](https://instagram.com/_bbyxyz)")
st.write("Email: sulissetyowati528@gmail.com")
