from fastapi import FastAPI
from pydantic import BaseModel
from langchain_ollama import OllamaLLM
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document

# Load the FAISS vectorstore built from your PDF + tables
embedding_model = GPT4AllEmbeddings()
vectorstore = FAISS.load_local(
    "vectorstore",
    embedding_model,
    allow_dangerous_deserialization=True
)

# Use the phi model from Ollama
llm = OllamaLLM(model="phi")

# Create a RetrievalQA chain using the retriever
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever()
)

#  Set up small talk responses
small_talk_responses = {
    "hi": "Hi there! How can I help you with the dataset?",
    "hello": "Hello! Ask me something from the dataset.",
    "bye": "Goodbye! Have a great day.",
    "thank you": "You're welcome!",
}

#  Initialize the FastAPI app
app = FastAPI()

#  Request model
class Question(BaseModel):
    question: str

#  API endpoint to handle questions
@app.post("/ask")
async def ask_question(payload: Question):
    question = payload.question.lower().strip()

    #  Handle small talk directly
    if question in small_talk_responses:
        print(f"[SMALL TALK] '{question}'")
        return {"answer": small_talk_responses[question]}

    #  Retrieve relevant documents from vectorstore
    retrieved_docs = vectorstore.similarity_search(question, k=2)

    #  If no matching content found, block the question
    if not retrieved_docs:
        print(f"[BLOCKED] No relevant data for: {question}")
        return {"answer": "Sorry, I couldn’t find anything in the dataset related to your question."}

    #  Proceed with answering from retrieved context
    print(f"[QUESTION] {question}")
    response = qa_chain.invoke(question)
    return {"answer": response["result"]}