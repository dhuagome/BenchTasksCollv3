# Evaluation script for feedback-collector task
import os
import sys

def evaluate():
    workspace = os.environ.get('AGENT_WORKSPACE', '.')
    feedback_file = os.path.join(workspace, 'feedback.json')
    if not os.path.exists(feedback_file):
        print('FAIL: feedback.json not found')
        return False
    print('PASS: feedback.json found')
    return True

if __name__ == '__main__':
    success = evaluate()
    sys.exit(0 if success else 1)
