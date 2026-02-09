# PinPoint

## 目标

把“项目依赖版本 -> AI 可消费上下文”这件事标准化，降低 AI 编码工具（如 Codex / Gemini CLI）在依赖 API 上的幻觉概率。

## 当前 AI 工程化配置

- `AGENTS.md`：仓库级 agent 协作规范。
- `docs/ai-agent-standards.md`：采用的开放实践说明。
- `scripts/export_dependency_context.py`：从 `pyproject.toml` 生成依赖上下文。
- `.ai/dependency-context.json`：可提交、可审查的机器可读上下文。
- `.github/copilot-instructions.md`：IDE 内 AI 助手一致性提示。
- `.editorconfig`：跨工具基础格式规范。

## 快速开始

```bash
python scripts/export_dependency_context.py
python scripts/export_dependency_context.py --check
python -m compileall .
```

## 设计说明

> 你提到的问题是“skill 往往不区分依赖版本，导致内容混乱”。

本仓库采用“生成式上下文工件”的方式：

1. 以 `pyproject.toml`（后续可扩展 lockfile）作为版本源。
2. 生成 `.ai/dependency-context.json`，供任何 agent 读取。
3. 在本地检查和 CI 中通过 `--check` 保证上下文不过期。

这样，AI 工具不需要依赖模糊记忆，而是读取项目自己的版本化事实。
