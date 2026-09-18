---
trigger: glob
glob:
  - backend/**/*.py
---

# 后端规范（FastAPI + Pydantic v2）

## 路由

- 路由定义在 `backend/app/api/`，用 `APIRouter` 组织，在 `main.py` 通过 `app.include_router(..., prefix="/api")` 挂载。
- 每个接口必须声明 `response_model`，请求体/响应体用 Pydantic 模型定义。
- 路径用复数资源名 + 动作（如 `/skills/analyze`），保持 REST 风格。

## 数据模型

- 请求/响应模型统一放 `app/schemas.py`（模块变多时可拆到 `app/schemas/`）。
- 使用 Pydantic **v2** 语法（`model_validate` / `model_dump`），不要用 v1 的 `.parse_obj()` / `.dict()`。
- 字段必须有类型注解；可选字段用 `X | None = None`。

## 错误处理

- 业务错误用 `fastapi.HTTPException` 抛出，带明确 `status_code` 与 `detail`。
- 不要用裸 `except:` 吞掉异常。

## 类型与质量

- 所有函数带类型注解，能通过 `mypy .`。
- 提交前跑 `ruff format .` 与 `ruff check .`。

## 依赖与配置

- 新增第三方库必须固定版本写入 `backend/requirements.txt`。
- 配置从环境变量读取（`os.environ` 或 pydantic-settings），禁止硬编码密钥。

## 示例（符合规范）

```python
# app/schemas.py
from pydantic import BaseModel

class SkillRequest(BaseModel):
    skill_name: str

class SkillResponse(BaseModel):
    skill_name: str
    analysis: str

# app/api/routes.py
from fastapi import APIRouter, HTTPException
from app.schemas import SkillRequest, SkillResponse

router = APIRouter()

@router.post("/skills/analyze", response_model=SkillResponse)
def analyze_skill(request: SkillRequest) -> SkillResponse:
    if not request.skill_name.strip():
        raise HTTPException(status_code=422, detail="skill_name 不能为空")
    return SkillResponse(skill_name=request.skill_name, analysis="...")
```
