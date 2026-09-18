---
trigger: always_on
---

# 架构与目录约定

## 后端分层（backend/）

- `main.py`：应用入口，只负责创建 FastAPI 实例、注册中间件、挂载路由；**不写业务逻辑**。
- `app/api/`：路由层（HTTP 入口），负责请求解析与响应，不写复杂业务逻辑。
- `app/schemas.py`：Pydantic 数据模型（请求/响应契约）。
- 业务逻辑放 `app/services/`（按需新增），数据访问放 `app/repositories/` 或 `app/db/`（按需新增）。
- 依赖方向：`api → services → repositories`，**禁止反向依赖**。

## 前端结构（frontend/，React + TS）

- `src/components/` 可复用组件；`src/pages/` 页面；`src/api/` 接口封装；`src/types/` 类型；`src/hooks/` 自定义 hook。
- 组件内不直接 `fetch`，统一通过 `src/api/` 调用后端。

## 通用

- 新增功能优先放入既有分层，不在仓库根目录随意堆文件。
- 跨端共享的数据结构以后端 `schemas.py` 为准，前端类型与之对齐。
- 不提交构建产物与缓存（`dist/`、`__pycache__/` 等，已在 `.gitignore`）。
