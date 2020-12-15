import streamlit as st

st.title('Covid-19 Tarama')

oksuruk = st.slider('Oksurme araligi', 0.0, 10.0, 0.0)
st.subheader(oksuruk)

ates = st.slider('Atesiniz', 30.0, 42.0, 32.0)
st.subheader(ates)

nefes = st.slider('Nefes alma zorlugu', 0.0, 10.0, 0.0)
st.subheader(nefes)

yas = st.slider('Yasiniz', 1, 100, 25)
st.subheader(yas)

kirlilik = st.checkbox('Hava kirliligi olan bir yerde mi yasiyorsun?')
st.subheader(kirlilik)

hipertansiyon = st.checkbox('Hiper Tansiyonun var mi?')
st.subheader(hipertansiyon)

diyabet = st.checkbox('Diyabet hastasi misin?')
st.subheader(diyabet)

kardio = st.checkbox('Kardiovaskuler bir sorun yasiyor musun?')
st.subheader(kardio)

solunum = st.checkbox('Solunum ile ilgili bir hastaligin var mi?')
st.subheader(solunum)

bagisiklik = st.checkbox('Bagisiklik sistemin zayif mi?')
st.subheader(bagisiklik)

hesapla = st.button('Hesapla')
st.subheader(hesapla)

if(hesapla is True):
    st.subheader("Don't worry, you will die someday.")
else:
    pass


