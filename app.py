import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# 1. Sayfa Ayarları
st.set_page_config(page_title="Green Alloy AI - Ultimate 13", page_icon="🔬", layout="wide")

# Görünüm Özelleştirme
st.markdown("""
<style>
    .main-title { font-size:32px; font-weight: bold; color: #1B5E20; text-align: center; }
    .stMetric { background-color: #f8f9fa; border-radius: 15px; border-left: 5px solid #2E7D32; }
</style>
""", unsafe_allow_html=True)


   # 2. EKSİKSİZ 13 METAL VERİTABANI (Sertlik Değerleri Eklendi)
metal_db = {
    "Demir": {"yogunluk": 7.87, "erime": 1538, "emisyon": 2.0, "fiyat": 0.6, "sertlik": 80, "not": "Dayanıklılığın ve sanayinin sarsılmaz temeli."},
    "Alüminyum": {"yogunluk": 2.70, "erime": 660, "emisyon": 12.0, "fiyat": 2.5, "sertlik": 25, "not": "Geleceğin hafif ve geri dönüştürülebilir gücü."},
    "Bakır": {"yogunluk": 8.96, "erime": 1085, "emisyon": 3.5, "fiyat": 9.2, "sertlik": 50, "not": "Enerjiyi ve iletişimi birbirine bağlayan hat."},
    "Titanyum": {"yogunluk": 4.50, "erime": 1668, "emisyon": 15.0, "fiyat": 18.0, "sertlik": 180, "not": "Havacılığın ekstrem koşullara dayanan süper metali."},
    "Nikel": {"yogunluk": 8.90, "erime": 1455, "emisyon": 6.5, "fiyat": 20.0, "sertlik": 150, "not": "Korozyona karşı koruyucu ve birleştirici güç."},
    "Krom": {"yogunluk": 7.19, "erime": 1907, "emisyon": 7.5, "fiyat": 5.0, "sertlik": 900, "not": "Sertlik, parlaklık ve paslanmazlık katan zırh."},
    "Çinko": {"yogunluk": 7.14, "erime": 419, "emisyon": 3.0, "fiyat": 3.0, "sertlik": 40, "not": "Koruyucu galvaniz katmanı ve dayanıklılık."},
    "Magnezyum": {"yogunluk": 1.74, "erime": 650, "emisyon": 14.0, "fiyat": 3.5, "sertlik": 35, "not": "En hafif yapısal metal; verimliliğin anahtarı."},
    "Gümüş": {"yogunluk": 10.49, "erime": 961, "emisyon": 150, "fiyat": 850, "sertlik": 30, "not": "Zarafetle birleşen en yüksek elektriksel iletkenlik."},
    "Altın": {"yogunluk": 19.30, "erime": 1064, "emisyon": 12500, "fiyat": 68000, "sertlik": 25, "not": "Bozulmaz değer ve mükemmel mühendislik çözümü."},
    "Lityum": {"yogunluk": 0.53, "erime": 180, "emisyon": 18.0, "fiyat": 25.0, "sertlik": 5, "not": "Yeni enerji çağının ve batarya teknolojisinin kalbi."},
    "Platin": {"yogunluk": 21.45, "erime": 1768, "emisyon": 12000, "fiyat": 32000, "sertlik": 40, "not": "Tepkimeleri başlatan nadir ve dönüştürücü güç."},
    "Niyobyum": {"yogunluk": 8.57, "erime": 2477, "emisyon": 40.0, "fiyat": 45.0, "sertlik": 130, "not": "Süperiletkenlik ve yüksek sıcaklık mukavemeti."}
}


st.markdown("<div class='main-title'>👩‍🔬 Green Alloy AI: 13 Stratejik Metal Analizi</div>", unsafe_allow_html=True)
st.divider()

