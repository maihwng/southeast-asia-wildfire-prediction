# 🔥 Southeast Asia Wildfire Prediction

Dự án xây dựng hệ thống **phân tích dữ liệu và dự báo mức độ cháy rừng bằng Machine Learning** tại khu vực Đông Nam Á dựa trên dữ liệu viễn thám, khí tượng và môi trường.

Hệ thống thực hiện dự báo **4 mức độ cháy rừng**:

| Label | Mức độ |
|---|---|
| 0 | Không cháy |
| 1 | Cháy thấp |
| 2 | Cháy trung bình |
| 3 | Cháy cao |

Dữ liệu được thu thập trong giai đoạn **2020 - 2024** tại **11 quốc gia Đông Nam Á**.

Dự án hướng tới giải quyết bài toán cảnh báo nguy cơ cháy rừng trong bối cảnh:

- Biến đổi khí hậu.
- Hiện tượng El Niño.
- Nhiệt độ tăng cao.
- Các đợt hạn hán kéo dài tại khu vực Đông Nam Á.

---

# 📌 Giới thiệu đề tài

Cháy rừng là một trong những vấn đề môi trường nghiêm trọng, gây ảnh hưởng lớn đến hệ sinh thái, kinh tế và đời sống con người.

Dự án tập trung xây dựng một quy trình phân tích dữ liệu chuyên sâu và huấn luyện mô hình học máy nhằm dự báo chính xác mức độ cháy rừng dựa trên các yếu tố:

- Dữ liệu điểm cháy từ vệ tinh.
- Điều kiện khí tượng.
- Trạng thái thảm thực vật.
- Các đặc trưng thời gian và không gian.

Mục tiêu của hệ thống:

- Phân loại nguy cơ cháy rừng thành 4 cấp độ.
- Khai thác mối quan hệ giữa các yếu tố môi trường và hiện tượng cháy.
- Hỗ trợ cảnh báo sớm nguy cơ cháy rừng.

---

# 🛠 Công nghệ và thư viện sử dụng

## Ngôn ngữ lập trình

- Python

---

## Xử lý dữ liệu

- Pandas
- NumPy

---

## Trực quan hóa dữ liệu

- Matplotlib
- Seaborn

---

## Machine Learning & Data Preprocessing

- Scikit-learn
- XGBoost
- Imbalanced-learn (SMOTE)

---

## Triển khai hệ thống

- Streamlit / Flask
- Pickle (lưu trữ mô hình)

---

# 📊 Nguồn dữ liệu (Multi-source Data)

Hệ thống tích hợp dữ liệu từ ba nguồn viễn thám và khí tượng mở có độ tin cậy cao.

---

# 🔥 NASA FIRMS

Nguồn dữ liệu phát hiện điểm cháy từ vệ tinh.

Cung cấp:

- Fire Point.
- Fire Radiative Power (FRP).
- Nhiệt độ bức xạ.
- Thông tin phát hiện cháy.

Các đặc trưng này phản ánh mức độ và cường độ của các điểm cháy thực tế.

---

# 🌦 ERA5-Land (ECMWF)

Dữ liệu tái phân tích khí tượng bề mặt.

Bao gồm:

- Nhiệt độ (`temp_c`).
- Lượng mưa (`precip_mm`).
- Độ ẩm tương đối.
- Các biến khí tượng môi trường khác.

Các yếu tố này đóng vai trò quan trọng trong việc đánh giá điều kiện hình thành cháy rừng.

---

# 🌱 MODIS

Dữ liệu vệ tinh cung cấp chỉ số thực vật:

- NDVI (Normalized Difference Vegetation Index).

NDVI phản ánh:

- Sức khỏe thảm thực vật.
- Mức độ khô hạn.
- Khả năng dễ cháy của khu vực.

---

# 🏗 Quy trình xử lý dữ liệu (Data Processing Pipeline)

Hệ thống xây dựng pipeline tiền xử lý dữ liệu nhiều bước nhằm đảm bảo chất lượng dữ liệu đầu vào cho mô hình Machine Learning.

---

# 1. Data Integration

Dữ liệu được tích hợp từ nhiều nguồn:

```
NASA FIRMS
      +
ERA5-Land
      +
MODIS
```

Các bước thực hiện:

- Quét dữ liệu đệ quy từ nhiều thư mục.
- Gộp dữ liệu từ 11 quốc gia Đông Nam Á.
- Đồng bộ dữ liệu theo:

Không gian:

```
Country Level
```

Thời gian:

```
Daily Time Series
```

---

# 2. Data Cleaning & Standardization

## Các bước làm sạch dữ liệu:

 Xử lý định dạng thời gian
Chuẩn hóa dữ liệu
# 3. Missing Data Handling

Fire Features
Environmental Features
# 4. Outlier Handling

Xử lý giá trị ngoại lai bằng:

- IQR Method.
- Capping Technique.

Áp dụng cho:

- Các biến khí tượng.
- Các biến môi trường.

Tuy nhiên:

- Giữ lại các tín hiệu cháy cực đoan.
- Giúp mô hình học được các vụ cháy lớn.

---

# 5. Feature Engineering

Fire Level Classification
NDVI Classification
Label Encoding
Temporal Feature Extraction
Feature Scaling
Min-Max Scaling
Standardization (Z-score)

# 6. Dimensionality Reduction

Áp dụng:

```
PCA
(Principal Component Analysis)
```

Mục tiêu:

- Giảm số chiều dữ liệu.
- Loại bỏ nhiễu.
- Nén các kênh nhiệt độ vệ tinh có độ tương quan cao.
- Tăng tốc độ tính toán.

---

# 7. Data Balancing

Dữ liệu cháy thường có sự mất cân bằng giữa:

- Ngày không cháy.
- Ngày có cháy.

Giải pháp:

Sử dụng kỹ thuật:

```
SMOTE
(Synthetic Minority Oversampling Technique)
```

Tạo mẫu giả lập cho các lớp thiểu số.

Sau cân bằng:

```
15,230 samples / class
```

giúp mô hình học tốt hơn trên toàn bộ các mức độ cháy.

---

# 🤖 Machine Learning Model

Mô hình chính được sử dụng:

```
XGBoost Classifier
```

Lý do lựa chọn:

- Hiệu quả cao với dữ liệu dạng bảng.
- Xử lý tốt quan hệ phi tuyến.
- Phù hợp với dữ liệu khí tượng và môi trường.
- Hoạt động tốt trên bài toán phân loại nhiều lớp.

---

# 📈 Kết quả huấn luyện

Mô hình XGBoost đạt hiệu suất:

| Metric | Result |
|---|---:|
| Accuracy | 93.05% |
| F1-score (Class 3 - High Fire) | 0.92 |

---

# 🔎 Đánh giá mô hình

Mô hình đạt khả năng nhận diện tốt:

## Class 0 - Không cháy

- Phân biệt tốt các trường hợp không có nguy cơ cháy.

## Class 3 - Cháy cao

- Nhận diện hiệu quả các vụ cháy nghiêm trọng.
- Nhờ các đặc trưng vật lý có sự khác biệt rõ ràng.

---

