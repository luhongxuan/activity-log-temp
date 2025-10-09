# ci/generate_badge.py
import os
from coverage_badge import badge

# 產生 coverage.svg 檔案
badge.report(metafile=".coverage", outfile="coverage.svg")
print("✅ coverage.svg 產生完成！")
