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

# 2. إدخال الأسعار (البورصة العالمية)
ounce_price = st.number_input("أدخل سعر الأونصة ($):", value=2025.0)

usd_to_aed = 3.6725
gram_24 = (ounce_price / 31.1035) * usd_to_aed
gram_21 = gram_24 * 0.875
gram_18 = gram_24 * 0.75

st.write("---")

# 3. حساب الوزن والمصنعية
karat = st.selectbox("اختر العيار:", ["21", "18", "24"])
weights = st.text_input("أدخل الأوزان (مثال: 10+5):", value="0")

# جمع الأوزان تلقائياً
total_w = 0.0
try:
    total_w = sum([float(x.strip()) for x in weights.replace('+', ',').split(',') if x.strip()])
except:
    st.warning("يرجى إدخال أرقام صحيحة في خانة الوزن")

making = st.number_input("المصنعية للغرام الواحد (AED):", value=0.0)

# الحسابات المالية
price_list = {"24": gram_24, "21": gram_21, "18": gram_18}
base_price = price_list[karat]

# قيمة الذهب الصافي (بدون أي إضافات)
gold_value_only = base_price * total_w
# الإجمالي مع المصنعية والضريبة 5%
total_with_making = (base_price + making) * total_w
grand_total = total_with_making * 1.05

# 4. عرض النتائج النهائية (حل مشكلة اختفاء النصوص)
st.write("---")
st.markdown(f"""
<div style='text-align: center; border: 2px solid #D4AF37; padding: 25px; border-radius: 20px; background-color: #ffffff;'>
    <p style='color: #333; font-size: 18px;'>الوزن الإجمالي: <b>{total_w:.2f} غرام</b></p>
    <p style='color: #333; font-size: 20px;'>قيمة الذهب بدون مصنعية فقط:</p>
    <h3 style='color: #555;'>{gold_value_only:.2f} AED</h3>
    <hr style='border: 1px dashed #D4AF37; width: 60%; margin: 20px auto;'>
    <p style='color: #333; font-size: 22px;'>قيمة الذهب مع الضريبة (الإجمالي):</p>
    <h1 style='color: #D4AF37; font-size: 45px; margin: 0;'>{grand_total:.2f} درهم</h1>
</div>
""", unsafe_allow_html=True)
