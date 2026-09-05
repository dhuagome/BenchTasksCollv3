# Evaluation script for reminder-service task
import os
import sys

def evaluate():
    workspace = os.environ.get('AGENT_WORKSPACE', '.')
    reminder_file = os.path.join(workspace, 'reminder_service.py')
    if not os.path.exists(reminder_file):
        print('FAIL: reminder_service.py not found')
        return False
    print('PASS: reminder_service.py found')
    return True

if __name__ == '__main__':
    success = evaluate()
    sys.exit(0 if success else 1)
