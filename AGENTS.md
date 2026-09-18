# AGENTS.md

本文件为所有 AI 编码助手（Qoder Agent 等）提供项目上下文，随代码库提交、团队共享。
更细粒度的强制约定见 `.qoder/rules/`；**规则与本文件冲突时，以规则为准**。

## 项目概述

Skill Lens AI —— 技能分析类应用（hackathon 项目），前后端分离。

- 后端：Python + FastAPI，提供 `/api` REST 接口，入口 `backend/main.py`。
- 前端：React + TypeScript + Vite（**尚未脚手架化**，见 `.qoder/rules/frontend.md`）。

## 目录结构

```
├── AGENTS.md              # 本文件：Agent 上下文总纲
├── .qoder/rules/          # 团队共享的强制规则（务必遵守）
├── .github/               # PR / issue 模板、CI
├── backend/               # FastAPI 后端
│   ├── main.py            # 应用入口（仅装配，无业务逻辑）
│   ├── app/
│   │   ├── api/routes.py  # 路由层
│   │   └── schemas.py     # Pydantic 请求/响应模型
│   ├── requirements.txt   # 运行时依赖（固定版本）
│   ├── requirements-dev.txt # 开发/质量工具依赖
│   └── pyproject.toml     # ruff / mypy / pytest 配置
└── frontend/              # React 前端（待初始化）
```

## 技术栈与版本

- Python **3.12**（见 `backend/.python-version`）；FastAPI、Pydantic v2、Uvicorn。
- 前端：React 18 + TypeScript + Vite，包管理统一用 **npm**。
- 质量工具：Python 用 ruff（lint + format）+ mypy；前端用 ESLint + Prettier。

## 常用命令

后端（在 `backend/` 目录执行）：

```bash
pip install -r requirements.txt -r requirements-dev.txt  # 安装依赖
uvicorn main:app --reload                                 # 本地运行
ruff format . && ruff check . && mypy .                   # 格式化 + 检查
pytest                                                    # 测试
```

前端（在 `frontend/` 目录执行，脚手架化后）：

```bash
npm install && npm run dev     # 安装 + 本地运行
npm run lint && npm run build  # 检查 + 构建
```

## 环境与配置

- 所有环境变量见 `.env.example`；复制为 `.env` 后填写，**`.env` 不提交**。
- 严禁在代码中硬编码密钥、令牌或本地绝对路径。

## 协作红线（必须遵守）

- 不直接向 `main` 推送；走 feature 分支 + PR。
- 提交信息遵循 Conventional Commits。
- 提交前本地跑通 lint 与测试。
- 改动他人负责模块的公共接口前先沟通。
- 新增依赖必须固定版本并写入 `requirements.txt` / `package.json`。

## 给 Agent 的工作约定

- 生成代码需与现有风格一致（命名、分层、错误处理）。
- 改动公共 API（`schemas` / `routes`）时，同步更新本文件与相关说明。
- 优先编辑现有文件，非必要不新增文件；不主动创建文档文件。
