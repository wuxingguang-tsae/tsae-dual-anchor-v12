# TSAE 框架配置：外生阈值（严禁修改为拟合数据）
ALPHA = 0.05       # 成本锚分位 (95th percentile)
BETA = 0.80        # 支付锚分位 (80th percentile)
GAMMA_LOW = 0.10   # 流动性缓冲下限
GAMMA_HIGH = 0.30  # 流动性缓冲上限

# 扫描参数（敏感性分析用）
ETA_LOW = 0.20
ETA_HIGH = 0.40
ETA_STEP = 0.01
ETA_BASE = 0.30