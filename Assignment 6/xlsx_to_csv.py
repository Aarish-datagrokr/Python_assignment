import pandas as pd
import sys



excel_filename = sys.argv[1]
xl = pd.ExcelFile(excel_filename)


for sheet in xl.sheet_names:
    print(excel_filename)
    print('- ' + sheet + '.csv')
    df = pd.DataFrame()
    df_tmp = xl.parse(sheet)
    df = df.append(df_tmp, ignore_index=True,sort=False)
    df.to_csv(sheet.replace(' ','_')+'.csv', index=False)