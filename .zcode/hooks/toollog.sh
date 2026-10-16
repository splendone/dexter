#!/bin/bash
# Dexter PostToolUse 记账钩子:Write/Edit 落盘后追加一行到 journal/toollog.md
# stdin 是事件 JSON,截断原样记录;永远 exit 0,记账失败不阻塞会话
LOG="${ZCODE_PROJECT_DIR:-$(pwd)}/Dexter/journal/toollog.md"
mkdir -p "$(dirname "$LOG")"
{
  printf '%s | ' "$(date '+%F %T')"
  head -c 300
  printf '\n'
} >> "$LOG" 2>/dev/null
exit 0
