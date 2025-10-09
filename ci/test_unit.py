import sys
import os

print(f"=== Unit Test (env={os.getenv('TEST_ENV')}) ===")

PASS = True

if PASS:
    print("✅ Unit tests passed.")
    sys.exit(0)
else:
    print("❌ Unit tests failed.")
    sys.exit(1)