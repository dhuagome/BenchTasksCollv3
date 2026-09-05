# Evaluation script for activity-logger task
import os
import sys

def evaluate():
    workspace = os.environ.get('AGENT_WORKSPACE', '.')
    log_file = os.path.join(workspace, 'activity_log.json')
    if not os.path.exists(log_file):
        print('FAIL: activity_log.json not found')
        return False
    print('PASS: activity_log.json found')
    return True

if __name__ == '__main__':
    success = evaluate()
    sys.exit(0 if success else 1)
