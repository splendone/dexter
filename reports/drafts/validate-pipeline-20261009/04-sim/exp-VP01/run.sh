#!/usr/bin/env bash
# ============================================================
#  run.sh — exp-VP01 · R3-NeuTraL 三臂中立对照(dry-run 验证)
#  纪律:不得含 2>/dev/null 吞错;失败/崩溃须暴露在日志里。
#  ⚠️ dry-run:本脚本为真实备料,未在真实 GPU/仿真环境执行(无算力)。
#  真实跑前须:① 委托人明示云/API 预算锚点(🔴);② 锁定闭源 VLM 骨干版本。
# ============================================================
set -euo pipefail          # 出错即停、未定义变量报错、管道任一环失败即失败(不吞错)

EXP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$EXP_DIR"

CONFIG="config.yaml"
LOG_DIR="logs"
mkdir -p "$LOG_DIR"

# 冻结环境快照(复现地基)
python3 -c "import torch, numpy, sys; print('torch', torch.__version__); print('numpy', numpy.__version__); print('cuda', torch.version.cuda); print('py', sys.version)" > env-lock.txt
git rev-parse HEAD > code-commit.txt 2>&1 || echo "NOT-A-GIT-REPO: snapshot $(date -u +%FT%TZ)" > code-commit.txt

mapfile -t SEEDS < seeds.txt

# 三臂 + 基线对齐 + 消融(变体直列,不靠 $VAR 词分割;zsh 兼容)
for VARIANT in R3_vla_frozen R3_harness R3_cap baseline_align_pi05 R3_no_recovery_axis; do
  for SEED in "${SEEDS[@]}"; do
    echo "[run] variant=$VARIANT seed=$SEED"
    # 冻结子集 rollout + 恢复轴探测(SCB)+ 成本计量;日志落盘,不吞错
    python3 run_libero_pro_eval.py \
      --config "$CONFIG" \
      --variant "$VARIANT" \
      --seed "$SEED" \
      --frozen-subset N300 \
      --probe recovery \
      2>&1 | tee "$LOG_DIR/${VARIANT}_seed${SEED}.log"
  done
done

# 汇总到 results.json(供 ⑥ ResultsAuditor 核)
python3 aggregate_results.py --config "$CONFIG" --logs "$LOG_DIR" --out results.json

echo "[done] results -> results.json ; logs -> $LOG_DIR/"
echo "[next] 交 ⑥:python3 <skill>/references/scripts/check_freeze.py $EXP_DIR"
