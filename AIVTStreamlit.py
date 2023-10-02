
import streamlit as st
from AIVideoTranscriber import AIVT_services
import tempfile


st.set_page_config(
    page_title="AIVideoTranscriber+",
    page_icon=":performing_arts:",
    layout="wide"
  )


with st.container():
  c1,c2 = st.columns(2)
  image = "image/jcvqmhcv.png" # Replace with the path to your image file
  c2.image(image, use_column_width=True)

  with c1:

    st.title("Welcome to AIVideoTranscriber+")
    st.write("This is an AI-based application that can transcribe audio from video files and extract metadata such as Title, Description, Keywords, and Category using Speech-to-Text and OpenAI APIs. The extracted metadata can be used to create promotional materials for the video files.")
    st.write("---")
    st.markdown("""#### Anitesh Shaw""")
    st.write(":envelope: anitesh.shaw@gmail.com")
    st.write("📲 +1 (973) 641-4269")



if "file" not in st.session_state:
    st.session_state["file"] = None
    
   
   
def change_file_state():
  st.session_state["file"] = "done"


with st.container():
  st.write("---")
  col1,col2 = st.columns(2)   

  root_folder =col1.file_uploader("Upload Files you want to Transcribe",type=['mp4','wav'], on_change=change_file_state)



if st.session_state["file"] == "done":
  
  with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    temp_file.write(root_folder.read())
    file_path = temp_file.name

 
    
  col1.success("File Successfully uploaded")
 
st.write("---")
st.write("##")
if st.session_state["file"] is not None:
  OPENAI_API_Key=col2.text_input("Enter your OpenAI API Key")
  Speech_API_KEY1=col2.text_input("Enter your Azure Cognitive Speech API Key")
  start_transcription_button = col2.button("Start Transcriber")
  if start_transcription_button:
    col2.write("Transcribing is in progress...")
    AIVT_services(root_folder,file_path,OPENAI_API_Key,Speech_API_KEY1) 
    col2.write("Transcribing is completed")


    
  else:
    col2.write("Please click Start Transcriber to process the file")  