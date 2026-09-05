# Evaluation script for video-trimmer task
import os
import sys

def evaluate():
    workspace = os.environ.get('AGENT_WORKSPACE', '.')
    trim_file = os.path.join(workspace, 'video_trimmer.py')
    if not os.path.exists(trim_file):
        print('FAIL: video_trimmer.py not found')
        return False
    print('PASS: video_trimmer.py found')
    return True

if __name__ == '__main__':
    success = evaluate()
    sys.exit(0 if success else 1)
