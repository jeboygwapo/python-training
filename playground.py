import pandas as pd
import glob
import os

path = "/Users/jayveemacaraeg/Projects/DCPs/*.xls"
all_files = glob.glob(path)

df_list = []

print(f"Scanning {len(all_files)} files...")

def get_value_next_to(df, label):
    """Scans the dataframe for a label and returns the value to its immediate right."""
    for r in range(len(df)):
        for c in range(len(df.columns)):
            if label in str(df.iloc[r, c]):
                return df.iloc[r, c + 1]
    return None

for f in all_files:
    try:
        # 1. Read sheet
        raw_df = pd.read_excel(f, engine='xlrd', sheet_name=1, header=None)

        # 2. Find the Table Anchor
        start_row, start_col = None, None
        for r in range(len(raw_df)):
            for c in range(len(raw_df.columns)):
                if "Depth (mm)" in str(raw_df.iloc[r, c]):
                    start_row, start_col = r, c
                    break
            if start_row is not None: break

        if start_row is not None:
            # 3. Extract the 3 rows of data
            data = raw_df.iloc[start_row + 1: start_row + 4, start_col: start_col + 6].copy()
            data.columns = [
                "Depth (mm)", "Layer Thickness (mm)", "Ave.E-Moduli (MPa)",
                "E-Moduli Range (MPa)", "CBR (%)", "UCS (kPa)"
            ]

            # 4. Extract Top Header Metadata
            # This looks for the labels anywhere in the sheet and grabs the neighbor cell
            data['Project']      = get_value_next_to(raw_df, "Project:")
            data['Site']         = get_value_next_to(raw_df, "Site:")
            data['Distance']     = get_value_next_to(raw_df, "Distance:")
            data['Project_Date'] = get_value_next_to(raw_df, "Project Date:")
            data['Location']     = get_value_next_to(raw_df, "Location:")
            data['Position']     = get_value_next_to(raw_df, "Position:")
            data['Source_File']  = os.path.basename(f)

            df_list.append(data)
            print(f"✅ Captured full data from: {os.path.basename(f)}")
        else:
            print(f"⚠️ Table not found in: {os.path.basename(f)}")

    except Exception as e:
        print(f"❌ Error in {os.path.basename(f)}: {e}")

# 5. Merge and Save
if df_list:
    final_df = pd.concat(df_list, ignore_index=True)

    # Convert numeric columns
    cols_to_fix = ["Depth (mm)", "Layer Thickness (mm)", "Ave.E-Moduli (MPa)", "CBR (%)", "UCS (kPa)"]
    final_df[cols_to_fix] = final_df[cols_to_fix].apply(pd.to_numeric, errors='coerce')

    # Reorder columns so Metadata comes first (optional but cleaner)
    meta_cols = ['Project', 'Site', 'Distance', 'Project_Date', 'Location', 'Position', 'Source_File']
    table_cols = [c for c in final_df.columns if c not in meta_cols]
    final_df = final_df[meta_cols + table_cols]

    output_path = "/Users/jayveemacaraeg/Projects/DCPs/table_1_consolidated.csv"
    final_df.to_csv(output_path, index=False)

    print("\n" + "=" * 40)
    print(f"DONE! Merged {len(df_list)} files.")
    print(f"Saved to: {output_path}")
    print("=" * 40)