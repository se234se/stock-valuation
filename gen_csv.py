import pandas as pd

# 读取原始数据
df = pd.read_excel('downloads/19f3ac99-9152-81e2-8000-0000a8dd94a3_list_20260707.xlsx', header=3)

# 去掉空行和来源行
df = df[df['CL1'].notna() & (df['CL1'] != 'Source: Capital IQ')].copy()

# 排除的列索引 (A=0, B=1, ...)
exclude_cols = [9, 11, 13, 14, 15, 20, 21, 26, 27, 28, 29, 33, 34, 35, 40, 41, 42, 47, 48, 49, 50]
keep_cols = [i for i in range(len(df.columns)) if i not in exclude_cols and i != 0]

# 提取保留列
new_df = df.iloc[:, keep_cols].copy()

# 重命名列名
rename_map = {
    'CL1': '分类',
    'CL2': '子分类',
    'Ticker': '代码',
    'Name': '名称',
    'TC': '货币',
    'Price': '股价',
    "'25 chg": '25涨幅',
    'YTD': 'YTD',
    'USD\n(bn)': '市值USD',
    'USD\n(bn).1': 'TEV_USD',
    'CY25': 'PE_25',
    'CY26': 'PE_26',
    'CY27': 'PE_27',
    'CY28': 'PE_28',
    'CY25.1': 'EV_25',
    'CY26.1': 'EV_26',
    'CY27.1': 'EV_27',
    'CY28.1': 'EV_28',
    'CY26.2': 'RevYoY_26',
    'CY27.2': 'RevYoY_27',
    'CY28.2': 'RevYoY_28',
    'CY25.3': 'EBITDA_Margin_25',
    'CY26.3': 'EBITDA_Margin_26',
    'CY27.3': 'EBITDA_Margin_27',
    'CY28.3': 'EBITDA_Margin_28',
    'CY25.4': 'NP_Margin_25',
    'CY26.4': 'NP_Margin_26',
    'CY27.4': 'NP_Margin_27',
    'CY28.4': 'NP_Margin_28',
}
new_df = new_df.rename(columns=rename_map)

# 保存CSV
new_df.to_csv('stock-valuation/data.csv', index=False, encoding='utf-8-sig')

print('CSV saved. Rows:', len(new_df))
print('Columns:', new_df.columns.tolist())
