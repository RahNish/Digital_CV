import streamlit as st
from PIL import Image
import base64

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


# Function to convert image to Base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

#####################
# Header Section
st.markdown("""
<style>
.profile-pic {
    display: block;
    margin-left: auto;
    margin-right: auto;
    border-radius: 50%;
    width: 250px;
    height: 250px;
    object-fit: cover;
    object-position: top;
    border: 4px solid #16A2CB;
}
</style>
""", unsafe_allow_html=True)

# Add your profile picture in a circular format
image_path = 'dp.png'  # Replace with your image file path
image_base64 = image_to_base64(image_path)
st.markdown(f'<img src="data:image/png;base64,{image_base64}" class="profile-pic">', unsafe_allow_html=True)



#####################
# Header 
st.write('''
# Dr. Ashish Srivastava, Ph.D.

''')

st.markdown("""

<div style="display: flex; justify-content: center;">
    <a href="https://www.linkedin.com/in/dr-ashish-srivastava-769a70146?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BUeoEKhcoTuaScJsdrqNBxQ%3D%3D" target="_blank" style="margin: 0 10px; font-size: 24px; color: #0077b5;">
        <i class="fab fa-linkedin"></i> LinkedIn
    </a>
    <a href="https://scholar.google.co.in/citations?user=Md9Z1PMAAAAJ" target="_blank" style="margin: 0 10px; font-size: 24px; color: #4285F4;">
        <i class="fab fa-google-scholar"></i> Google Scholar
    </a>
    <a href="https://www.scopus.com/authid/detail.uri?authorId=57211776060" target="_blank" style="margin: 0 10px; font-size: 24px; color: #FF6A00;">
        <i class="fab fa-scoop"></i> Scopus
    </a>
</div>
""", unsafe_allow_html=True)

# st.markdown("[Download Resume](https://drive.google.com/file/d/1le0wrIDUz_MSw1YUbAFGQFbsXmnrUAGh/view?usp=share_link)", unsafe_allow_html=True)

st.markdown("""
<div style="display: flex; justify-content: center; margin-top: 20px;">
    <a href="https://drive.google.com/file/d/1le0wrIDUz_MSw1YUbAFGQFbsXmnrUAGh/view?usp=share_link" 
       target="_blank" 
       style="background-color: #16A2CB; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none; font-size: 16px;">
        Download Resume
    </a>
</div>
""", unsafe_allow_html=True)

# image = Image.open('dp.png')
# image = image.rotate(90, expand=True)
# st.image(image, width=200)




st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
I am Dr. Ashish Srivastava, and I completed my Ph.D. from IIT-BHU, Varanasi, in 2019. My Ph.D. research
focused on Barkhausen noise signal processing generated from ground steel to assess its surface integrity.
My current research work focuses on the application of Artificial Intelligence (AI) and Machine Learning (ML)
techniques for material discovery and characterization. I leverage ML algorithms to predict material
behaviour, assess surface damage, and classify microstructural changes in steels during machining, thereby
enhancing process eﬀiciency and sustainability.
Additionally, I am working on a government-funded project by the Government of Karnataka, where I am
utilizing deep learning techniques to segment diﬀerent layers in the grinding of steel.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

# st.markdown("""
# <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
#   <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Ashish Srivastava</a>
#   <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
#     <span class="navbar-toggler-icon"></span>
#   </button>
#   <div class="collapse navbar-collapse" id="navbarNav">
#     <ul class="navbar-nav">
#       <li class="nav-item active">
#         <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
#       </li>
#       <li class="nav-item">
#         <a class="nav-link" href="#education">Education</a>
#       </li>
#       <li class="nav-item">
#         <a class="nav-link" href="#work-experience">Work Experience</a>
#       </li>
#       <li class="nav-item">
#         <a class="nav-link" href="#projects">Projects</a>
#       </li>
#       <li class="nav-item">
#         <a class="nav-link" href="#publications">Publications</a>
#       </li>
#       <li class="nav-item">
#         <a class="nav-link" href="#phd-students">PhD Students</a>
#       </li>
#     </ul>
#   </div>
# </nav>
# """, unsafe_allow_html=True)


