# 📰 NewsIQ: One-Sentence News Summarizer

NewsIQ is a lightweight and intelligent NLP application designed to distill lengthy news articles into a single, clear, and concise sentence. Tailored for headline generation and rapid news comprehension, it enables users to gain quick insights without reading full articles.

The application is powered by a fine-tuned T5 (Text-To-Text Transfer Transformer) model trained on the XSum dataset, which specializes in generating highly abstractive, single-sentence summaries of BBC news content.

T5 was selected over models like BERT and GPT due to its encoder-decoder architecture, which is inherently suited for text generation tasks. Unlike BERT, which is limited to understanding tasks, and GPT, which is unidirectional and computationally intensive, T5 excels at structured summarization—making it an ideal choice for efficient and accurate headline generation.

---

## 🚀 Features

- 🔍 Extracts essential information from news content.
- 🧠 Generates a one-sentence summary/headline.
- ⚡ Powered by Hugging Face Transformers.
- ✅ Simple interface for quick input/output.
- 📦 Easily deployable as a notebook, script, or web app.

---

## 🛠️ Technologies Used

- Python
- Jupyter Notebook
- Transformers (`HuggingFace`)
- Torch
- T5 Model (`t5-small`)
- SentencePiece
- Streamlit (UI)

---

## 📁 Project Structure

```

NewsIQ/
│
├── NewsIQ_Headline_Generator.ipynb   # Main notebook
├── Model_trained/                            # Fine-tuned model (optional)
├── requirements.txt                  # Dependencies
├── README.md                         # Project info
└── app/                              # (Optional) Streamlit or Flask app

```
---


## 📌 How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/NewsIQ.git
cd NewsIQ
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Notebook

Open the `NewsIQ_Headline_Generator.ipynb` in Jupyter Notebook or VSCode:

```bash
jupyter notebook NewsIQ_Headline_Generator.ipynb
```

Or convert to a script and run:

```bash
python headline_generator.py
```

---

## 📸 Screenshots
![NewsIQ UI](screenshots/image.png)


## 🧪 Example

**Input:**

> The government announced a new policy today aiming to reduce emissions by 30% by the year 2030, focusing on clean energy investments and stricter vehicle regulations.

**Output:**

> Government unveils new policy to cut emissions by 30% by 2030.


---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📜 License

[No Licence]()

---

## 🙌 Acknowledgments

* [Hugging Face Transformers](https://huggingface.co/transformers/)
* [T5 Model](https://huggingface.co/t5-small)
* [News Summarization Research](https://arxiv.org/abs/2006.15454)

```
