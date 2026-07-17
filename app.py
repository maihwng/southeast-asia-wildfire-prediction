import pandas as pd

print("BẮT ĐẦU TÍCH HỢP DỮ LIỆU ĐA NGUỒN")

# Đọc 3 file nguồn (Ép thẳng cột date thành chuỗi Text để bảo tồn sự nát)
df_era5 = pd.read_csv(r'C:\BTL_DataPre\Dataset\ERA5_Data_Wildfire_SEA.csv')
# Chặt đuôi giờ phút của ERA5 (nếu có) để nó thành dạng YYYY-MM-DD
df_era5['date'] = df_era5['date'].astype(str).str.split(' ').str[0]

df_modis = pd.read_csv(r'C:\BTL_DataPre\Dataset\MODIS_NDVI_SEA.csv')
df_modis['date'] = df_modis['date'].astype(str)

df_firms = pd.read_csv(r'C:\BTL_DataPre\NASA_FIRMS_SEA_Daily.csv')
df_firms['date'] = df_firms['date'].astype(str)

# TIẾN HÀNH GỘP THÔ (OUTER JOIN)
print("Đang gộp để bộc lộ sự bất đồng bộ khóa (Key Mismatch)...")
df_master = pd.merge(df_era5, df_modis, on=['ADM0_NAME', 'date'], how='outer')
df_master = pd.merge(df_master, df_firms, on=['ADM0_NAME', 'date'], how='outer')

# Sắp xếp lại để dễ nhìn thấy lỗi
df_master = df_master.sort_values(by=['ADM0_NAME', 'date']).reset_index(drop=True)

# Xuất file thô nguyên thủy
df_master.to_csv('Wildfire_SEA.csv', index=False)
