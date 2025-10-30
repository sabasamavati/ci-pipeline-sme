# ci_pipeline/run_pipeline.py
import os

# مسیر خروجی روی Runner گیتهاب:
BASE = os.getenv("BASE", "./run_out")
TABLES_DIR = os.path.join(BASE, "tables")
SNAPSHOT_DIR = os.path.join(BASE, "snapshots")

def main():
    # --- TODO: منطق فعلی‌ات را از Colab اینجا کپی کن ---
    # نکته: هرجا قبلا BASE="/content/..." بود، همان BASE بالا را استفاده کن
    # و در پایان فایل‌ها را داخل BASE/.. ذخیره کن.
    os.makedirs(TABLES_DIR, exist_ok=True)
    os.makedirs(SNAPSHOT_DIR, exist_ok=True)
    print("Pipeline ran. Write your CSV/XLSX into:", BASE)

if __name__ == "__main__":
    main()
