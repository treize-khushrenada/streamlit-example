import streamlit as st
import requests
import time

def get_data():
    # make your 6 GET requests here and store the responses in a dictionary
    response1 = requests.get('https://rt.data.gov.hk/v2/transport/citybus/eta/CTB/003782/22x').json()            
    response2 = requests.get('https://rt.data.gov.hk/v2/transport/citybus/eta/CTB/003520/22m').json()
    response3 = requests.get('https://rt.data.gov.hk/v2/transport/citybus/eta/CTB/003520/22').json()
    response4 = requests.get('https://rt.data.gov.hk/v2/transport/citybus/eta/CTB/003520/5r').json()
    response5 = requests.get('https://rt.data.gov.hk/v2/transport/citybus/eta/CTB/003520/22d').json()
    response6 = requests.get('https://rt.data.gov.hk/v2/transport/citybus/eta/CTB/003587/22x').json()

    try:
        response1 = response1['data'][0]['eta']
    except:
        response1 = 'N/A'

    try:
        response2 = response2['data'][0]['eta']
    except:
        response2 = 'N/A'

    try:
        response3 = response3['data'][0]['eta']
    except:
        response3 = 'N/A'

    try:
        response4 = response4['data'][0]['eta']
    except:
        response4 = 'N/A'

    try:
        response5 = response5['data'][0]['eta']
    except:
        response5 = 'N/A'

    try:
        response6 = response6['data'][0]['eta']
    except:
        response6 = 'N/A'
    

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
    data = get_data()    
    st.markdown('#22X走', data['22x_OV'])
    st.markdown('#22M走', data['22m_SFR'])
    st.markdown('#22走', data['22_SFR'])
    st.markdown('#5R走', data['5R_SFR'])
    st.markdown('#22D走', data['22d_SFR'])
    st.markdown('#22x返', data['22x_KT'])

while __name__ == '__main__':
    main()
    time.sleep(60)
