import streamlit as st 
from fit_images import fill_custom_size,fill_custom_size_height
from utils import IPHONE_MODELS,POSTCARDS_SIZES
from PIL import Image




class Gen_Tab():
    
    def __init__(self, model_selected, key) -> None:
        # self._custom_offset_x = custom_offset
        self._model_selected = model_selected
        self._key = key
        
        
    def get_phone_cases_tab(self):
        st.caption('Higher image quality yields superior final results 🚨')
        uploaded_file_handler = st.file_uploader("**Choose file:**", accept_multiple_files = False, type = ['jpg', 'png', 'jpeg'], key = self._key)
        if uploaded_file_handler is not None:
            # To read file as bytes:
            _image = uploaded_file_handler.getvalue()
            _image_pillow = Image.open(uploaded_file_handler)
            st.write('---')
            
            im_1,im_2,im_3 = st.columns((1,3,1))
            of1,of2,of3 = st.columns((1,3,1))
            with of2:
                _custom_offset_x = st.slider(f'{self._key}', min_value = -50, max_value=50, value=0, step=1, label_visibility='hidden')
                st.markdown("<h6 style='text-align: center; color: #7F8487;'>X-axis align</h6>", unsafe_allow_html=True)
                st.write('---')
                st.markdown("<h6 style='text-align: center; color: #171717;'>Move the slider (left or right) to fit the image.<br> Take your time! ⌛</h6>", unsafe_allow_html=True)
                create_button = st.button('C R E A T E', type='primary', key= f'{self._key}_button')
                if create_button:
                    st.toast('EFRAIN APONTE', icon='🧟')
            with im_2:
                _custom_width = IPHONE_MODELS[self._model_selected]['width']
                _custom_height = IPHONE_MODELS[self._model_selected]['height']
                image_resize,aspect_ratio_input = fill_custom_size(_image_pillow, custom_width_mm=_custom_width, custom_height_mm=_custom_height, custom_offset_x=_custom_offset_x, target_dpi=100)
                st.image(image_resize, width=200)
                if aspect_ratio_input > 1:
                    st.toast('For better results try to select vertical images, instead of wide ones', icon='⚠️')
    
    
    def get_postcard_tab(self):
        st.caption('Higher image quality yields superior final results 🚨')
        uploaded_file_handler = st.file_uploader("**Choose file:**", accept_multiple_files = False, type = ['jpg', 'png', 'jpeg'], key = self._key)
        if uploaded_file_handler is not None:
            # To read file as bytes:
            _image = uploaded_file_handler.getvalue()
            _image_pillow = Image.open(uploaded_file_handler)
            st.write('---')
            
            im_1,im_2,im_3 = st.columns((1,3,1))
            of1,of2,of3 = st.columns((1,3,1))
            with of2:
                _custom_offset_x = st.slider(f'{self._key}_xoffset', min_value = -50, max_value=50, value=0, step=1, label_visibility='hidden')
                st.markdown("<h6 style='text-align: center; color: #7F8487;'>X-axis align</h6>", unsafe_allow_html=True)
                _custom_offset_y = st.slider(f'{self._key}_yoffset', min_value = -100, max_value=100, value=0, step=1, label_visibility='hidden')
                st.markdown("<h6 style='text-align: center; color: #7F8487;'>Y-axis align</h6>", unsafe_allow_html=True)
                st.write('---')
                st.markdown("<h6 style='text-align: center; color: #171717;'>Move the slider (left or right) to fit the image.<br> Take your time! ⌛</h6>", unsafe_allow_html=True)
                create_button = st.button('C R E A T E', type='primary', key = f'{self._key}_sdsdsd')
                if create_button:
                    st.toast('EFRAIN APONTE', icon='🧟')
            # bt1,bt2,bt3 = st.columns((1,3,1))
            # with bt2:
            with im_2:
                _custom_width = POSTCARDS_SIZES[self._model_selected]['width']
                _custom_height = POSTCARDS_SIZES[self._model_selected]['height']
                image_resize,aspect_ratio_input = fill_custom_size_height(_image_pillow, custom_width_mm=_custom_width, custom_height_mm=_custom_height, custom_offset_x=_custom_offset_x,custom_offset_y = _custom_offset_y, target_dpi=100)
                st.image(image_resize, use_column_width=True)
                if aspect_ratio_input < 1:
                    st.toast('For better results try to select wide images, instead of vertical ones', icon='⚠️')