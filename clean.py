import sys
import pandas as pd
def clean_data(input1, input2, output):
    df_contact = pd.read_csv(input1)
    df_other = pd.read_csv(input2)
    df_merged = pd.merge(df_contact, df_other, left_on='respondent_id', right_on='id')
    df_merged.drop(columns=['id'], inplace=True)
    df_merged.dropna(inplace=True)
    df_merged = df_merged[~df_merged['job'].str.contains('insurance', case=False, na=False)]
    df_merged.to_csv(output, index=False)
    print(f"Data cleaned and saved to {output}")
if __name__ == "__main__":
        if len(sys.argv) != 4:
            print("Usage: python clean.py <input1> <input2> <output>")
            sys.exit(1)

        input1, input2, output = sys.argv[1], sys.argv[2], sys.argv[3]
        clean_data(input1, input2, output)
