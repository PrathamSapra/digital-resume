from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Pratham Sapra | Digital CV"
PAGE_ICON = ":wave:"
NAME = "PRATHAM SAPRA"
DESCRIPTION = """
Cloud Architecture & Administration Student | Microsoft Certified Professional | Passionate Digital Marketing Executive | Web Designer | AI Enthusiast
"""
EMAIL = "prathamssapra@gmail.com"
SOCIAL_MEDIA = {
    "Instagram": "https://www.instagram.com/prathamsapra16?igsh=MW14MDB6Zm1pdHRpNQ==",
    "Twitter": "https://x.com/Sapruuuu?t=qQV06p9LiPnIAGGpUeoWNg&s=08",
    "LinkedIn": "https://www.linkedin.com/in/prathamsapra/",
    "GitHub": "https://github.com/PrathamSapra",

}

PROJECTS = {
    "**🏆 Azure Infrastructure Deployment Utilizing Active Directory Domain Services**": "https://seneca-my.sharepoint.com/:v:/g/personal/pssapra_myseneca_ca/EWnEustBBjZAtyMchRu4iBgBI8KtLZxpmMnqee1vSKyYVw?e=0qzvsw&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D",
    "**🏆 Azure Load Balancing and Private DNS Integration**": "https://seneca-my.sharepoint.com/:v:/g/personal/pssapra_myseneca_ca/Eau1iGi6sMlOiEX0tayinKYBHFx3MfmC345T_syNmu9JXw?e=4BgbDv&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D",
    "**🏆 AWS Auto Scaling Application**": "https://seneca-my.sharepoint.com/:v:/g/personal/pssapra_myseneca_ca/EapX7K66EkVOioIVgL6O8sUBDN7uULUM3r4Yj5g9Vtfryw?e=pLmw7i&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D",
    "**🏆 AWS Load Balancing Configuration**": "https://seneca-my.sharepoint.com/:v:/g/personal/pssapra_myseneca_ca/EVl_FtY9Z7tAnJKjfrotZPcB4pryPW4NvENf_tGLcO-Z1Q?e=U7jNQY&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D",
    "**🏆 AWS Configuration Management Automation Utilizing Ansible**": "https://seneca-my.sharepoint.com/:v:/g/personal/pssapra_myseneca_ca/EQBA1X-GluJNoxSW1Opo3TwBP_ksPml6MrkHXkX2Gup4hw?e=4eJFmL&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D",
}



st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)



# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=330)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📩", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ♠️ Skilled Web Developer & Marketing Executive with expertise in Python, MySQL, HTML, CSS, 
     Azure, AWS, and cloud computing technologies.
- ♠️ 2 Years of proven track record in client relationship management, delivering impactful digital 
     strategies, and achieving significant growth in online sales revenue and brand visibility.
- ♠️ Proficient in digital marketing, including social media campaigns, email optimization, and 
     analytics using tools
- ♠️ Experienced in deploying secure and scalable cloud architectures using Azure and AWS, 
     including infrastructure setup, load balancing, and application auto-scaling.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- ☁️️ Cloud Platforms: Azure & AWS
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visualization : PowerBi| MS Excel 
- 📚 Software and Tools Proficiency: Adobe Photoshop |  MS Word | MS Excel | MS PowerPoint | Canva | Power BI | Google Ads | Meta Ads | LinkedIn Ads


"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")



# --- JOB 1
st.write("📌", "**Web Developer & Marketing Executive | Vizcom Solutions**")
st.write("06/2022 - 12/2023")
st.write(
    """
- ► Managed client relationships, achieving a 99% satisfaction rate and driving repeat business opportunities.
- ► Delivered persuasive presentations on digital strategies, increasing client engagement by 30%.
- ► Developed data-driven sales strategies that led to a 20% increase in online sales revenue.
- ► Orchestrated targeted social media campaigns, increasing brand visibility by 25%.
- ► Optimized email marketing campaigns, improving open rates by 15%.
- ► Contributed to maintaining a 90% brand consistency score across digital platforms.
"""
)



# --- JOB 2
st.write('\n')
st.write("📌", "**Web Designer & Marketing Executive Intern | SK Edu Services**")
st.write("04/2021 - 08/2021")
st.write(
    """
- ► Implemented SEO strategies, enhancing online visibility and search rankings by 30%.
- ► Collaborated on visually captivating marketing materials, ensuring brand consistency.
- ► Utilized Google Analytics and SEMrush to optimize digital marketing efforts.
- ► Enhanced email marketing effectiveness through strategic segmentation.
- ► Supported creative teams in producing engaging content for digital campaigns.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# --- education ---
st.write('\n')
st.subheader("Education")
st.write("---")

# --- ED1
st.write("🔖", "**Cloud Architecture & Administration | Seneca Polytechnic**")
st.write("01/2024 - 12/2024")


# --- ED2
st.write('\n')
st.write("🔖", "**Bachelors of Science in Information Technology | Narsee Monjee College**")
st.write("2020 - 2023")

# --- ED3
st.write('\n')
st.write("🔖", "**AI-900: Microsoft Azure AI Fundamentals | Score: 921/1000**")
st.write("Febuary 2023")