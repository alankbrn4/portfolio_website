import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key="api_key")

model = genai.GenerativeModel('gemini-1.5-flash')

col1 , col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title('I am Alan Blanco')

with col2:
    st.image("images/AlanBlanco.jpg", width=200)


st.title('Welcome to my portfolio website!')
st.title(' ')

persona = """
        You are Murtaza AI bot. You help people answer questions about your self (i.e Murtaza)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Murtaza: 

        Murtaza Hassan is an Educator/Youtuber/Entrepreneur in the field of Computer Vision and Robotics.
        He runs one of the largest YouTube channels in the field of Computer Vision,
        educating over 3 Million developers,
        hobbyists and students. Murtaza obtained his Bachelor’s degree in
        Mechatronics and later specialized in the field of Robotics from
        Bristol University (UK). He is also a serial entrepreneur having launched several
        successful ventures including CVZone, which is a one stop solution for learning 
        and building vision projects. Prior to starting his entrepreneurial career, 
        Murtaza worked as a university lecturer and a design engineer, evaluating 
        and developing rapid prototypes of US patents.

        Murtaza's Youtube Channel: https://www.youtube.com/channel/UCYUjYU5FveRAscQ8V21w81A
        Murtaza's Email: contact@murtazahassan.com 
        Murtaza's Facebook: https://www.facebook.com/murtazasworkshop
        Murtaza's Instagram: https://www.instagram.com/murtazasworkshop/
        Murtaza's Linkdin: https://www.linkedin.com/in/murtaza-hassan-8045b38a/
        Murtaza's Github :https://github.com/murtazahassan
        """

st.title("Alan's AI Bot")

user_question = st.text_input("Ask anything about me")
if st.button("ASK", use_container_width=400):
    prompt = persona +"Here is the question that the user asked: " +  user_question
    response = model.generate_content(prompt)
    st.write(response.text)

col1 , col2 = st.columns(2)
with col1:
    st.subheader("Youtube Channel")
    st.write("- Subscribe to my channel")
    st.write("- Amazing projects")
    st.write("- Over 45 Free Video Tutorials")
    st.write("- Amazing promotions")

with col2:
    st.video("https://youtu.be/kCDBHrwNCX4")

st.title(' ')

st.title('My Setup')
st.image("images/setup.jpg")

st.write(' ')
st.title('My Skills')
st.slider("Programming", 0, 100, 50)
st.slider("Teaching", 0, 100, 90)
st.slider("Robotics", 0, 100, 50)
st.slider("Web Development", 0, 100, 30)
st.slider("Data Science", 0, 100, 40)
st.slider("Computer Vision", 0, 100, 50)

st.write(' ')
st.title('Gallery')

st.write('Here are some of my projects:')
col1 , col2, col3 = st.columns(3)
with col1:
    st.image("images/g1.jpg")
    st.image("images/g2.jpg")
    st.image("images/g3.jpg")
with col2:
    st.image("images/g4.jpg")
    st.image("images/g5.jpg")
    st.image("images/g6.jpg")
with col3:
    st.image("images/g7.jpg")
    st.image("images/g8.jpg")
    st.image("images/g9.jpg")

st.write('Here is my LinkedIn:')
st.write('LinkedIn')
st.write('Here is my GitHub:')
st.write('GitHub')
st.write('Here is my email:')
st.write('Email')
st.write('Here is my phone number:')
st.write('Phone number')
st.write('Here is my address:')
st.write('Address')
st.write('Here is my location:')
st.write('Location')

st.subheader(' ')
st.write('CONTACT')
st.title('For any inquiries, email at:')
st.subheader('ablancom@utleon.edu.mx')


