import streamlit as st

# Cấu hình tiêu đề trang
st.set_page_config(page_title="About Me", page_icon="📋")

# Tiêu đề trang
st.title("About Me")

# Thông tin cá nhân
st.header("🧑‍💻 Personal Information")
st.write("""
- **Name:** Hoàng Tiến Anh  
- **Email:** [hoangtienanh2k3@gmail.com](mailto:hoangtienanh2k3@gmail.com)
- **Phone:** 0386186103  
- **Facebook:** [Hoàng Tiến Anh](https://www.facebook.com/hoang.tien.anh.2003)
""")

# Link GitHub
st.header("🔗 GitHub & Repository")
st.write("""
- **GitHub Profile:** [GitHub](https://github.com/HTAnh2003)  
- **Project Repository:** [DataMate Repo](https://github.com/HTAnh2003/DataMate)
""")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
