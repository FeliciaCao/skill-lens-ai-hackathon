---
trigger: model_decision
description: 涉及 git 提交、分支、合并、PR、提交信息规范时使用。
---

# Git 协作流程

## 分支

- `main` 为受保护主干，**禁止直接 push**。
- 功能分支从最新 `main` 切出，命名：`feat/<简述>`、`fix/<简述>`、`chore/<简述>`。
- 分支生命周期尽量短，频繁同步 `main` 减少冲突。

## 提交信息（Conventional Commits）

格式：`<type>(<scope>): <subject>`

- type：`feat` / `fix` / `docs` / `style` / `refactor` / `perf` / `test` / `chore` / `ci`
- scope（可选）：`backend` / `frontend` / `ci` 等
- subject：祈使句、简短、结尾不加句号

示例：`feat(backend): add /skills/analyze endpoint`

## Pull Request

- 每个 PR 聚焦单一主题，按模板填写（改动、测试、影响、截图）。
- 合并前需至少 1 人 Review 通过，且 CI（lint + test）通过。
- 统一用 **Squash Merge**，保持 `main` 历史整洁。

## 协作注意事项

- 改动他人负责模块的公共接口前先沟通。
- 不提交生成物与本地环境文件（`.env`、`dist/`、`__pycache__/`）。
