import streamlit as st
import requests
import time

def get_data():
    # make your 6 GET requests here and store the responses in a dictionary
    response1 = requests.get('https://rt.data.gov.hk/v2/transport/citybus/eta/CTB/003782/22x').text
    response2 = requests.get('https://rt.data.gov.hk/v2/transport/citybus/eta/CTB/003520/22m').text
    response3 = requests.get('https://rt.data.gov.hk/v2/transport/citybus/eta/CTB/003520/22').text
    response4 = requests.get('https://rt.data.gov.hk/v2/transport/citybus/eta/CTB/003520/5r').text
    response5 = requests.get('https://rt.data.gov.hk/v2/transport/citybus/eta/CTB/003520/22d').text
    response6 = requests.get('https://rt.data.gov.hk/v2/transport/citybus/eta/CTB/003587/22x').text

    data = {
        '22x_OV': response1,
        '22m_SFR': response2,
        '22_SFR': response3,
        '5R_SFR': response4,
        '22d_SFR': response5,
        '22x_KT': response6,
    }
    return data

def main():
    st.title('Auto-Refreshing Data')
    while True:
        data = get_data()
        st.write('22x_OV', data['22x_OV'])
        st.write('22m_SFR', data['22m_SFR'])
        st.write('22_SFR', data['22_SFR'])
        st.write('5R_SFR', data['5R_SFR'])
        st.write('22d_SFR', data['22d_SFR'])
        st.write('22x_KT:', data['22x_KT'])
        time.sleep(60) # wait for 60 seconds before refreshing
        st.experimental_refresh() # refresh the Streamlit app

if __name__ == '__main__':
    main()
