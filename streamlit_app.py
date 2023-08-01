import streamlit as st
import requests
import time
from datetime import datetime
from pytz import timezone    

def get_data():

    data = {
        '22x_OV': [None, None],
        '22m_SFR': [None, None],
        '22_SFR': [None, None],
        '5R_SFR': [None, None],
        '22d_SFR': [None, None],
        '22x_KT': [None, None],
    }
    
    hkt = timezone('Asia/Hong_Kong')
    hkt_now = datetime.now(hkt)
    # make your 6 GET requests here and store the responses in a dictionary
    response1 = requests.get('https://rt.data.gov.hk/v2/transport/citybus/eta/CTB/003782/22x').json()            
    response2 = requests.get('https://rt.data.gov.hk/v2/transport/citybus/eta/CTB/003520/22m').json()
    response3 = requests.get('https://rt.data.gov.hk/v2/transport/citybus/eta/CTB/003520/22').json()
    response4 = requests.get('https://rt.data.gov.hk/v2/transport/citybus/eta/CTB/003520/5r').json()
    response5 = requests.get('https://rt.data.gov.hk/v2/transport/citybus/eta/CTB/003520/22d').json()
    response6 = requests.get('https://rt.data.gov.hk/v2/transport/citybus/eta/CTB/003587/22x').json()

    try:
        response1 = response1['data'][0]['eta']
        eta = datetime.fromisoformat(response1)
        response1 = (eta - hkt_now).total_seconds() / 60
        eta = eta.strftime("%H:%M")
    except:
        eta = 'N/A'
        response1 = 0
    
    data['22x_OV'][0] = eta
    data['22x_OV'][1] = response1

    try:
        response2 = response2['data'][0]['eta']
        eta = datetime.fromisoformat(response2)
        response2 = (eta - hkt_now).total_seconds() / 60
        eta = eta.strftime("%H:%M")
    except:
        eta = 'N/A'
        response2 = 0

    data['22m_SFR'][0] = eta
    data['22m_SFR'][1] = response2

    try:
        response3 = response3['data'][0]['eta']
        eta = datetime.fromisoformat(response3)
        response3 = (eta - hkt_now).total_seconds() / 60
        eta = eta.strftime("%H:%M")
    except:
        eta = 'N/A'
        response3 = 0

    data['22_SFR'][0] = eta
    data['22_SFR'][1] = response3

    try:
        response4 = response4['data'][0]['eta']
        eta = datetime.fromisoformat(response4)
        response4 = (eta - hkt_now).total_seconds() / 60
        eta = eta.strftime("%H:%M")
    except:
        eta = 'N/A'
        response4 = 0

    data['5R_SFR'][0] = eta
    data['5R_SFR'][1] = response4

    try:
        response5 = response5['data'][0]['eta']
        eta = datetime.fromisoformat(response5)
        response5 = (eta - hkt_now).total_seconds() / 60
        eta = eta.strftime("%H:%M")
    except:
        eta = 'N/A'
        response5 = 0

    data['22d_SFR'][0] = eta
    data['22d_SFR'][1] = response5

    try:
        response6 = response6['data'][0]['eta']
        eta = datetime.fromisoformat(response6)
        response6 = (eta - hkt_now).total_seconds() / 60
        eta = eta.strftime("%H:%M")
    except:
        eta = 'N/A'
        response6 = 0

    data['22x_KT'][0] = eta
    data['22x_KT'][1] = response6
    
    return data
    

def main():
    st.title('維一Come & Go💨')
    data = get_data()
    col1, col2 = st.columns(2)
    with col1:
        st.header("Come")
        st.markdown('# 22x')
        st.markdown('# 22x ETA: '+str(data['22x_KT'][0]))
        st.markdown('# '+str(int(data['22x_KT'][1]))+"mins left")
    with col2:
        st.header("Go")
        st.markdown('# 22X')
        st.markdown('# ETA: '+str(data['22x_OV'][0]))
        st.markdown('# '+str(int(data['22x_OV'][1]))+"mins left")
        st.markdown('# 22M')
        st.markdown('# ETA: '+str(data['22m_SFR'][0]))
        st.markdown('# '+str(int(data['22m_SFR'][1]))+"mins left")
        st.markdown('# 22')
        st.markdown('# ETA: '+str(data['22_SFR'][0]))
        st.markdown('# '+str(int(data['22_SFR'][1]))+"mins left")
        st.markdown('# 5R')
        st.markdown('# ETA: '+str(data['22_SFR'][0]))
        st.markdown('# '+str(int(data['22_SFR'][1]))+"mins left")
        st.markdown('# 22D')
        st.markdown('# ETA: '+str(data['22d_SFR'][0]))
        st.markdown('# '+str(int(data['22d_SFR'][1]))+"mins left")
    

if __name__ == '__main__':
    main()
