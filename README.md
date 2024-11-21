# Trợ Lý Phân Tích Dữ Liệu Đa Năng (DataMate)

**Giới Thiệu**  
Chào mừng bạn đến với hướng dẫn cá nhân của mình! Trong dự án này, mình sẽ xây dựng **DataMate** - một công cụ phân tích dữ liệu mạnh mẽ và tiện lợi sử dụng các mô hình ngôn ngữ lớn (LLMs). Với **DataMate**, bạn có thể dễ dàng tải lên dữ liệu, đặt câu hỏi, khám phá dữ liệu và nhận các phân tích trực quan thông qua giao diện đàm thoại. Dự án này sử dụng Python cùng các công cụ Langchain, Streamlit, PyGWalker và OpenAI (Gemini) API.  

**Mục Tiêu Dự Án**  
Mục tiêu của mình là xây dựng một công cụ hỗ trợ phân tích dữ liệu dành cho cá nhân hoặc nhóm nhỏ, giúp tiết kiệm thời gian và tối ưu hóa quy trình khám phá dữ liệu.  

---

## **Nội Dung Dự Án**  

1. **Tổng Quan về DataMate**  
   - **DataMate** là công cụ hỗ trợ phân tích dữ liệu với các tính năng chính:  
     - **Tải lên tệp CSV:** Dễ dàng tải lên dữ liệu qua giao diện đơn giản.  
     - **Trả lời câu hỏi:** Phân tích dữ liệu và đưa ra phản hồi thông minh thông qua giao diện trò chuyện.  
     - **Trực quan hóa dữ liệu:** Tạo biểu đồ và hình ảnh minh họa dựa trên dữ liệu và các câu hỏi.  
     - **Khám phá tương tác:** Tùy chỉnh và khám phá dữ liệu với các công cụ trực quan hóa tương tác.  

2. **Công Nghệ Sử Dụng**  
   - **Python 3.9+**: Ngôn ngữ chính cho dự án.  
   - **Langchain:** Khung hỗ trợ xây dựng ứng dụng tương tác dựa trên mô hình ngôn ngữ lớn.  
   - **Streamlit:** Khung phát triển giao diện web dễ sử dụng cho khoa học dữ liệu.  
   - **PyGWalker:** Công cụ mạnh mẽ để tạo trực quan hóa dữ liệu tương tác.  
   - **OpenAI API:** (Tùy chọn) Tận dụng các mô hình ngôn ngữ mạnh mẽ như GPT để xử lý câu hỏi.  

---

## **Hướng Dẫn Chạy Dự Án**

### 1. **Cài Đặt Môi Trường**
- Tạo môi trường ảo Python:
  ```bash
  python -m venv venv
  source venv/bin/activate  # Trên macOS/Linux
  venv\Scripts\activate     # Trên Windows
  ```
- Cài đặt các gói cần thiết:
  ```bash
  pip install -r requirements.txt
  ```

### 2. **Chạy Ứng Dụng**
- Chạy ứng dụng Streamlit:
  ```bash
  streamlit run 1_📊_Chat_With_Your_Data.py
  ```
### Giao diện ứng dụng

![Giao diện ứng dụng](./images/page1.jpg)
---

## **Các Bước Thực Hiện**  

1. **Khởi Tạo Dự Án**  
   - Tạo cấu trúc thư mục và môi trường lập trình.  
   - Cài đặt các gói Python cần thiết, bao gồm Streamlit, Langchain, PyGWalker, và OpenAI API.  

2. **Phát Triển Công Cụ Chat Với Dữ Liệu**  
   - Tạo giao diện web bằng Streamlit để người dùng có thể tải lên tệp CSV.  
   - Tích hợp Langchain và mô hình GPT để hỗ trợ việc trả lời câu hỏi về dữ liệu.  
   - Tối ưu hóa giao diện để dễ sử dụng và thân thiện với mọi đối tượng.  

3. **Tích Hợp Công Cụ Trực Quan Hóa Dữ Liệu**  
   - Sử dụng PyGWalker để tạo biểu đồ tự động dựa trên dữ liệu.  
   - Tích hợp các tính năng tương tác để người dùng có thể điều chỉnh biểu đồ và khám phá dữ liệu theo cách riêng.  

---

**Tổng Kết**  

**DataMate** là một dự án cá nhân với mục tiêu đơn giản hóa quá trình phân tích dữ liệu. Nhờ các mô hình ngôn ngữ lớn và công cụ trực quan hóa mạnh mẽ như PyGWalker, mình có thể tạo ra một công cụ giúp khám phá và làm việc với dữ liệu một cách dễ dàng.  

Nếu bạn muốn thử xây dựng một công cụ tương tự, mình tin rằng dự án này sẽ là một khởi đầu tuyệt vời!