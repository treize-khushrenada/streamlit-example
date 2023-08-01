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
        response1 = eta - hkt_now
        response1 = response1.minutes
    except:
        eta = 'N/A'
        response1 = 'N/A'
    
    data['22x_OV'][0] = eta.strftime("%H:%M:%S")
    data['22x_OV'][1] = response1

    try:
        response2 = response2['data'][0]['eta']
        eta = datetime.fromisoformat(response2)
        response2 = (eta - hkt_now)
    except:
        eta = 'N/A'
        response2 = 'N/A'

    data['22m_SFR'][0] = eta.strftime("%H:%M:%S")
    data['22m_SFR'][1] = response2

    try:
        response3 = response3['data'][0]['eta']
        eta = datetime.fromisoformat(response3)
        response3 = (eta - hkt_now)
    except:
        eta = 'N/A'
        response3 = 'N/A'

    data['22_SFR'][0] = eta.strftime("%H:%M:%S")
    data['22_SFR'][1] = response3

    try:
        response4 = response4['data'][0]['eta']
        eta = datetime.fromisoformat(response4)
        response4 = (eta - hkt_now)
    except:
        eta = 'N/A'
        response4 = 'N/A'

    data['5R_SFR'][0] = eta.strftime("%H:%M:%S")
    data['5R_SFR'][1] = response4

    try:
        response5 = response5['data'][0]['eta']
        eta = datetime.fromisoformat(response5)
        response5 = (eta - hkt_now)
    except:
        eta = 'N/A'
        response5 = 'N/A'

    data['22d_SFR'][0] = eta.strftime("%H:%M:%S")
    data['22d_SFR'][1] = response5

    try:
        response6 = response6['data'][0]['eta']
        eta = datetime.fromisoformat(response6)
        response6 = (eta - hkt_now)
    except:
        eta = 'N/A'
        response6 = 'N/A'

    data['22x_KT'][0] = eta.strftime("%H:%M:%S")
    data['22x_KT'][1] = response6
    
    return data
    

def main():
    st.title('Come & Go💨')
    data = get_data()    
    st.markdown('# 22X走')
    st.markdown('# ETA: '+str(data['22x_OV'][0]))
    st.markdown('# '+str(data['22x_OV'][1])+" left")
    st.markdown('# 22M走')
    st.markdown('# ETA: '+str(data['22m_SFR'][0]))
    st.markdown('# '+str(data['22m_SFR'][1])+" left")
    st.markdown('# 22走')
    st.markdown('# ETA: '+str(data['22_SFR'][0]))
    st.markdown('# '+str(data['22_SFR'][1])+" left")
    st.markdown('# 5R走')
    st.markdown('# ETA: '+str(data['22_SFR'][0]))
    st.markdown('# '+str(data['22_SFR'][1])+" left")
    st.markdown('# 22D走')
    st.markdown('# ETA: '+str(data['22d_SFR'][0]))
    st.markdown('# '+str(data['22d_SFR'][1])+" left")
    st.markdown('# 22x返')
    st.markdown('# ETA: '+str(data['22x_KT'][0]))
    st.markdown('# '+str(data['22x_KT'][1])+" left")

if __name__ == '__main__':
    main()
