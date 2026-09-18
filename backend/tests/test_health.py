from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root_health() -> None:
    """根级健康检查（main.py 直接挂载）。"""
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_api_health() -> None:
    """/api 前缀下的健康检查（routes.py）。"""
    resp = client.get("/api/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_analyze_skill() -> None:
    """技能分析接口返回契约字段。"""
    resp = client.post("/api/skills/analyze", json={"skill_name": "python"})
    assert resp.status_code == 200
    body = resp.json()
    assert body["skill_name"] == "python"
    assert "python" in body["analysis"]
