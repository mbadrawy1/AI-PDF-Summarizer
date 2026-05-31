# Import the required libraries
import streamlit as st
import google.generativeai as genai
import PyPDF2

# Set the title of our web application
st.title("PDF Summarizer AI 🤖")

# Create a file uploader allowing only PDF files
uploaded_file = st.file_uploader("Upload your PDF document here", type="pdf")

# Check if a file has been uploaded
if uploaded_file is not None:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    
    # Initialize an empty string to store the extracted text
    extracted_text = ""
    
    # Loop through all the pages in the PDF to extract text
    for page in pdf_reader.pages:
        extracted_text += page.extract_text()
        
    # Display a success message
    st.success("PDF uploaded and text extracted successfully! 🎉")
    
    # Show a small preview of the extracted text (first 500 characters)
    st.write("Here is a quick preview of the text:")
    st.write(extracted_text[:500] + "...")
    # --- The AI Summary Section ---
    st.write("---") # Creates a horizontal line to separate sections
    
    # Add a field for the user to enter their API Key
    api_key = st.text_input("Enter your Google Gemini API Key:", type="password")
    
    # Create a button to start the summary process
    if st.button("Summarize PDF 🚀"):
        
        # Check if the user entered the key
        if api_key == "":
            st.warning("Please enter your API Key first!")
        else:
            try:
                # 1. Setup the API with your Key
                genai.configure(api_key=api_key)
                
                # 2. Choose the AI model we want to use (Flash is fast and great for text)
                model = genai.GenerativeModel('gemini-3.5-flash')
                
                # 3. Create the prompt (the instructions for the AI)
                prompt = f"Please summarize the following text in a clear and concise way:\n\n{extracted_text}"
                
                # 4. Show a loading spinner while the AI is thinking
                with st.spinner("AI is reading and summarizing... ⏳"):
                    
                    # Send the request to Gemini and get the response
                    response = model.generate_content(prompt)
                    
                    # 5. Display the final summary
                    st.subheader("Here is your Summary 📄:")
                    st.write(response.text)
                    
            except Exception as e:
                # Show an error message if something fails (e.g., wrong API key)
                st.error(f"Oops! Something went wrong: {e}")