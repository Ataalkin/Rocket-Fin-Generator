import win32com.client
import math

def create_3d_solid_fin():
    try:
        print("\n🚀 ROKET KANATÇIK 3D OTOMASYONU")
        rc = float(input("👉 Kök (Root Chord) [mm]: "))
        tc = float(input("👉 Uç (Tip Chord) [mm]: "))
        h = float(input("👉 Yükseklik (Height) [mm]: "))
        sa = float(input("👉 Sweep Açısı (Derece): "))
        thick = float(input("👉 Kanatçık Kalınlığı [mm]: ")) # Yeni Giriş!

        swApp = win32com.client.Dispatch("SldWorks.Application")
        Part = swApp.ActiveDoc
        if Part is None:
            print("❌ HATA: SolidWorks'te yeni bir 'Part' dosyası açın!")
            return

        # Birim Çevrimleri (mm -> m)
        rc_m = rc / 1000
        tc_m = tc / 1000
        h_m = h / 1000
        thick_m = thick / 1000
        sd_m = (h * math.tan(math.radians(sa))) / 1000

        # 1. Çizim (Sketch) Aşaması
        Part.SketchManager.InsertSketch(True)
        Part.SketchManager.CreateLine(0, 0, 0, rc_m, 0, 0)
        Part.SketchManager.CreateLine(rc_m, 0, 0, sd_m + tc_m, h_m, 0)
        Part.SketchManager.CreateLine(sd_m + tc_m, h_m, 0, sd_m, h_m, 0)
        Part.SketchManager.CreateLine(sd_m, h_m, 0, 0, 0, 0)
        Part.SketchManager.InsertSketch(True)

        # 2. Üçüncü Boyut (Extrude) Aşaması
        print(f"🧱 {thick}mm kalınlık veriliyor...")
        # FeatureExtrusion2(SD, Flip, Dir, T1, T2, D1, D2, WithDraft, DraftDir, ...)
        # Sadece kalınlık (D1) ve yön (SD=True) kısımlarını kullanıyoruz.
        Part.FeatureManager.FeatureExtrusion2(True, False, False, 0, 0, thick_m, 0, False, False, False, False, 0, 0, False, False, False, False, True, True, True, 0, 0, False)

        Part.ViewZoomtofit2()
        print(f"\n✅ BAŞARILI: 3D Kanatçık MSI laptop'ında canlandı!")

    except Exception as e:
        print(f"\n❌ HATA: {e}")

if __name__ == "__main__":
    create_3d_solid_fin()