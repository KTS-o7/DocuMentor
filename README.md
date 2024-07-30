# DocuMentor

A local Rag implementation to chat with anything !

Quick run guide

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
touch .env
cp exampleenv .env
mkdir data
mkdir vectorstores
mkdir vectorstores/db
# Add files to the data folder
python load_data.py
chainlit run multiChat.py

## For single instant chat
chainlit run InstantChat.py
# supports only pdf
```

## Screenshots

## Detailed usage guide