# 3. Yan Panel
with st.sidebar:
    st.header("🧪 Alaşım Tasarımı")
    m1 = st.selectbox("1. Ana Metal:", sorted(list(metal_db.keys())), index=4) # Demir varsayılan
    oran1 = st.slider(f"{m1} Oranı (%)", 0, 100, 80)
    
    oran2 = 100 - oran1
    m2 = st.selectbox("2. Katkı Metali:", sorted(list(metal_db.keys())), index=11) # Titanyum varsayılan
    
    st.info(f"Reçete: %{oran1} {m1} + %{oran2} {m2}")
    total_weight = st.number_input("Toplam Miktar (kg):", value=100)

    # Hesaplamalar
    alloy_density = (oran1 * metal_db[m1]["yogunluk"] + oran2 * metal_db[m2]["yogunluk"]) / 100
    alloy_cost = (oran1 * metal_db[m1]["fiyat"] + oran2 * metal_db[m2]["fiyat"]) / 100 * total_weight
    alloy_emission = (oran1 * metal_db[m1]["emisyon"] + oran2 * metal_db[m2]["emisyon"]) / 100 * total_weight

    st.markdown("---")
    # Rapor Hazırlama
    report_df = pd.DataFrame({
        "Parametre": ["Tarih", "Alaşım", "Kompozisyon", "Yoğunluk", "Maliyet", "Emisyon"],
        "Değer": [datetime.now().strftime('%d/%m/%Y'), f"{m1}-{m2}", f"%{oran1}-%{oran2}", f"{alloy_density:.2f}", f"${alloy_cost:,.2f}", f"{alloy_emission:,.2f}"]
    })
    st.download_button("📥 Mühendislik Raporunu İndir", data=report_df.to_csv(index=False).encode('utf-8'), file_name="GreenAlloy_13_Report.csv", mime='text/csv')

# 4. Ana Panel Metrikleri
c1, c2, c3 = st.columns(3)
c1.metric("Alaşım Yoğunluğu", f"{alloy_density:.2f} g/cm³")
c2.metric("Üretim Maliyeti", f"${alloy_cost:,.2f}")
c3.metric("Karbon Ayak İzi", f"{alloy_emission:,.2f} kg CO2")

st.divider()

# 5. Görselleştirme
col_left, col_right = st.columns([1, 2])

with col_left:
    fig_pie = px.pie(names=[m1, m2], values=[oran1, oran2], hole=0.5, title="Alaşım Dağılımı", color_discrete_sequence=px.colors.qualitative.Safe)
    st.plotly_chart(fig_pie, use_container_width=True)

with col_right:
            all_data_df = pd.DataFrame(metal_db).T
            all_data_df.index.name = 'Metal'
            all_data_df = all_data_df.reset_index()
            all_data_df['fiyat'] = pd.to_numeric(all_data_df['fiyat'], errors='coerce')
            fig_bubble = px.scatter(all_data_df, x="yogunluk", y="emisyon", size="fiyat", color="Metal", 
                                    hover_name="Metal", title="13 Metal Analizi: Yoğunluk vs Emisyon",
                                    template="plotly_white")
        

# 6. AI Karar Destek ve Geliştiren Kadınlar Notları
st.divider()
col_ai, col_note = st.columns(2)

with col_ai:
    st.subheader("🔍 Mühendislik Tavsiyesi (AI)")
    if alloy_density < 1.0: st.success("🚀 İnanılmaz! Bu alaşım suyun üzerinde bile yüzebilir (Lityum etkisi).")
    if alloy_emission > 1000: st.warning("⚠️ Yüksek Karbon: Bu alaşım çevresel açıdan zorlayıcıdır.")
    if "Platin" in [m1, m2] or "Altın" in [m1, m2]: st.info("💎 Değerli Metal: Bu alaşım yüksek ekonomik değere ve korozyon direncine sahiptir.")
# --- 94. Satıra Gelecek Fonksiyon ve Hesaplama ---

def sertlik_hesapla(m1, m2, o1, o2):
    # Vickers Sertlik Değerleri (HV)
    sertlik_verileri = {
        "Demir": 80, "Alüminyum": 25, "Bakır": 50, "Titanyum": 180, 
        "Nikel": 150, "Krom": 900, "Çinko": 40, "Magnezyum": 35, 
        "Gümüş": 30, "Altın": 25, "Lityum": 5, "Platin": 40, "Niyobyum": 130
    }
    # Karışımlar kuralı ile tahmini sertlik
    tahmini_sertlik = (o1 * sertlik_verileri[m1] + o2 * sertlik_verileri[m2]) / 100
    return tahmini_sertlik

# Hesaplamayı Çağır
alloy_hardness = sertlik_hesapla(m1, m2, oran1, oran2)

# Not: Bu değeri ekranda göstermek için c4 diye yeni bir sütun ekleyebilir 
# veya mevcut metriklerin yanına koyabilirsin:
# st.metric("Tahmini Sertlik", f"{alloy_hardness:.1f} HV")
with col_note:
    st.subheader("💡 Geliştiren Kadınlar Köşesi")
    st.write(f"**{m1}:** {metal_db[m1]['not']}")
    st.write(f"**{m2}:** {metal_db[m2]['not']}")
    st.caption("Farklı özelliklerin uyumu, en güçlü alaşımı ve en güçlü toplumu oluşturur.")
