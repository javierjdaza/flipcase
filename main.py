import streamlit as st 
from io import StringIO
from streamlit_option_menu import option_menu
from utils import IPHONE_MODELS,POSTCARDS_SIZES,hide_watermarks,center_image_streamlit,center_button
from tab import Gen_Tab
# ------------------------
# PAGE CONFIGURATION
# ------------------------


_menu_items = {
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
st.set_page_config(page_title='Flip Case Customize!', page_icon = ':brain:', layout="wide", initial_sidebar_state="collapsed", menu_items=_menu_items)
hide_watermarks()
center_image_streamlit()
center_button()

# ------
# LOGO
# ------
st.image('./img/svg_flipcase.png',width=250 )


# ------------------------
# NAV BAR
# ------------------------



st.write('---')
menu_bar_selected = option_menu(None, ["Home", "Upload", 'Contact'], 
    icons=['house', 'cloud-upload', 'file-person-fill'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
st.write('---')


if menu_bar_selected == 'Home':
    st.markdown("<h1 style='text-align: center;'>Welcome to the FlipCase Customization Center!</h1>", unsafe_allow_html=True)
    st.write('---')
    
    # with open("./img/gif_flip.gif", "rb") as file_:
    #     contents = file_.read()
    #     data_url = base64.b64encode(contents).decode("utf-8")
    #     st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',unsafe_allow_html=True,)
    st.markdown("<h3 style='text-align: center;'>💥 Upload your pictures and start your own customization right now! 💥</h3>", unsafe_allow_html=True)


if menu_bar_selected == 'Upload':
    

    a1,a2,a3 = st.columns((1,2.5,1))
    with a2:
        # st.subheader('Please Select your product ⬇️')
        product_selected = st.selectbox('**Please Select Your Product ⬇️**', options= ['Phone Cases 📱','Postcards 🌄', 'Polaroid 📸']) #label_visibility='hidden',
        st.write(' ')
        
        # -----------------------
        # PHONE CASES SELECTED
        # -----------------------
        if product_selected =='Phone Cases 📱':
            st.write('---')
            model_selected = st.selectbox('**Select the model:**', options = IPHONE_MODELS.keys())
            st.write('---')
            st.markdown("<h3 style='text-align: center; color: #171717;'>Select The Pictures<br> Be Creative!🎆'</h3>", unsafe_allow_html=True)
            tab1, tab2 = st.tabs(["Image 1", "Image 2"])
            
            
            
            with tab1:
                tab_1 = Gen_Tab(model_selected=model_selected, key= 'tab_1')
                tab_1.get_phone_cases_tab()
            
            with tab2:
                tab_2 = Gen_Tab(model_selected=model_selected, key = 'tab2')
                tab_2.get_phone_cases_tab()
                
        # -----------------------
        # Postcards
        # -----------------------
        if product_selected =='Postcards 🌄':
            st.write('---')
            size_selected = st.selectbox('**Select the size:**', options = POSTCARDS_SIZES.keys())
            st.write('---')
            st.markdown("<h3 style='text-align: center; color: #171717;'>Select The Pictures<br> Be Creative!🎆'</h3>", unsafe_allow_html=True)
            tab1, tab2 = st.tabs(["Image 1", "Image 2"])
            with tab1:
                tab_1 = Gen_Tab(model_selected=size_selected, key= 'post_1')
                tab_1.get_postcard_tab()
                
            with tab2:
                tab_2 = Gen_Tab(model_selected=size_selected, key = 'post_2')
                tab_2.get_postcard_tab()
        

if menu_bar_selected == 'Contact':
    
    e1,e2 = st.columns(2)
    with e1:
        st.image('./img/efra.jpeg', use_column_width=True)
    with e2:
        st.image('./img/efra1.jpeg', use_column_width=True)