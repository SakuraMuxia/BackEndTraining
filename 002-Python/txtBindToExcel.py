"""
功能描述：
1. 读取 txt 文件中的 ICCID 列表。
2. 读取 Excel 文件，并确保 ICCID 列为字符串格式，同时去除空格和双引号。
3. 在 Excel 文件中标注哪些 ICCID 存在于 txt 文件中，添加 'Found' 列。
4. 打印出 txt 文件中但未在 Excel 文件中找到的 ICCID。
5. 生成一个新的 Excel 文件，包含原始数据和标注信息。
"""

import pandas as pd

# 读取txt文件，每行一个ICCID
txt_file = 'D:/var/data/cards.txt'  # txt文件路径
txt_data = set(line.strip() for line in open(txt_file, encoding='utf-8'))

# 读取Excel文件
excel_file = 'D:/var/data/data.xlsx'  # Excel文件路径
sheet_name = 'Sheet1'  # 需要处理的Sheet
column_name = 'ICCID'  # 需要匹配的列名

# 读取Excel数据并确保ICCID列为字符串类型
df = pd.read_excel(excel_file, sheet_name=sheet_name, dtype=str, engine='openpyxl')

# 处理ICCID列，去除空格和双引号
df[column_name] = df[column_name].astype(str).str.strip().str.replace('"', '')

# 在Excel文件中标注是否在txt文件中
df['Found'] = df[column_name].isin(txt_data)

# 找出txt文件中但不在Excel文件中的ICCID
not_found = txt_data - set(df[column_name])
print("以下ICCID未在Excel中找到:")
for iccid in not_found:
    print(iccid)

# 保存新的Excel文件
output_file = 'D:/var/data/output2.xlsx'
df.to_excel(output_file, index=False, engine='openpyxl')

print(f'处理完成，结果已保存至 {output_file}')


