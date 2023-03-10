# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 17:33:43 2023

Author: Giddy Physicist

Rebel_App.py

######## Color Schemes and Fonts ########
from website: 
Font: Roboto
Colors: #ff6600
        #ffffff
        #000000


Chassis (2 choices)



     Ram 5500 (standard)

74,985.25 

     Ford 550

77,262.15 

Body

16,668.41 

Pump (2 choices)



     Hale Pump (standard)

13,526.13 

     Wateraxe Pump

126,434.18 

Tank

4,225.00 

Hose Reels (2 choices)

1,141.56 

     1 Reel (left or right) (Standard is left)

11,000.00 

     2 Reels

22,000.00 

Rims & Tires  (2 choices)



     Factory wheels (standard)

0.00 

     Lifted super singles

10,000.00 

Paint (2 choices)

0.00 

     None (standard)

0.00 

     Non-OEM Red

6,000.00 


"""
import streamlit as st

#### UTILITIES ####
def round5(x):
    return x + (5-x)%5
####

# define session state variables.

if 'chassis' not in st.session_state:
    st.session_state['chassis'] = 'Ram 5500 (standard)'


if 'body' not in st.session_state:
    st.session_state['body'] = '(standard)'


if 'pump' not in st.session_state:
    st.session_state['pump'] = 'Hale Pump (standard)'


if 'tank' not in st.session_state:
    st.session_state['tank'] = '(standard)'


if 'hose_reels' not in st.session_state:
    st.session_state['hose_reels'] = '1 Reel, Left (standard)'



if 'rims_tires' not in st.session_state:
    st.session_state['rims_tires'] = 'Factory wheels (standard)'


if 'paint' not in st.session_state:
    st.session_state['paint'] = 'None (standard)'

if 'price_db' not in st.session_state:
    st.session_state['price_db'] = {'chassis':{'Ram 5500 (standard)': round5(74_985.25),
                                               'Ford 550': round5(77_262.15)},
                                    'body':{'(standard)': round5(16_668.41)},
                                    'pump':{'Hale Pump (standard)': round5(13_526.13),
                                            'Wateraxe Pump': round5(126_434.18)},
                                    'tank':{'(standard)': round5(4_225.00)},
                                    'hose_reels':{'1 Reel, Left (standard)': round5(11_000.00),
                                                  '1 Reel, Right': round5(11_000.00), 
                                                  '2 Reels': round5(22_000.00)},
                                    'rims_tires':{'Factory wheels (standard)': round5(0.00),
                                                  'Lifted super singles': round5(10_000.00)},
                                    'paint':{'None (standard)': round5(0.00),
                                             ' Non-OEM Red': round5(6_000.00)}}
if 'element_to_name' not in st.session_state:
    st.session_state['element_to_name'] = {'chassis':'Chassis',
                                           'body':'Body',
                                           'pump':'Pump',
                                           'tank':'Tank',
                                           'hose_reels':'Hose Reels',
                                           'rims_tires':'Rims & Tires',
                                           'paint':'Paint'}

if 'diffs' not in st.session_state:
    st.session_state['diffs'] = []
    
if 'costs' not in st.session_state:
    st.session_state['costs'] = []
    

st.set_page_config(page_title='Rebel Price Estimator',
                          # page_icon="",
                           layout='wide',
                          initial_sidebar_state='auto')

hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""

# hide_menu_style = """
#     <style>
#     footer {visibility: hidden;}
#     </style>
# """


st.markdown(hide_menu_style, unsafe_allow_html=True)





def Header():
    pass
    _,c,_ = st.columns(3)
    with c:
        st.image('./Rebel Logo.png',use_column_width='auto')
    st.markdown('# Rebel Strike Cost Estimator')
    # here, want title of page and logo

    
def PriceTally_element(element):
    name = st.session_state['element_to_name'][element]
    choice = st.session_state[element]
    price = st.session_state['price_db'][element][choice]
    s = f'{name}: {choice} ({price})'
    return s

