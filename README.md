# 🚀 Rocket Fin Generator for SolidWorks

Bu proje, Python ve SolidWorks API kullanarak aerodinamik roket kanatçıklarını (Fin) otomatik olarak modelleyen bir mühendislik aracıdır.

## ✨ Özellikler
- **Hassas Geometri:** Manuel çizim hatalarını önleyen `CreateLine` algoritması.
- **Tam Otomasyon:** Sketch aşamasından sonra otomatik `Extrude` (katılaştırma).
- **Parametrik:** Değerleri girin, 3D model saniyeler içinde oluşsun.

## 🛠️ Kurulum & Kullanım
1. `pip install -r requirements.txt` komutuyla kütüphaneyi kurun.
2. SolidWorks'ü açıp yeni bir **Part** dosyası oluşturun.
3. `python fin_generator.py` komutuyla aracı çalıştırın.