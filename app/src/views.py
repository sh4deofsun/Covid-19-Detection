import streamlit as st

from app.helper.mf import MF
from app.src.graph import get_graphics

def main ():
    st.title('Covid-19 Tarama')

    cough = st.slider('Oksurme yoğunluğu:', 0.0, 9.9, 0.0)

    fever = st.slider('Ateş yoğunluğu:', 0.0, 9.9, 0.0)

    breath_diff = st.slider('Nefes alma zorlugu:', 0.0, 9.9, 0.0)

    pain = st.slider('Ağrı Yoğunluğu', 0.0, 9.9, 0.0)

    age = st.slider('Yasiniz:', 1, 100, 25)

    polluted = st.checkbox('Hava kirliligi olan bir yerde mi yasiyorsun?')

    hypertension = st.checkbox('Hiper Tansiyonun var mi?')

    diabetes = st.checkbox('Diyabet hastasi misin?')

    cardiovascular = st.checkbox('Kardiovaskuler bir sorun yasiyor musun?')

    respiratory = st.checkbox('Solunum ile ilgili bir hastaligin var mi?')

    immune = st.checkbox('Bagisiklik sistemin zayif mi?')

    calculate_risk = st.button('Hesapla ')

    if(calculate_risk is True):
        """
            additional_risks = (age,polluted,hypertension,diabetes,cardiovascular,respiratory,immune)
            add_result = Risk.calc_additional_risks_score(*additional_risks)
        """
        risk = MF.simulation(cough,fever,breath_diff,pain)
        st.subheader(f"Covid-19 olama ihtimalin %{risk * 10}")
        get_graphics()

