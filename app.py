import streamlit as st

# 1. إعدادات الهوية البصرية (مجوهرات فقيش)
st.set_page_config(page_title="حاسبة فقيش", page_icon="⚖️")

# رابط اللوغو الخاص بك
logo_url = "https://image2url.com/r2/default/images/1772046217248-c9e7d8cc-4d59-4c2a-bd75-981920c403a8.png"

st.markdown(f"""
    <div style='text-align: center;'>
        <img src='{logo_url}' width='180'>
        <h1 style='color: #D4AF37;'>حاسبة فقيش</h1>
        <h4 style='color: #555;'>خيارك.. حتى ما حد يستغلك</h4>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 2. إدخال الأسعار (البورصة العالمية) وعرض سعر الغرام
st.markdown("<h3 style='color: #D4AF37;'>💰 أسعار الذهب اللحظية (AED)</h3>", unsafe_allow_html=True)
ounce_price = st.number_input("أدخل سعر الأونصة ($):", value=2025.0)

usd_to_aed = 3.6725
gram_24 = (ounce_price / 31.1035) * usd_to_aed
gram_21 = gram_24 * 0.875
gram_18 = gram_24 * 0.75

# عرض أسعار الغرام بوضوح في الأعلى
col1, col2, col3 = st.columns(3)
col1.metric("سعر عيار 24", f"{gram_24:.2f}")
col2.metric("سعر عيار 21", f"{gram_21:.2f}")
col3.metric("سعر عيار 18", f"{gram_18:.2f}")

st.write("---")

# 3. حساب الوزن والمصنعية
st.markdown("<h3 style='color: #D4AF37;'>⚖️ تفاصيل الحسبة</h3>", unsafe_allow_html=True)
karat = st.selectbox("اختر العيار المطلوب حسابه:", ["21", "18", "24"])
weights = st.text_input("أدخل الأوزان (مثال: 10+5):", value="0")

total_w = 0.0
try:
    total_w = sum([float(x.strip()) for x in weights.replace('+', ',').split(',') if x.strip()])
except:
    st.warning("يرجى إدخال أرقام صحيحة")

making = st.number_input("المصنعية للغرام الواحد (AED):", value=0.0)

# الحسابات المالية
price_list = {"24": gram_24, "21": gram_21, "18": gram_18}
base_price = price_list[karat]

gold_value_only = base_price * total_w
total_with_making = (base_price + making) * total_w
grand_total = total_with_making * 1.05

# 4. عرض النتائج النهائية بوضوح
st.write("---")
st.markdown(f"""
