# HCLTech Internship Project – RAG-based Chatbot with Multimodal PDF Understanding

## Project Title
**Intelligent Document Question-Answering System using RAG and Vision-Language Models**

## Intern Details
- **Name:** R. Priyanka  
- **College:** Sudharsan Engineering College  
- **Department:** B.Tech Artificial Intelligence and Data Science  
- **Company:** HCLTech  
- **Project Type:** Learning-Based Internship



## Project Overview

This project aims to develop a **Retrieval-Augmented Generation (RAG)**-based chatbot that can answer user queries from a large collection of technical PDF documents. The documents contain a mix of text, tables, and images (especially flowcharts and diagrams).

The solution focuses on:
- Chunking and embedding of PDF text
- Handling tables and diagrams separately
- Summarizing image content using a **Vision-Language Model (LLaVA)**
- Building an interactive chatbot interface using **LangChain + FAISS + OpenAI**



## Project Architecture

PDFs ➝ Chunking ➝ Embedding ➝ FAISS Vector DB
⬇
Text, Table, Figure Extraction
⬇
LLaVA-based Flowchart Summarization
⬇
RAG Pipeline (LangChain)
⬇
Interactive Chatbot Output
## Folder Structure
├── main.py # Main script to run the chatbot
├── vectorstore/ # FAISS index and embedding store
├── xerox_dataset/ # PDF files
├── images/ # Extracted diagrams/figures
├── summaries/
│ └── flowchart_summaries.txt # AI-generated diagram summaries
├── utils/
│ ├── pdf_parser.py # Custom PDF parsing logic
│ ├── table_extractor.py # Extracts tables
│ ├── image_extractor.py # Extracts diagrams
│ ├── flowchart_summarizer.py # Google Colab script for LLaVA
└── README.md # Project description

## Technologies & Tools Used

- Python
- LangChain
- OpenAI API (GPT-3.5 / GPT-4)
- FAISS
- PyMuPDF / pdfplumber / fitz – for PDF text & image parsing
- Pandas – for table extraction
- LLaVA-1.5 – Vision-Language Model for diagram summarization
- Google Colab – for running image-based AI model
- VS Code – for development



## Features

- Intelligent Q&A over large PDF corpus  
- Extracts and answers from **tables**  
- Auto-summarizes and interprets **diagrams and flowcharts**  
- Dynamic retrieval using FAISS  
- Clean code with modular utility functions  
- Ready for frontend integration



## How to Run

### 1. Prepare Environment

pip install -r requirements.txt
2. Place your PDFs
Put all PDFs in the xerox_dataset/ folder.

3. Run Preprocessing
python utils/pdf_parser.py
python utils/table_extractor.py
python utils/image_extractor.py

4. Summarize Diagrams (Run in Colab)
Open flowchart_summarizer.py in Google Colab.

Upload images and run each cell to generate summaries.

Save the output as flowchart_summaries.txt inside summaries/.

5. Run the Chatbot
python main.py
Sample Query Types
“Explain the architecture mentioned in document A.”

“What does the diagram about data pipeline convey?”

“Summarize the table with accuracy metrics.”

“Give me the steps described in the process flowchart.”

Challenges Faced
Extracting embedded diagrams from PDFs

Structuring and chunking mixed content types

Integrating multimodal LLM (LLaVA) on limited infrastructure

Improving retrieval quality for tabular and visual data

Outcome
A working chatbot that can intelligently answer document-based questions.

Successfully handled both textual and non-textual data sources.

Learned to integrate state-of-the-art Vision-Language Models into real use cases.

Acknowledgements
Thanks to the HCLTech mentorship team and the AI Tools and Resources provided, which helped in shaping and guiding this internship project.


