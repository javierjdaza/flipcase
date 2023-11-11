import streamlit as st 
from io import StringIO
from streamlit_option_menu import option_menu
import base64
from utils import iphone_models,hide_watermarks
from fit_images import resize_and_crop_image_from_image
from PIL import Image

# ------------------------
# PAGE CONFIGURATION
# ------------------------


_menu_items = {
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
st.set_page_config(page_title='Flip Case Customize!', page_icon = ':brain:', layout="centered", initial_sidebar_state="collapsed", menu_items=_menu_items)
hide_watermarks()

logo_1,logo_2,logo_3 = st.columns(3)

# ------
# LOGO
# ------
with logo_2:
    st.image('./img/svg_flipcase.png', use_column_width=True)


# ------------------------
# NAV BAR
# ------------------------
st.write('---')
menu_bar_selected = option_menu(None, ["Home", "Upload", 'About Us'], 
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
        product_selected = st.selectbox('**Please Select Your Product ⬇️**', options= ['Phone Cases 📱','Postcards 🌄']) #label_visibility='hidden',
        st.write(' ')
        if product_selected =='Phone Cases 📱':
            st.write('---')
            model_selected = st.selectbox('**Select the model:**', options = iphone_models.keys())
    st.write('---')
    tab1, tab2 = st.tabs(["Image 1", "Image 2"])

    with tab1:
        st.caption('Higher image quality yields superior final results 🚨')
        uploaded_file_handler_1 = st.file_uploader("**Choose file:**", accept_multiple_files = False, type = ['jpg', 'png', 'jpeg'], key = '_image_1')
        if uploaded_file_handler_1 is not None:
            # To read file as bytes:
            _image_1 = uploaded_file_handler_1.getvalue()
            _image_pillow = Image.open(uploaded_file_handler_1)
            st.write('---')
            
            im_1,im_2,im_3 = st.columns(3)
            offset_col1,offset_col2,offset_col3 = st.columns(3)
            
            with offset_col2: 
                _custom_offset = st.slider('X-axis slider', min_value = -50, max_value=50, value=0, step=1, label_visibility='hidden')
                st.caption('Move the slider (left or right) to fit the image. Take your time! ⌛')
                # st.markdown("<h6 style='text-align: center;'>Move the slider (left or right) to fit the image</h6>", unsafe_allow_html=True)
            with im_2:
                # st.image(_image_1, width=250)
                # st.toast('Image uploaded succesfully! ', icon='🎉')
                _custom_width = iphone_models[model_selected]['width']
                _custom_height = iphone_models[model_selected]['height']
                image_resize = resize_and_crop_image_from_image(_image_pillow, custom_width_mm=_custom_width, custom_height_mm=_custom_height, custom_offset_x=_custom_offset, target_dpi=600, output_path="output_image.jpg")
                st.image(image_resize, width=200)
                
                

        
    with tab2:
        st.caption('Higher image quality yields superior final results 🚨')
        uploaded_file_handler_2 = st.file_uploader("**Choose file:**", accept_multiple_files = False, type = ['jpg', 'png', 'jpeg'],  key = '_image_2')
        if uploaded_file_handler_2 is not None:
            # To read file as bytes:
            _image_2 = uploaded_file_handler_2.getvalue()
            im_1,im_2,im_3 = st.columns(3)
            with im_2:
                st.image(_image_2, width=250)
                st.toast('Image uploaded succesfully! ', icon='🎉')
                # st.caption('')
    

    