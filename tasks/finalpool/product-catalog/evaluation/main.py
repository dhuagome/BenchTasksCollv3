# Evaluation script for product-catalog task
import os
import sys

def evaluate():
    workspace = os.environ.get('AGENT_WORKSPACE', '.')
    catalog_file = os.path.join(workspace, 'product_catalog.json')
    if not os.path.exists(catalog_file):
        print('FAIL: product_catalog.json not found')
        return False
    print('PASS: product_catalog.json found')
    return True

if __name__ == '__main__':
    success = evaluate()
    sys.exit(0 if success else 1)
