import streamlit as st

st.title("🐰 MJ's page")
st.write("**This is a page of MJ!** We are right now mid session.")
st.write("Separating the paragraphs automatically.")

st.success("✅ 성공 메시지입니다.")

# st.expander("제목"): 내용을 접었다 펼 수 있는 컨테이너입니다
with st.expander("❤️  I hid bunnies here"):
    st.write("Here are some bunnies for you!")
    st.image("https://cdn.shopify.com/s/files/1/0040/8997/0777/files/Cute_Bunny_7d_1024x1024.jpg?v=1698453869", caption="it's a bunny", use_container_width=True)
    st.image("https://media.istockphoto.com/id/499124260/photo/white-rabbit-close-up.jpg?s=612x612&w=0&k=20&c=6ubyY4MwngyBjIAKwA8IeBIVYNjZ4nN7StrOlSHSVHo=", caption="another bunny", use_container_width=True)

st.divider() 

    # 파일 업로드: 파일을 선택하면 BytesIO 객체로 반환됩니다
uploaded_file = st.file_uploader("Submit your HWP file here.", type=["hwp"])
if uploaded_file:
    import pandas as pd
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)