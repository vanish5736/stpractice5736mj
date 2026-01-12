import streamlit as st

st.title("🐰 MJ's page")
st.write("**This is a page of MJ!** We are right now mid session.")
st.write("Does it not matter if I enter? Another code just separated the paragraph automatically.")

# 정보성 메시지 박스
st.info("ℹ️ 정보 메시지입니다.")
st.warning("⚠️ 경고 메시지입니다.")
st.success("✅ 성공 메시지입니다.")
st.error("❌ 오류 메시지입니다.")

st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6uAX2ocay9_KDio_M5mH1GjuS2XbE5CQZ2Q&s", caption="it's a bunny", use_container_width=True)
st.image("https://media.istockphoto.com/id/499124260/photo/white-rabbit-close-up.jpg?s=612x612&w=0&k=20&c=6ubyY4MwngyBjIAKwA8IeBIVYNjZ4nN7StrOlSHSVHo=", caption="another bunny")