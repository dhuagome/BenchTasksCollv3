# Preprocess script for image-processor task
import os

def preprocess():
    workspace = os.environ.get('AGENT_WORKSPACE', '.')
    os.makedirs(workspace, exist_ok=True)

if __name__ == '__main__':
    preprocess()
