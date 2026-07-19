import os

DOCUMENTS_FOLDER = "documents"


def load_documents():
    """
    Load all text documents from the documents folder.
    """

    documents = []

    for file in os.listdir(DOCUMENTS_FOLDER):

        if file.endswith(".txt"):

            file_path = os.path.join(DOCUMENTS_FOLDER, file)

            with open(file_path, "r", encoding="utf-8") as f:

                text = f.read()

                documents.append(
                    {
                        "filename": file,
                        "content": text
                    }
                )

    return documents