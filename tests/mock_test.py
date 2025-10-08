# ci/mock_test.py
import sys

PASS = False

print("=== 模擬測試階段 ===")

if PASS:
    print("✅ 所有測試通過，準備部署！")
    sys.exit(0)
else:
    print("❌ 測試失敗，停止部署。")
    sys.exit(1)