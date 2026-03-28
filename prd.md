# 📄 Ürün Gereksinim Belgesi (PRD) - Green Alloy AI

## 🎯 Ürün Özeti
Green Alloy AI, metalurji ve malzeme mühendisliği öğrencileri ile profesyonelleri için tasarlanmış, 13 farklı metal üzerinden dinamik alaşım hesaplamaları yapan ve AI destekli mühendislik yorumları sunan bir dashboard uygulamasıdır.

## 🧐 Problem Tanımı
Metalurji eğitiminde ve pratik uygulamalarda, alaşım oranlarının fiziksel özellikler (sertlik, korozyon direnci, özgül ağırlık vb.) üzerindeki etkilerini anlık olarak görselleştirmek ve bu verileri sektörel standartlara göre yorumlamak zaman alıcıdır.

## ✨ Çözüm
Kullanıcının sliderlar aracılığıyla belirlediği metal oranlarını (Krom, Lityum vb.) anında bir donut chart üzerinde görselleştiren ve Google Gemini API kullanarak bu karışıma özel "Mühendislik Tavsiyesi" üreten bir web aracı.

## 🛠️ Teknik Gereksinimler
- **Arayüz:** Streamlit (Python tabanlı hızlı web arayüzü)
- **Veri:** Pandas (Metal özelliklerinin hesaplanması için)
- **AI:** Google Gemini Pro (Analiz ve tavsiye üretimi için)
- **Yayınlama:** Streamlit Cloud
