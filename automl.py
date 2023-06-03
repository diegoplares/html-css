import pandas as pd
import streamlit as st
import datetime

from sklearn.datasets import fetch_openml

# dataset = openml.dataset.get_dataset('iris')
# df = dataset.get_dataframe()
# st.dataframe (df)

dataset = fetch_openml('iris')
df = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
df['target'] = dataset.target

with st.sidebar:
    st.image('./logo.png')
    st.title("AutoML")
    choice = st.radio("Navigation",["Data Preprocessing","Data Profiling","Cash","Download"])
    st.info("You can navigate through each of the sections")
st.write("This is an automated machin learning project")

if choice =="Data Preprocessing":
    st.write("This section is under development please make sure that the data is preprocessed accordingly")
    st.info("Only preprocessed data can make good results")

    options =("Upload your data","Default Test data")
    input = st.selectbox("Select your Data loading methods",options)

    if input == "Upload your data":
        uploaded_file=st.file_uploader("Upload Data")

        if uploaded_file is not None:
            df =pd.read_csv(uploaded_file)
            st.dataframe(df)

    if input == "Default Test data":
        from sklearn.datasets import fetch_openml
        # dataset = openml.dataset.get_dataset('iris')
        # df = dataset.get_dataframe()
        # st.dataframe (df)

        dataset = fetch_openml('iris')
        df =pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
        df['target']= dataset.target
        st.dataframe(df)
        pass


if choice =="Data Profiling":
    import pandas_profiling
    from streamlit_pandas_profiling import st_profile_report
    st.title("Explore today data analysis")
    profile_report = df.profile_report()
    st_profile_report(profile_report)
    pass

if choice =="Cash":
    st.checkbox("Yes")
    st.checkbox("No")
    st.button("Submit")
    st.multiselect("Favorite food",["Burger", "Pizza", "Iceacream"])
    st.select_slider("Rate the movie", ["Good", "Average", "Bad"])
    st.slider("Choose number", 0,50)

    st.number_input("Enter your age: ", 0,100)
    st.text_input("Enter your name:")
    min_date = datetime (1920,1,1)
    max_date = datetime(2030,12,31)
    st.date_input("Choose your DOB", min_value=min_date,max_value=max_date)
    st.text_input("When should we stop the class?")
    st.text_area("How do you feel today?:")
    st.color_picker("Choose your favorite color")

    pass

if choice =="Download":
    st.video('https://www.youtube.com/watch?v=hvF5wWChxbk')

    name = st.text_input("Enter your name:")
    options = ('select',"Tacos", "Chilaquiles",'Tortas','Tostadas')
    input = st.selectbox("Select your favorite food", options)

    if input == 'Tacos':
        st.write('thank you {} for choosing tacos'.format(name))
        st.video('https://www.youtube.com/watch?v=OO9kSxcT9Rg')


    if input == 'Chilaquiles':
        st.video('https://www.youtube.com/watch?v=nH7MSS6zxe4')
        st.write ('Variedad de tacos')

    if input == 'Tortas':
        st.video('https://www.youtube.com/watch?v=MQMFa6wwGco')
        st.write ('Variedad de tacos')

    if input == 'Tostadas':
        st.video('https://www.youtube.com/watch?v=NlTprxvNRgs')
        st.write ('Variedad de tacos')

    pass