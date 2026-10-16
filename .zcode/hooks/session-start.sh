#!/bin/bash
# Dexter SessionStart 钩子:向新会话注入开工仪式提醒(替代不存在的工作记忆)
printf '{"additionalContext": "Dexter 开工仪式:先读 Dexter/journal/latest.md → Dexter/agenda.md 在办与监控哨 → Dexter/honor.md 同类过失 → Dexter/promises.md 到期项。所有路径以 Dexter/ 为根。档案里没有的就明说没有。"}\n'
exit 0
