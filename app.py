import streamlit as st

# 1. إعدادات الهوية البصرية (مجوهرات فقيش)
st.set_page_config(page_title="حاسبة فقيش", page_icon="⚖️")

# رابط اللوغو الأصلي الخاص بك
logo_url = "https://image2url.com/r2/default/images/1772046217248-c9e7d8cc-4d59-4c2a-bd75-981920c403a8.png"

st.markdown(f"""
    <div style='text-align: center;'>
        <img src='{logo_url}' width='180'>
        <h1 style='color: #D4AF37;'>حاسبة فقيش</h1>
        <h4 style='color: #555;'>خيارك.. حتى ما حد يستغلك</h4>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 2. إدخال الأسعار (الحسابات بالدرهم الإماراتي)
ounce_price = st.number_input("أدخل سعر الأونصة ($):", value=2025.0)

usd_to_aed = 3.6725
gram_24 = (ounce_price / 31.1035) * usd_to_aed
gram_21 = gram_24 * 0.875
gram_18 = gram_24 * 0.75

# عرض العيارات
c1, c2, c3 = st.columns(3)
c1.metric("عيار 24", f"{gram_24:.2f} AED")
c2.metric("عيار 21", f"{gram_21:.2f} AED")
c3.metric("عيار 18", f"{gram_18:.2f} AED")

st.write("---")

# 3. حساب الوزن والمصنعية
karat = st.selectbox("اختر العيار:", ["21", "18", "24"])
weights = st.text_input("أدخل الأوزان (مثال: 10+5.5):", value="0")

total_w = 0.0
try:
    total_w = sum([float(x.strip()) for x in weights.replace('+', ',').split(',') if x.strip()])
except:
    st.error("يرجى كتابة الوزن بشكل صحيح")

making = st.number_input("المصنعية للغرام الواحد (AED):", value=0.0)

# الحسابات (تصحيح خطأ Syntax السابق)
price_list = {"24": gram_24, "21": gram_21, "18": gram_18}
base_gold_price = price_list[karat]

# قيمة الذهب بدون مصنعية فقط
gold_value_only = base_gold_price * total_w
# الإجمالي (ذهب + مصنعية + ضريبة 5%)
total_with_making = (base_gold_price + making) * total_w
grand_total = total_with_making * 1.05

# 4. عرض الفاتورة النهائية للزبون
st.write("---")
st.markdown(f"""
<div style='text-align: center; border: 2px solid #D4AF37; padding: 25px; border-radius: 20px; background-color: #fcfcfc;'>
    <p style='font-size: 18px;'>الوزن الإجمالي: <b>{total_w:.2f} غرام</b></p>
    <p style='font-size: 19px;'>قيمة الذهب بدون مصنعية فقط: <br><b>{gold_value_only:.2f} AED</b></p>
    <hr style='border: 1px dashed #D4AF37; width: 50%; margin: 15px auto;'>
    <p style='font-size: 22px; color: #555;'>قيمة الذهب مع الضريبة (الإجمالي):</p>
    <h1 style='color: #D4AF37; font-size: 45px; margin: 0;'>{grand_total:.2f} درهم</h1>
</div>
""", unsafe_allow_html=True)