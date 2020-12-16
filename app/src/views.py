import streamlit as st

from app.helper.calc_risk import calc_additional_risks

def main ():
    st.title('Covid-19 Tarama')

    cough = st.slider('Oksurme araligi:', 0.0, 10.0, 0.0)

    fever = st.slider('Atesiniz:', 30.0, 42.0, 32.0)

    breath_diff = st.slider('Nefes alma zorlugu:', 0.0, 10.0, 0.0)

    age = st.slider('Yasiniz:', 1, 100, 25)

    polluted = st.checkbox('Hava kirliligi olan bir yerde mi yasiyorsun?')

    hypertension = st.checkbox('Hiper Tansiyonun var mi?')

    diabetes = st.checkbox('Diyabet hastasi misin?')

    cardiovascular = st.checkbox('Kardiovaskuler bir sorun yasiyor musun?')

    respiratory = st.checkbox('Solunum ile ilgili bir hastaligin var mi?')

    immune = st.checkbox('Bagisiklik sistemin zayif mi?')

    calculate = st.button('Hesapla')


    if(calculate is True):
        result = calc_additional_risks(age,polluted,hypertension,diabetes,cardiovascular,respiratory,immune)
        st.subheader(f"Risk Score: {result}")
    else:
        pass


