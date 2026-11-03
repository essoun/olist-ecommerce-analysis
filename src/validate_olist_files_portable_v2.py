
from pathlib import Path
import csv
import sys
import zipfile

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data" / "raw"
ARCHIVE = DATA_DIR / "brazilian-ecommerce.zip"

EXPECTED_FILES = {
    "olist_customers_dataset.csv",
    "olist_geolocation_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_order_payments_dataset.csv",
    "olist_order_reviews_dataset.csv",
    "olist_orders_dataset.csv",
    "olist_products_dataset.csv",
    "olist_sellers_dataset.csv",
    "product_category_name_translation.csv",
}

def main():
    print("=" * 60)
    print("OLIST DATASET VALIDATION")
    print("=" * 60)

    found_files = {p.name for p in DATA_DIR.glob("*.csv")}

    missing = EXPECTED_FILES - found_files
    extra = found_files - EXPECTED_FILES

    print(f"Expected CSV files: {len(EXPECTED_FILES)}")
    print(f"Found CSV files:    {len(found_files)}")
    print(f"Missing files:      {sorted(missing)}")
    print(f"Unexpected files:   {sorted(extra)}")

    valid = not missing and not extra

    if not ARCHIVE.is_file():
        print("Archive: NOT PRESENT (optional)")
    else:
        try:
            with zipfile.ZipFile(ARCHIVE) as zf:
                damaged = zf.testzip()
            archive_ok = damaged is None
            print("Archive integrity:", "PASS" if archive_ok else "FAIL")
            valid = valid and archive_ok
        except (zipfile.BadZipFile, OSError) as error:
            print("Archive integrity: FAIL")
            print("Archive error type:", type(error).__name__)
            valid = False

    for filename in sorted(found_files):
        path = DATA_DIR / filename
        with path.open(
            "r", encoding="utf-8-sig", newline=""
        ) as handle:
            reader = csv.reader(handle)
            header = next(reader, None)

        if not header:
            print(f"FAIL: {filename} has no header")
            valid = False
            continue

        size = path.stat().st_size
        print(f"\nFILE: {filename}")
        print(f"SIZE: {size:,} bytes")
        print(f"COLUMNS: {len(header)}")
        print(f"HEADER: {header}")

        if len(set(header)) != len(header):
            print("FAIL: Duplicate column names")
            valid = False

    print("\nOVERALL:", "PASS" if valid else "FAIL")
    return 0 if valid else 1

if __name__ == "__main__":
    sys.exit(main())
