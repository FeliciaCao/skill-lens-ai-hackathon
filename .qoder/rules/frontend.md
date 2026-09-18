---
trigger: glob
glob:
  - frontend/**/*.ts
  - frontend/**/*.tsx
  - frontend/**/*.js
  - frontend/**/*.jsx
---

# 前端规范（React + TypeScript + Vite）

> 前端应用尚未脚手架化。首次创建时在**仓库根目录**执行：
> `npm create vite@latest frontend -- --template react-ts`

## 语言与组件

- 一律用 TypeScript，不新增 `.js` / `.jsx` 业务文件。
- 用函数式组件 + Hooks，不用 class 组件。
- 组件文件 `PascalCase`（`SkillCard.tsx`），工具/hook 文件 `camelCase`（`useSkill.ts`）。
- Props 必须定义 `interface` / `type`；禁止 `any`（确需时用 `unknown` 并收窄）。

## 目录与数据流

- `src/components/` 可复用组件；`src/pages/` 页面；`src/api/` 接口封装；`src/types/` 类型；`src/hooks/` 自定义 hook。
- 组件内不直接 `fetch`，统一调用 `src/api/` 中的函数。
- 与后端交互的类型应与后端 `schemas` 对齐。

## 样式

- 全项目统一一种方案（CSS Modules 或 Tailwind），不混用。

## 质量与依赖

- 提交前 `npm run lint` 与 `npm run build` 必须通过。
- 用 ESLint + Prettier，配置随仓库提交，不各自本地改。
- 统一用 npm；新增依赖写入 `package.json` 并提交 `package-lock.json`。
