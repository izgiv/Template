import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

# Load sensitive values from environment variables
GIT_TOKEN = os.getenv("GITHUB_TOKEN")
GIT_USER = os.getenv("GITHUB_USER", "izgiv")  # default to izgiv if not set

if GIT_TOKEN:
    repo_url = f"https://{GIT_USER}:{GIT_TOKEN}@github.com/izgiv/Monarch-Pyro"
    clone_cmd = f"git clone {repo_url} bott && cd bott && pip3 install -U -r requirements.txt && nohup python3 -m Monarch &"
    os.system(clone_cmd)
else:
    print("Warning: GITHUB_TOKEN environment variable is not set. Skipping repo clone.")
