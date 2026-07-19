from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    """
    Split loaded documents into smaller chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    chunks = []

    for doc in documents:
        split_texts = splitter.split_text(doc["content"])

        for text in split_texts:
            chunks.append({
                "filename": doc["filename"],
                "content": text
            })

    return chunks