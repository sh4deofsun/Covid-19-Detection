import streamlit as st

from app.helper.symptoms import get_symptoms_data

def main ():
    st.title('Covid-19 Tarama')

    oksuruk = st.slider('Oksurme araligi:', 0.0, 10.0, 0.0)

    ates = st.slider('Atesiniz:', 30.0, 42.0, 32.0)

    nefes = st.slider('Nefes alma zorlugu:', 0.0, 10.0, 0.0)

    yas = st.slider('Yasiniz:', 1, 100, 25)

    kirlilik = st.checkbox('Hava kirliligi olan bir yerde mi yasiyorsun?')

    hipertansiyon = st.checkbox('Hiper Tansiyonun var mi?')

    diyabet = st.checkbox('Diyabet hastasi misin?')

    kardio = st.checkbox('Kardiovaskuler bir sorun yasiyor musun?')

    solunum = st.checkbox('Solunum ile ilgili bir hastaligin var mi?')

    bagisiklik = st.checkbox('Bagisiklik sistemin zayif mi?')

    hesapla = st.button('Hesapla')

    if(hesapla is True):
        st.subheader("Don't worry, you will die someday.")
    else:
        pass


