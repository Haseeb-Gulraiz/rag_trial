from flask import Flask, request, jsonify
import chromadb
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# setting the environment

DATA_PATH = r"data"
CHROMA_PATH = r"chroma_db"

chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = chroma_client.get_or_create_collection(name="trial_data")

client = OpenAI()

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_query = data.get("query", "")

    if not user_query:
        return jsonify({"error": "Query parameter is required."}), 400


    results = collection.query(
        query_texts=[user_query],
        n_results=5
    )

    print(results['documents'])
    #print(results['metadatas'])


    system_prompt = """
    You are a helpful assistant. You answer questions about growing vegetables in Florida. 
    But you only answer based on knowledge I'm providing you.
    --------------------
    The data:
    """+str(results['documents'])+"""
    """

    #print(system_prompt)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages = [
            {"role":"system","content":system_prompt},
            {"role":"user","content":user_query}    
        ]
    )

    return jsonify({"response": response.choices[0].message.content})

if __name__ == '__main__':
    app.run(debug=True)

# print("\n\n---------------------\n\n")

# print(response.choices[0].message.content)