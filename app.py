import streamlit as st

# 1. إعدادات الهوية البصرية
st.set_page_config(page_title="حاسبة فقيش", page_icon="⚖️")

logo_url = "https://image2url.com/r2/default/images/1772046217248-c9e7d8cc-4d59-4c2a-bd75-981920c403a8.png"

st.markdown(f"""
    <div style='text-align: center;'>
        <img src='{logo_url}' width='180'>
        <h1 style='color: #D4AF37;'>حاسبة فقيش</h1>
        <h4 style='color: #555;'>خيارك.. حتى ما حد يستغلك</h4>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 2. الأسعار العالمية
ounce_price = st.number_input("أدخل سعر الأونصة ($):", value=2025.0)

usd_to_aed = 3.6725
g24 = (ounce_price / 31.1035) * usd_to_aed
g21 = g24 * 0.875
g18 = g24 * 0.75

# 3. مدخلات الحسبة
karat = st.selectbox("اختر العيار:", ["21", "18", "24"])
weights = st.text_input("أدخل الأوزان (مثلاً 10+5):", value="0")

total_w = 0.0
try:
    total_w = sum([float(x.strip()) for x in weights.replace('+', ',').split(',') if x.strip()])
except:
    st.error("⚠️ يرجى التأكد من الأرقام")

making_per_gram = st.number_input("المصنعية للغرام الواحد (AED):", value=0.0)

# الحسابات التفصيلية
price_map = {"24": g24, "21": g21, "18": g18}
current_gram_price = price_map[karat]

gold_only_total = current_gram_price * total_w  # سعر الذهب لحال
total_making = making_per_gram * total_w      # مجموع المصنعية لحال
tax_amount = (gold_only_total + total_making) * 0.05 # الضريبة لحال
grand_total = gold_only_total + total_making + tax_amount # الإجمالي النهائي

# 4. عرض الفاتورة المفصلة (فوق بعض)
st.write("---")
st.markdown(f"""
<div style='text-align: center; border: 2px solid #D4AF37; padding: 25px; border-radius: 20px; background-color: #ffffff;'>
    <div style='text-align: right; display: inline-block; width: 100%; direction: rtl;'>
        <p style='color: #333; font-size: 18px;'>⚖️ الوزن الإجمالي: <b>{total_w:.2f} غرام</b></p>
        <p style='color: #333; font-size: 18px;'>💰 قيمة الذهب (بدون إضافات): <b>{gold_only_total:.2f} درهم</b></p>
        <p style='color: #333; font-size: 18px;'>🛠️ مجموع المصنعية: <b>{total_making:.2f} درهم</b></p>
        <p style='color: #333; font-size: 18px;'>📜 ضريبة القيمة المضافة (5%): <b>{tax_amount:.2f} درهم</b></p>
    </div>
    <hr style='border: 1px solid #D4AF37; margin: 20px 0;'>
    <p style='color: #555; font-size: 22px; font-weight: bold;'>الإجمالي النهائي (شامل كل شيء):</p>
    <h1 style='color: #D4AF37; font-size: 50px; margin: 0;'>{grand_total:.2f} درهم</h1>
</div>
""", unsafe_allow_html=True)
