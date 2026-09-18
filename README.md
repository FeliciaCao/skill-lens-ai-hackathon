# Skill Lens AI

前后端分离项目：后端 Python FastAPI，前端 React + TypeScript + Vite。

> 多人协作请先阅读 [AGENTS.md](AGENTS.md) 与 [`.qoder/rules/`](.qoder/rules)（团队共享的 Qoder 规则）。

## 项目结构

```
├── AGENTS.md      # AI Agent 上下文总纲
├── .qoder/rules/  # 团队共享规则 (Qoder)
├── backend/       # 后端服务 (FastAPI)
└── frontend/      # 前端应用 (React + Vite)
```

## 快速启动

### 后端

```bash
cd backend
pip install -r requirements.txt -r requirements-dev.txt
uvicorn main:app --reload
```

服务默认运行在 `http://localhost:8000`，API 文档访问 `http://localhost:8000/docs`。

### 前端

前端尚未脚手架化，首次初始化（在仓库根目录执行）：

```bash
npm create vite@latest frontend -- --template react-ts
cd frontend && npm install && npm run dev
```

默认运行在 `http://localhost:5173`。

## 环境变量

复制 `.env.example` 为 `.env` 并填写真实值，`.env` 不会提交到 git。

## 团队协作规范

- **规则即契约**：`.qoder/rules/` 下的规则随仓库共享，每个人的 Qoder 都会自动遵守；新增约定请改规则文件，而非口头传达。
- **分支**：`main` 受保护，功能走 `feat/xxx` 分支 + PR，禁止直接 push。
- **提交信息**：遵循 Conventional Commits（见 `.qoder/rules/git-workflow.md`）。
- **提交前自检**：后端 `ruff format . && ruff check . && mypy . && pytest`；前端 `npm run lint && npm run build`。
