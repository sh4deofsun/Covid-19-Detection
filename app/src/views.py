from datetime import time
import streamlit as st

from app.helper.calc_risk import calc_additional_risks_score, calc_risk_percentage

def main ():
    st.title('Covid-19 Tarama')

    cough = st.slider('Oksurme araligi:', 0.0, 10.0, 0.0)

    fever = st.slider('Atesiniz:', 30.0, 42.0, 32.0)

    breath_diff = st.slider('Nefes alma zorlugu:', 0.0, 10.0, 0.0)

    calculate_covid = st.button('Hesapla')

    st.title('Risk Kontrolü')

    st.info("Bu kontrol sırasında herhangi bir veri kullanılmadı kontrol test amaçlı yapıldı.")

    age = st.slider('Yasiniz:', 1, 100, 25)

    density = st.slider('Bölgedeki covid-19 durumu :', 0.0, 10.0, 5.0)

    polluted = st.checkbox('Hava kirliligi olan bir yerde mi yasiyorsun?')

    hypertension = st.checkbox('Hiper Tansiyonun var mi?')

    diabetes = st.checkbox('Diyabet hastasi misin?')

    cardiovascular = st.checkbox('Kardiovaskuler bir sorun yasiyor musun?')

    respiratory = st.checkbox('Solunum ile ilgili bir hastaligin var mi?')

    immune = st.checkbox('Bagisiklik sistemin zayif mi?')

    calculate_risk = st.button('Hesapla ')

    if(calculate_risk is True):
        additional_risks = (age,polluted,hypertension,diabetes,cardiovascular,respiratory,immune)
        result = calc_additional_risks_score(*additional_risks)
        result = calc_risk_percentage(result,density)
        st.subheader(f"Covid-19'a yakalanma ihtimaliniz %{result}")


