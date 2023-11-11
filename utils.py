import streamlit as st 

iphone_models = {
    'iPhone 11': 
        {
            'height' : 143.03,
            'width': 67.83
        },
    'iPhone 12': 
        {
            'height' : 142.69,
            'width': 67.51
        },
    'iPhone 13': 
        {
            'height' : 143.91,
            'width': 68.68
        },
    'iPhone 14': 
        {
            'height' : 143.31,
            'width': 68.12
        },
    'iPhone 15': 
        {
            'height' : 144.05,
            'width': 68.04
        },
    'iPhone 12 Pro': 
        {
            'height' : 143.91,
            'width': 68.68
        },
    'iPhone 13 Pro': 
        {
            'height' : 143.91,
            'width': 68.68
        },
    'iPhone 14 Pro': 
        {
            'height' : 143.86,
            'width': 67.85
        },
    'iPhone 15 Pro': 
        {
            'height' : 142.87,
            'width': 66.86
        },
    'iPhone 11 Pro Max': 
        {
            'height' : 150.21,
            'width': 70.08
        },
    'iPhone 12 Pro Max': 
        {
            'height' : 157.3,
            'width': 74.43
        },
    
    'iPhone 13 Pro Max': 
        {
            'height' : 158.29,
            'width': 75.62
        },
    'iPhone 14 Pro Max': 
        {
            'height' : 157.21,
            'width': 74.08
        },
    'iPhone 15 Pro Max' : 
        {
            'height' : 156.26,
            'width': 73.12
        }
        }


def hide_watermarks():
    hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """
    return st.markdown(hide_streamlit_style, unsafe_allow_html=True)