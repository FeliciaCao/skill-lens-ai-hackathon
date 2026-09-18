---
trigger: always_on
---

# 通用编码风格

## 命名

- Python：模块/函数/变量用 `snake_case`，类用 `PascalCase`，常量用 `UPPER_SNAKE`。
- 前端 TS：变量/函数 `camelCase`，类型/组件 `PascalCase`，常量 `UPPER_SNAKE`。
- 命名表意清晰，避免无意义缩写与拼音。

## 注释与文档

- 注释解释“为什么”，不复述“做了什么”。
- 公共函数/接口写简洁 docstring / JSDoc。
- 代码注释默认使用中文（保留英文技术术语与标识符）。

## 代码质量

- 单个函数职责单一，避免超长函数与深层嵌套。
- 不提交被注释掉的死代码，不残留调试 `print` / `console.log`。
- 不硬编码密钥、令牌、本地绝对路径。

## 一致性

- 修改代码时保持与周围代码风格一致（命名、缩进、错误处理）。
- 优先编辑现有文件，非必要不新增文件；不主动创建文档文件。

## 提交前自检

- 后端：`ruff format .` + `ruff check .` + `mypy .` + `pytest` 通过。
- 前端：`npm run lint` + `npm run build` 通过。
