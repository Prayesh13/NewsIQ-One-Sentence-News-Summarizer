import streamlit as st
from transformers import TFAutoModelForSeq2SeqLM, AutoTokenizer
import tensorflow as tf

# ---- Config ----
MAX_INPUT_LENGTH = 512
MAX_TARGET_LENGTH = 150
MIN_TARGET_LENGTH = 30

# ---- Load model and tokenizer ----
folder_path = r"./Model_trained"  # Replace this
@st.cache_resource
def load_model_tokenizer():
    model = TFAutoModelForSeq2SeqLM.from_pretrained(folder_path)
    tokenizer = AutoTokenizer.from_pretrained(folder_path)
    return model, tokenizer

model, tokenizer = load_model_tokenizer()

# ---- Streamlit UI ----
st.title("📄 Document Summarizer")
st.write("Enter a long-form document and the model will generate a concise summary using a fine-tuned Transformer.")

user_input = st.text_area("Enter document:", height=300, placeholder="Paste your document here...")

if st.button("Summarize"):
    if user_input.strip() == "":
        st.warning("Please enter some text to summarize.")
    else:
        with st.spinner("Generating summary..."):
            inputs = tokenizer.encode("summarize: " + user_input, return_tensors="tf", 
                                      max_length=MAX_INPUT_LENGTH, truncation=True)
            summary_ids = model.generate(
                inputs,
                max_length=MAX_TARGET_LENGTH,
                min_length=MIN_TARGET_LENGTH,
                length_penalty=2.0,
                num_beams=4,
                early_stopping=True,
                do_sample=False,
                use_cache=True
            )
            summary = tokenizer.decode(tf.convert_to_tensor(summary_ids)[0], skip_special_tokens=True)
        st.subheader("Generated Summary:")
        st.success(summary)
