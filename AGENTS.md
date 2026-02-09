# AGENTS.md

本仓库工具用于优化与智能体协作（Gemini CLI, qwen-code, Codex等）, 通过对依赖类库的版本的分析，生成确定性版本的知识库, 帮助智能体获得准确的参考知识, 避免智能体在依赖类库版本上的不确定性.

## 目标
- 同步项目的固定版本依赖的知识库。
- 生成所有依赖的知识库索引`.ai/dependency-context.json`, 格式为json, 包含项目元数据, 声明的依赖, 可选的锁定版本, 生成时间戳等信息。
- 生成每个依赖多层级具体文档, `index.md`包括类库的模块列表/接口列表/命令行接口, `module-<module-name>.md`包括每个模块的详细信息, 如函数/类/方法的签名, 参数, 返回值,  异常, 示例等.

## 智能体标准工作流
1. 阅读 `README.md` 和 `docs/ai-agent-standards.md`。
2. 依赖变更后运行 `python scripts/export_dependency_context.py`。
3. 如果依赖图或锁定文件发生变化，更新 `.ai/dependency-context.json`。
4. 提交前验证本地检查。

## 护栏
- 当存在依赖上下文时，不要凭记忆臆造 API。
- 优先引用 `.ai/dependency-context.json` 中生成的上下文。
- 使用 Conventional Commits 风格进行小型、可审查的提交。

## 必需检查
- `python -m compileall .`
- `python scripts/export_dependency_context.py --check`
