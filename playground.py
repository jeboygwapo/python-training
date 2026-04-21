import pandas as pd
import glob
import os

path = "/Users/jayveemacaraeg/Projects/DCPs/*.xls"
all_files = glob.glob(path)

df_list = []

print(f"Scanning {len(all_files)} files...")

for f in all_files:
    try:
        # 1. Read second sheet (index 1) as a raw grid
        raw_df = pd.read_excel(f, engine='xlrd', sheet_name=1, header=None)

        # 2. Find the exact cell for "Depth (mm)" to anchor our search
        start_row, start_col = None, None
        for r in range(len(raw_df)):
            for c in range(len(raw_df.columns)):
                cell_value = str(raw_df.iloc[r, c])
                if "Depth (mm)" in cell_value:
                    start_row, start_col = r, c
                    break
            if start_row is not None: break

        if start_row is not None:
            # 3. Extract exactly 3 rows of data starting from the row AFTER the header
            # Based on your image, the data is 3 rows deep (520, 576, 800)
            data = raw_df.iloc[start_row + 1: start_row + 4, start_col: start_col + 6]

            # 4. Set clean headers manually
            data.columns = [
                "Depth (mm)", "Layer Thickness (mm)", "Ave.E-Moduli (MPa)",
                "E-Moduli Range (MPa)", "CBR (%)", "UCS (kPa)"
            ]

            # 5. Add identifying info from the top of the sheet (Project/Site/Distance)
            # These are usually a few rows above the table
            data['Distance'] = str(raw_df.iloc[start_row - 4, start_col + 1])  # Cell next to 'Distance:'
            data['Source_File'] = os.path.basename(f)

            df_list.append(data)
            print(f"✅ Captured Table 1 from: {os.path.basename(f)}")
        else:
            print(f"⚠️ Header not found in: {os.path.basename(f)}")

    except Exception as e:
        print(f"❌ Error in {os.path.basename(f)}: {e}")

# 6. Merge and Save
if df_list:
    final_df = pd.concat(df_list, ignore_index=True)

    # Final cleanup: ensure numbers are actually numbers
    cols_to_fix = ["Depth (mm)", "Layer Thickness (mm)", "Ave.E-Moduli (MPa)", "CBR (%)", "UCS (kPa)"]
    final_df[cols_to_fix] = final_df[cols_to_fix].apply(pd.to_numeric, errors='coerce')

    output_path = "/Users/jayveemacaraeg/Projects/DCPs/table_1_consolidated.csv"
    final_df.to_csv(output_path, index=False)

    print("\n" + "=" * 40)
    print(f"DONE! Data from {len(df_list)} files merged.")
    print(f"Saved to: {output_path}")
    print("=" * 40)