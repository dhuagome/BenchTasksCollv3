# Evaluation script for form-builder task
import os
import sys

def evaluate():
    workspace = os.environ.get('AGENT_WORKSPACE', '.')
    form_file = os.path.join(workspace, 'form_builder.py')
    if not os.path.exists(form_file):
        print('FAIL: form_builder.py not found')
        return False
    print('PASS: form_builder.py found')
    return True

if __name__ == '__main__':
    success = evaluate()
    sys.exit(0 if success else 1)
