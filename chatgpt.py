from langchain.text_splitter import MarkdownHeaderTextSplitter
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import HuggingFaceEmbeddings


# Get embeddings.
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
    ("####", "Header 4"),
]

markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)

with open('data/data.md', 'r', encoding='utf-8') as f:
    markdown_document = f.read()
    md_header_splits = markdown_splitter.split_text(markdown_document)

print(md_header_splits[:10])

retriever = Chroma.from_documents(documents=md_header_splits, embedding=embeddings ).as_retriever(
    search_kwargs={"k": 2}
)
query = "how to train a model"

# Get relevant documents ordered by relevance score
docs = retriever.get_relevant_documents(query)
print(docs[0].page_content)


# Create a retriever



