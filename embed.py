import os

import streamlit as st

from txtai.embeddings import Embeddings

class Application:
    """
    Main application.
    """

    def __init__(self):
        """
        Creates a new application.
        """

        # Create embeddings model, backed by sentence-transformers & transformers
        # self.embeddings = Embeddings({"path": "sentence-transformers/nli-mpnet-base-v2"})
        # #self.embeddings = Embeddings({"path": "sentence-transformers/bert-base-nli-mean-tokens"})
        # filename = 'occ_clean.txt';
        # with open(filename) as file:
        #     data = file.readlines()
        # self.embeddings.index([(uid, text, None) for uid, text in enumerate(data)])
        # self.embeddings.save("index")
        self.embeddings = Embeddings()
        self.embeddings.load("index")

    def run(self):
        """
        Runs a Streamlit application.
        """

        st.title("Similarity Search")
        st.markdown("This application runs a basic similarity search that identifies the best matching row for a query.")

        data = [
            "US tops 5 million confirmed virus cases",
            "Canada's last fully intact ice shelf has suddenly collapsed, forming a Manhattan-sized iceberg",
            "Beijing mobilises invasion craft along coast as Taiwan tensions escalate",
            "The National Park Service warns against sacrificing slower friends in a bear attack",
            "Maine man wins $1M from $25 lottery ticket",
            "Make huge profits without work, earn up to $100,000 a day",
        ]

        filename = 'occ_clean.txt';
        with open(filename) as file:
            data = file.readlines()

        #data = st.text_area("Data", value="\n".join(data))
        data = st.text_area("Data", value="".join(data))
        #print(data)
        query = st.text_input("Query")

        data = data.split("\n")


        if query:
            # Get index of best section that best matches query
            #uid = self.embeddings.similarity(query, data)[0][0]
            uid = self.embeddings.search(query, 1)[0][0]
            st.write(data[uid])


@st.cache(allow_output_mutation=True)
def create():
    """
    Creates and caches a Streamlit application.
    Returns:
        Application
    """

    return Application()


if __name__ == "__main__":
    os.environ["TOKENIZERS_PARALLELISM"] = "false"

    # Create and run application
    app = create()
    app.run()