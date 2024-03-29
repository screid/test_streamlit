import streamlit as st

#Colocar titulo
st.title ("this is the app title")

st.header("this is the header")
st.markdown("this is the markdown")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

#Colocar texto random
st.write("Hello ,let's learn how to build a streamlit app together")

#Botones
boton_imagen = st.button('Click')
if boton_imagen == True:
    st.image("decir_no.png")

#Widgets
#Checkbox
checkbox_yes = st.checkbox('yes')
if checkbox_yes == True:
    st.write("Presionado :)")

#Radio
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)

#Otros
st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

st.progress(10)
# with st.spinner('Wait for it...'):
#     time.sleep(10)



st.sidebar(
#Mostrar mensajes
)


st.success("You did it !")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))

#Mas cosas: https://www.datacamp.com/tutorial/streamlit