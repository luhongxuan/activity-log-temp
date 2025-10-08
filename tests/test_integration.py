import sys
import os

print(f"=== Integration Test (env={os.getenv('TEST_ENV')}) ===")

PASS = True   # ✅ 測試通過 (改成 False 可模擬失敗)

if PASS:
    print("✅ Integration tests passed.")
    sys.exit(0)
else:
    print("❌ Integration tests failed.")
    sys.exit(1)