def PriceStats():
    prices = []
    for element in st.session_state['element_to_name'].keys():
        choice = st.session_state[element]
        price = st.session_state['price_db'][element][choice]
        prices.append(price)
    # _,c,_ = st.columns(3)
    # with c:
    st.metric('Total Cost',f'${sum(prices):,.2f}*')
    st.caption('*Pricing is final at contract signing, as supply chain and availability/delivery is unknown')

def PriceTally():
    
    for element in st.session_state['element_to_name'].keys():
        
        name = st.session_state['element_to_name'][element]
        
        st.header(name)
        c1,c2,c3= st.columns(3)    
        with c1:
            value = st.selectbox(name, 
                                 options=list(st.session_state['price_db'][element].keys()),
                                 help=f'Choose {name}',
                                 label_visibility="collapsed")
            st.session_state[element] = value
            choice = st.session_state[element]
            price = st.session_state['price_db'][element][choice]
        with c2:
            st.info(f'{choice}')
        with c3:
            s = f'${price:,.2f}'
            st.info(s)
        # st.info(PriceTally_element(element))
        
        
    # st.markdown('\n\n'.join([PriceTally_element(element) for element in st.session_state['element_to_name'].keys()]))
                # Price
                
                # Body: {st.session_state["body"]}
                
                # Pump: {st.session_state["pump"]}
                
                # Tank: {st.session_state["tank"]}
                
                # Hose Reels: {st.session_state["hose_reels"]}
                
                # Rims & Tires : {st.session_state["rims_tires"]}
                
                # Paint: {st.session_state["paint"]}
                
                # ''')

# def Sidebar():
#     # here, can add options to choose for configuring truck
        
#     with st.sidebar:
#         st.header('Customize Parts')
#         # chassis = st.selectbox('Chassis', options=['Ram 5500 (standard)','Ford 550'],help='Choose Chassis')
#         # st.session_state['chassis'] = chassis
        
#         body = st.selectbox('Body', options=['(standard)'],help='Choose Body')
#         st.session_state['body'] = body
        
#         pump = st.selectbox('Pump',options=['Hale Pump (standard)','Wateraxe Pump'],help='Choose Pump')
#         st.session_state['pump'] = pump
        
#         tank = st.selectbox('Tank',options=['(standard)'],help='Choose Tank')
#         st.session_state['tank'] = tank
        
#         hose_reels = st.selectbox('Hose Reels',options=['1 Reel, Left (standard)','1 Reel, Right', '2 Reels'],help='Choose Hose Reels')
#         st.session_state['hose_reels'] = hose_reels
        
#         rims_tires = st.selectbox('Rims & Tires',options=['Factory wheels (standard)','Lifted super singles'],help='Choose Rims & Tires')
#         st.session_state['rims_tires'] = rims_tires
        
#         paint = st.selectbox('Paint',options=['None (standard)',' Non-OEM Red'],help='Choose Paint')
#         st.session_state['paint'] = paint
    
#     PriceStats()
#     PriceTally()
#     DiffFromStandard()

def DiffFromStandard():
    diffs = []
    for element in st.session_state['element_to_name']:
        choice = st.session_state[element]
        name = st.session_state['element_to_name'][element]
        if '(standard)' not in choice:
            diffs.append(f'{name}: {choice}')
    st.session_state['diffs'] = diffs
    st.markdown('-----')
    if diffs:
        st.header('Standard Design with Changes:')
        for choice in diffs:
            st.success(choice)
    else:
        st.header('Standard Design')

def Footer():
    pass

def applyCss():
    css = '''
    <style>
    img, div > div > .stButton, h2 > div > span, h1 > div > span, .stRadio, h3 > div > span, div[data-testid="stMetricValue"] > div {
        display: flex;
        align-items: center;
        justify-content: center;
        }

    .stRadio > label {
        display: none;
        }
    </style>'''
    st.markdown(css,unsafe_allow_html=True)

def App():
    Header()
    # PriceTally()
    # Sidebar()
    # PriceStats()
    PriceTally()
    PriceStats()
    DiffFromStandard()
    applyCss()
    Footer()
    


if __name__=='__main__':
    App()