st.markdown("""
<style>
/* Center the navbar content */
.navbar {
  justify-content: center !important;
}
.navbar-nav {
  display: flex;
  justify-content: center;
  width: 100%;
}
.nav-item {
  margin: 0 10px; /* Add spacing between items */
}
</style>

<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand"  target="_blank">Ashish Srivastava</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#publications">Publications</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#phd-students">PhD Students</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#workshops">Workshops</a>
    </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)





# st.markdown("""
# <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
#   <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Ashish Srivastava</a>
#   <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
#     <span class="navbar-toggler-icon"></span>
#   </button>
#   <div class="collapse navbar-collapse" id="navbarNav">
#     <ul class="navbar-nav">
#       <li class="nav-item active">
#         <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
#       </li>
#       <li class="nav-item">
#         <a class="nav-link" href="#education">Education</a>
#       </li>
#       <li class="nav-item">
#         <a class="nav-link" href="#work-experience">Work Experience</a>
#       </li>
#       <li class="nav-item">
#         <a class="nav-link" href="#projects">Projects</a>
#       </li>
#       <li class="nav-item">
#         <a class="nav-link" href="#social-media">Social Media</a>
#       </li>
#     </ul>
#   </div>
# </nav>
# """, unsafe_allow_html=True)



#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)


def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
# def txt4(a, b, c):
#   col1, col2, col3 = st.columns([1.5,2,2])
#   with col1:
#     st.markdown(f'`{a}`')
#   with col2:
#     st.markdown(b)
#   with col3:
#     st.markdown(c)



#####################
st.markdown('''
## Education
''')

txt('**Doctor of Philosophy** (Mechanical Engg.), *IIT-BHU*, Varanasi',
'2013-2019')


st.markdown('''
- Research thesis entitled <span style="font-size:20px; color:yellow; background-color:black;">`Study on grindability of surface modified steel`</span>.
''', unsafe_allow_html=True)

txt('**Master of Technology (M.Tech)** (Production Engg.), *Motilal Nehru National Institute of Technology*, Allahabad',
'2010-2012')
st.markdown('''      
- Research thesis entitled <span style="font-size:20px; color:yellow; background-color:black;">`Parameter optimization of EDDG Process using Artificial Neural Network and Genetic Algorithm`</span>.
''', unsafe_allow_html=True)


txt('**Bachelor of Technology (B.Tech)** (Mechanical Engg.), *U.I.E.T (CSJM University)*, Kanpur',
'2006-2010')



txt('**Post Graduate Diploma in AI and ML** (AI/ML.), *Central University of Hyderabad*, Hyderabad',
'2021-2022')



txt('**Diploma in Data Science** (Data Science), *IIT-Madras*, Chennai',
'2022-2023')


txt('**Diploma in Programming** (Programming), *IIT-Madras*, Chennai',
'2023-2024')


#####################
st.markdown('''
## Work Experience
''')

# txt('**Head, Center of Data Mining and Biomedical Informatics**, Faculty of Medical Technology, Mahidol University, Thailand',
# '2011-2021')
# st.markdown('''
# - Managing a Center of `10` professors, researchers and students to ensure KPIs are strategically achieved namely to publish at least `20+` research publications annually. 
# - Actively took part in the talent hiring process as well as help employees to plan and develop their career path.
# - Set budget and handle procurement in order to facilitate education and research activities. Secured `> 10 million THB` budget.
# - Set and reflect on OKR on an annual basis to ensure productivity strategically matches the organization's direction.
# ''')

txt('**Assistant Professor**, United College of Engineering and Management, Prayagraj',
'2012-2013')
txt('**Assistant Professor**, Presidency University, Bangalore, Karnataka',
'2019-2022')
txt('**Assistant Professor (Research)**, Presidency University, Bangalore, Karnataka',
'2022-present')

#####################
st.markdown('''
## Skills
''')
txt3('Core skills :', '`Application of Artificial Intelligence in Material discovery`,`X-Ray diﬀraction`,`Scanning electron microscopy`,`Non-destructive characterisation`')
txt3('Programming Languages', '`Python`, `Java`, `SQL`, `JavaScript`, `Bash`, `HTML/CSS`')
txt3('Technologies/Framework',  '`Pandas`, `Numpy`, `Sklearn`, `Excel`, `Linux`, `Flask`, `REST`, `VUE`')




#####################
# Add a header for the table
st.markdown('''
## Projects
''')
col1, col2, col3, col4, col5 = st.columns([2, 2, 1.5, 1.5, 1.5])

# Display header row
with col1:
    st.markdown("**Title**")
with col2:
    st.markdown("**Funding Agency**")
with col3:
    st.markdown("**Amount**")
with col4:
    st.markdown("**Scheme**")
with col5:
    st.markdown("**Status**")

# Function to display project details
def project_details(title, funding_agency, amount, scheme, status):
    col1, col2, col3, col4, col5 = st.columns([2, 2, 1.5, 1.5, 1.5])
    with col1:
        st.markdown(f"`{title}`")
    with col2:
        st.markdown(f"{funding_agency}")
    with col3:
        st.markdown(f"{amount}")
    with col4:
        st.markdown(f"{scheme}")
    with col5:
        st.markdown(f"{status}")

# Add project details below the header
project_details(
    title="Classification of Heat Aﬀected Zone upon Grinding of AISI52100 bearing Steel through Deep Learning-based Semantic Segmentation Technique,",
    funding_agency="VGST",
    amount="₹ 10 Lakhs",
    scheme="ECRA",
    status="Ongoing"
)


#####################

# Add a title for the publications section
st.markdown("## Publications")

# Define a function to display each publication
def display_publication(title, journal, authors, year, doi, rank, impact_factor=None):
    if impact_factor:
        st.markdown(f"""
        - **{title}**  
          _{journal}_  
          {authors}, {year},  
          [DOI Link]({doi}) {rank}  
          Impact Factor: {impact_factor}  
        """)
    else:
        st.markdown(f"""
        - **{title}**  
          _{journal}_  
          {authors}, {year},  
          [DOI Link]({doi}) {rank}  
        """)

# List of publications
publications = [
    {
        "title": "Assessing the Temperature-Dependent Characteristics of Warm-Rolled EN8 Steel through Magnetic Barkhausen Noise Technique and Predictive Modeling with Voting Regression Technique",
        "journal": "Journal of Materials Engineering and Performance",
        "authors": "Chaudhary, A., Srivastava, A., Nahak, B.",
        "year": "2024",
        "doi": "https://doi.org/10.1007/s11665-024-10089-2",
        "rank": "(Q2)"
    },
    {
        "title": "Magnetic non-destructive evaluation of microstructural and mechanical characteristics of hardened AISI H13 die steel upon sustainable grinding",
        "journal": "Journal of Manufacturing Processes",
        "authors": "Awale, A.S., Srivastava, A., Kumar, A., Yusufzai, M.Z.K., Vashista, M.",
        "year": "2023",
        "doi": "https://doi.org/10.1016/j.jmapro.2023.08.035",
        "rank": "(Q1)",
        "impact_factor": "6.2"
    },
    {
        "title": "Metallurgical Behaviour and Characterization on Polymer Metal with HCHCr Tool by using Friction Stir Welding Adopting L27 Taguchi Technique",
        "journal": "Journal of Mines, Metals & Fuels",
        "authors": "Srivastava, A., Ramesh, C.S. and Ramesh, S.",
        "year": "2023",
        "doi": " https://doi.org/10.18311/jmmf/2023/35046",
        "rank": "(Q4)"
    },
    {
        "title": "Assessing the role of different material properties on Barkhausen Noise Generation from machined steel using Machine Learning Techniques",
        "journal": "International Journal on Interactive Design and Manufacturing",
        "authors": "Srivastava, A., Nahak, B.",
        "year": "2023",
        "doi": "",
        "rank": "(Q2)",
        "impact_factor": "2.2"
    },
    {
        "title": "Microstructural Characterization of SiC reinforced Ti−6Al−4V metal matrix composites fabricated through powder metallurgy route",
        "journal": "Materials Physics and Mechanics",
        "authors": "Srivastava, A., Shaikh, K.A. and Bopanna, S.",
        "year": "2023",
        "doi": "",
        "rank": "(Q4)",
        "impact_factor": "0.75"
    },
    {
        "title": "Wear performance prediction of MWCNT reinforced AZ31 composite using machine learning technique",
        "journal": "Journal of Bio and Tribo-Corrosion",
        "authors": "Sandeep G M, Ashish Srivastava, Satish Babu Bopanna, Samuel Dayanand, Yashwant D.",
        "year": "2023",
        "doi": "https://doi.org/10.1007/s40735-023-00745-w",
        "rank": "(Q1)",
        "impact_factor": "3.31"
    },
    {
        "title": "Characterization of ground steel using non-destructive magnetic Barkhausen noise technique",
        "journal": "Journal of Materials Engineering and Performance",
        "authors": "Srivastava, A., Awale, A.S., Yusufzai, M.Z.K, Vashista, M.",
        "year": "2020",
        "doi": "",
        "rank": "(Q2)",
        "impact_factor": "2.3"
    },
    {
        "title": "Monitoring of thermal damages upon grinding of hardened steel using Barkhausen noise analysis",
        "journal": "Journal of Mechanical Science and Technology",
        "authors": "Srivastava, A., Awale, A.S., Yusufzai, M.Z.K, Vashista,M.",
        "year": "2020",
        "doi": "",
        "rank": "(Q2)",
        "impact_factor": "1.6"
    },
    {
        "title": "Surface integrity assessment upon electric discharge machining of die steel using non-destructive magnetic Barkhausen noise technique",
        "journal": "Transactions of Indian Institute of Metals",
        "authors": "Nahak, B., Srivastava, A., Yusufzai, M.Z.K, Vashista, M.",
        "year": "2020",
        "doi": "",
        "rank": "(Q2)",
        "impact_factor": "1.6"
    },
    {
        "title": "Non-destructive Monitoring of Electro-discharge Machined Die Steel",
        "journal": "Arabian Journal for Science and Engineering",
        "authors": "Nahak, B. and Srivastava, A.",
        "year": "2022",
        "doi": "",
        "rank": "(Q1)",
        "impact_factor": "2.9"
    },
    {
        "title": "Surface integrity characterization of ground-hardened H13 hot die steel using different lubrication environments",
        "journal": "Materials Research Express",
        "authors": "Awale, A., Srivastava, A., Vashista, M. and Yusufzai, M.K.",
        "year": "2018",
        "doi": "",
        "rank": "(Q2)",
        "impact_factor": "2.3"
    },
    {
        "title": "Influence of minimum quantity lubrication on surface integrity of ground hardened H13 hot die steel",
        "journal": "International Journal of Advanced Manufacturing Technology",
        "authors": "Awale, A.S., Srivastava, A., Vashista, M., Yusufzai, M.Z.K.",
        "year": "2018",
        "doi": "",
        "rank": "(Q1)",
        "impact_factor": "3.4"
    },
    {
        "title": "Utilisation of Industrial waste (Fly ash) in synthesis of copper based surface composite through friction stir processing route for wear applications",
        "journal": "Journal of Cleaner Production",
        "authors": "Kumar,H., Prasad,R., Srivastava, A., Yusufzai, M.Z.K., Vashista, M.",
        "year": "2018",
        "doi": "",
        "rank": "(Q1)",
        "impact_factor": "11.1"
    },
    {
        "title": "Barkhausen noise signal analysis of heat treated samples at various magnetizing frequencies",
        "journal": "International Journal of Materials and Product Technology",
        "authors": "Srivastava, A., Kumar,H., Yusufzai, M.Z.K., Vashista, M.",
        "year": "2017",
        "doi": "",
        "rank": "(Q3)",
        "impact_factor": "0.62"
    },
    {
        "title": "On the role of magnetising frequency and magnetic field intensity on hysteresis loop characteristics",
        "journal": "International Journal of Microstructure and Materials Properties",
        "authors": "Srivastava, A., Kumar, H., Yusufzai, M.Z.K. and Vashista, M.",
        "year": "2017",
        "doi": "",
        "rank": "(Q4)"
    },
    {
        "title": "Computer-aided hybrid ANN-GA approach for modelling and optimisation of EDDG process",
        "journal": "International Journal of Abrasive Technology",
        "authors": "Srivastava, A., Dubey, A.K., Shrivastava, P.K.",
        "year": "2012",
        "doi": "",
        "rank": "(Q3)"
    },
]

# Loop through the publications and display them
for pub in publications:
    display_publication(
        title=pub["title"],
        journal=pub["journal"],
        authors=pub["authors"],
        year=pub["year"],
        doi=pub["doi"],
        rank=pub["rank"],
        impact_factor=pub.get("impact_factor", None)
    )


st.markdown('## Conference Publications', unsafe_allow_html=True)

publications = [
    {
        "title": "Microstructural Characterization of Pack Carburized IS-2062 Low Carbon Steel Using Magnetic Barkhausen Noise",
        "journal": "Materials Today Proceedings",
        "authors": "Srivastava, A., Kumar, H., Yusufzai, M.Z.K., Vashista, M.",
        "year": 2017,
        "volume_issue": "16, 2",
        "pages": "439-443",
    },
    {
        "title": "Joining of Nylon Using Friction Stir Welding (FSW) Techniques",
        "journal": "SAE Technical",
        "authors": "Gangaraju, Ashish Srivastava, C.S. Ramesh",
        "year": 2023,
        "doi": "10.4271/2023-01-0994",
        "indexing": "Q3",
        "impact_factor": "0.53",
    },
    {
        "title": "Study on Structural Stability and Thermal Analysis of Intake Manifold Valve through Numerical Analysis",
        "journal": "SAE Technical",
        "authors": "Gangaraju, Ashish Srivastava, C.S. Ramesh",
        "year": 2023,
        "doi": "10.4271/2023-01-0989",
        "indexing": "Q3",
        "impact_factor": "0.53",
    },
    {
        "title": "Microstructural Analysis of Forged Al-11Si-2.5 Cu-0.6 Fe Alloy at Different Processing Conditions",
        "journal": "Materials Today Proceedings",
        "authors": "Sahu, K., Narayane, D., Singh, M.K., Singh, R.B., Srivastava, A.",
        "year": 2021,
        "volume_issue": "47",
        "pages": "6682-6685",
    },
]

# Display the publications
for pub in publications:
    st.markdown(f"""
    **{pub['title']}**  
    _{pub['journal']}_  
    Authors: {pub['authors']}  
    Year: {pub['year']}  
    """, unsafe_allow_html=True)
    
    # Add optional fields if present
    if 'volume_issue' in pub:
        st.markdown(f"Volume/Issue: {pub['volume_issue']}")
    if 'pages' in pub:
        st.markdown(f"Pages: {pub['pages']}")
    if 'doi' in pub:
        st.markdown(f"DOI: [{pub['doi']}](https://doi.org/{pub['doi']})")
    if 'indexing' in pub:
        st.markdown(f"Indexing: {pub['indexing']}")
    if 'impact_factor' in pub:
        st.markdown(f"Impact Factor: {pub['impact_factor']}")
    st.write("---")



# import streamlit as st
# import base64

# # Function to convert image to Base64
# def image_to_base64(image_path):
#     with open(image_path, "rb") as img_file:
#         return base64.b64encode(img_file.read()).decode("utf-8")

# st.markdown('## PhD Students', unsafe_allow_html=True)

# # Styling for the student card
# st.markdown("""
# <style>
# .student-card {
#     display: flex;
#     align-items: center;
#     margin-bottom: 20px;
#     padding: 10px;
#     border: 2px solid #16A2CB;
#     border-radius: 10px;
#     background-color: #f9f9f9;
#     box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
#     width: 100%;
# }
# .student-card img {
#     width: 120px;
#     height: 120px;
#     border-radius: 50%;
#     object-fit: cover;
#     margin-right: 20px;
#     border: 3px solid #16A2CB;
# }
# .student-details {
#     font-size: 16px;
#     color: #333;
#     line-height: 1.6;
# }
# </style>
# """, unsafe_allow_html=True)

# # Add student details
# students = [
#     {
#         "name": "John Doe",
#         "image_path": "gm.png",  # Replace with your image path
#         "phd_title": "Microstructural Analysis of Advanced Alloys",
#         "year_awarded": "2021",
#         "role": "Principal Investigator (PI)"
#     },
#     {
#         "name": "Jane Smith",
#         "image_path": "raju.png",  # Replace with your image path
#         "phd_title": "AI-Driven Material Characterization Techniques",
#         "year_awarded": "2023",
#         "role": "Co-Principal Investigator (Co-PI)"
#     }
# ]

# # Display student information
# for student in students:
#     # Convert student image to Base64 for inline display
#     student_image_base64 = image_to_base64(student["image_path"])
#     st.markdown(f"""
#     <div class="student-card">
#         <img src="data:image/png;base64,{student_image_base64}" alt="Student Image">
#         <div class="student-details">
#             <b>Name:</b> {student['name']}<br>
#             <b>PhD Title:</b> {student['phd_title']}<br>
#             <b>Year Awarded:</b> {student['year_awarded']}<br>
#             <b>Role:</b> {student['role']}
#         </div>
#     </div>
#     """, unsafe_allow_html=True)



import streamlit as st
import base64

# Function to convert image to Base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

st.markdown('## PhD Students', unsafe_allow_html=True)

# Styling for the student card
st.markdown("""
<style>
.student-card {
    display: flex;
    align-items: center;
    justify-content: flex-start; /* Ensures content aligns horizontally */
    margin-bottom: 20px;
    padding: 10px;
    border: 2px solid #16A2CB;
    border-radius: 10px;
    background-color: #f9f9f9;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    width: 100%;
}
.student-card img {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    object-fit: cover;
    margin-right: 80px; /* Space between image and text */
    border: 3px solid #16A2CB;
}
.student-details {
    font-size: 16px;
    color: #333;
    line-height: 1.6;
    text-align: left; /* Align text to the left */
}
</style>
""", unsafe_allow_html=True)

# Add student details
students = [
    {
        "name": "Dr. Sandeep GM",
        "image_path": "gm.png",  # Your uploaded image
        "phd_title": "Preparation and characterization of CNT- reinforced AZ-31 magnesium alloy nanocomposites",
        "year_awarded": "2023",
        "role": "Co-Supervisor"
    },
    {
        "name": "Gangaraju R",
        "image_path": "raju.png",  # Replace with your image path
        "phd_title": "Induction heating assisted friction stir welding of nylon 6A polymer",
        "year_awarded": "2024",
        "role": "Supervisor"
    }
]

# Display student information
for student in students:
    # Convert student image to Base64 for inline display
    student_image_base64 = image_to_base64(student["image_path"])
    st.markdown(f"""
    <div class="student-card">
        <img src="data:image/png;base64,{student_image_base64}" alt="Student Image">
        <div class="student-details">
            <b>Name:</b> {student['name']}<br>
            <b>PhD Title:</b> {student['phd_title']}<br>
            <b>Year Awarded:</b> {student['year_awarded']}<br>
            <b>Role:</b> {student['role']}
        </div>
    </div>
    """, unsafe_allow_html=True)



st.markdown("## Workshops", unsafe_allow_html=True)

# Styling for workshop list with black background compatibility
st.markdown("""
<style>
.workshop-container {
    font-size: 16px;
    color: #ffffff; /* Text color set to white */
    line-height: 1.6;
    margin: 20px 0;
}
.workshop-container ul {
    list-style-type: disc;
    padding-left: 20px;
    color: #ffffff; /* Bullet point color set to white */
}
</style>
""", unsafe_allow_html=True)

# Workshops content
workshops = """
<div class="workshop-container">
    <ul>
        <li>Five daysʼ workshop on <b>“Computational Analysis on Mechanical and Electronic Systems using ANSYS”</b>, organized by NIT-Surat from 7th Nov 2022 to 11th Nov 2022.</li>
        <li>One-week short term Course on <b>“Brain Mapping and Artificial Intelligence”</b>, organized by IIT Delhi from 11th March 2021 to 20th March 2021.</li>
        <li>AICTE recognized short term course organized by NITTTR, Chandigarh on <b>INDUCTION TRAINING PROGRAMME</b> through ICT during 10-14 December, 2012, held at United Institute of Technology, Naini, Allahabad.</li>
        <li>Self-Financed short term course on <b>Advanced Machining Processes</b> during 1-5 July, 2013, held at MNNIT, Allahabad.</li>
        <li>Workshop on <b>Micro Machining Technology</b> during 17-18 June, 2016, organized by IIT-BHU, Varanasi.</li>
        <li>National Welding Seminar during 9-11 December, 2015, organized by The Indian Institute of Welding, held at CIDCO Exhibition Centre, Vashi, Navi Mumbai.</li>
        <li>Workshop on <b>Manufacturing Automation</b> during 16-17 December, 2011, organized by Jaypee University of Engineering and Technology, Raghogarh, Guna (M.P).</li>
        <li><b>Magnetic Barkhausen Noise Characterization</b> of pack carburized IS - 2062 Low Carbon Steel during 11-14 November, 2016, held at IIT Kanpur (NMD-ATM 2016).</li>
        <li><b>Residual Stress in Pack Carburized Steel</b> during 2-3 April, 2016, organized by IIT-BHU, Varanasi.</li>
    </ul>
</div>
"""

# Display workshops
st.markdown(workshops, unsafe_allow_html=True)
