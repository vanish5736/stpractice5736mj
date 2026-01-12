import streamlit as st

st.title("🐰 MJ's page")
st.write("**This is a page of MJ!** We are right now mid session.")
st.write("Separating the paragraphs automatically.")

# 정보성 메시지 박스
st.info("ℹ️ 정보 메시지입니다.")
st.warning("⚠️ 경고 메시지입니다.")
st.success("✅ 성공 메시지입니다.")
st.error("❌ 오류 메시지입니다.")

st.image("https://cdn.shopify.com/s/files/1/0040/8997/0777/files/Cute_Bunny_7d_1024x1024.jpg?v=1698453869", caption="it's a bunny", use_container_width=True)
st.image("https://media.istockphoto.com/id/499124260/photo/white-rabbit-close-up.jpg?s=612x612&w=0&k=20&c=6ubyY4MwngyBjIAKwA8IeBIVYNjZ4nN7StrOlSHSVHo=", caption="another bunny", use_container_width=True)