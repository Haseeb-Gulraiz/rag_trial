Files info:

fill_db.py: builds the chroma db from provided data that is to be placed in data folder
ask.py: get the data from db and provide responses via openai
rest_api.py: build a flask api to get responses from rest api  
frontend.py: get responses from rest_api and displays it on streamlit frontend

To run:
build a virtual environment and install requirements.txt
make .env where openai key is to be added. OPENAI_API_KEY= ''
first run rest_api.py and then frontend.py

request-curl :
curl --location 'http://127.0.0.1:5000/ask' \
--header 'Content-Type: application/json' \
--data '{
    "query": "what is the yield of brocolli?"
}'
