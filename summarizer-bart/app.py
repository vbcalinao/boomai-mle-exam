# Step 1: Import necessary libraries
from transformers import BartTokenizer, BartForConditionalGeneration
import streamlit as st

# Step 2: Load the BART pre-trained model
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

# Step 3: Create a function to summarize text
def summarize_text(text):
    inputs = tokenizer([text], max_length=1024, return_tensors='pt')
    summary_ids = model.generate(inputs['input_ids'], num_beams=4, max_length=5, early_stopping=True)
    return [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids]

# Step 4: Create a Streamlit application
st.title('Text Summarization')
text = st.text_area("Enter Text")
if st.button('Summarize'):
    summary = summarize_text(text)
    st.write(summary)