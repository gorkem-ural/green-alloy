def karbon_ayak_izi_hesapla(metal_tipi, miktar):
    # Basit geri dönüşüm ve emisyon verileri (Temsili mühendislik verileri)
    veriler = {
        "Alüminyum": {"emisyon": 12.0, "geri_donusum": 0.9},
        "Bakır": {"emisyon": 3.5, "geri_donusum": 0.8},
        "Çelik": {"emisyon": 1.9, "geri_donusum": 0.7}
    }
    
    if metal_tipi in veriler:
        emisyon = miktar * veriler[metal_tipi]["emisyon"]
        donusum_skoru = miktar * veriler[metal_tipi]["geri_donusum"]
        return emisyon, donusum_skoru
    return 0, 0