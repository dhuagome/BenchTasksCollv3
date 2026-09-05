# Evaluation script for image-processor task
import os
import sys

def evaluate():
    workspace = os.environ.get('AGENT_WORKSPACE', '.')
    processor_file = os.path.join(workspace, 'image_processor.py')
    if not os.path.exists(processor_file):
        print('FAIL: image_processor.py not found')
        return False
    print('PASS: image_processor.py found')
    return True

if __name__ == '__main__':
    success = evaluate()
    sys.exit(0 if success else 1)
