# PinPoint


## 需求

有没有一个工具互或skill，可以按项目配置的依赖版本下载或整理依赖的skill用法，比如我python项目pyproject.toml依赖了pydantic v2.0版本，这个工具帮我把这个版本的确定性内容生成适合ai阅读的接口、测试等索引，以便其不会幻觉瞎讲，我观察目前貌似市面上的很多skill或最佳实践skill都是没有版本，这样不混乱吗?

目前成气候的有点像这种需求的context7这个网站，他也只是一个skill的实时引擎，并没有按版本查找的功能.

感觉一个skill解决不了这个问题，可能需要一个工具，这个工具可以按项目配置的依赖版本下载或整理依赖的skill用法。

gemini --list-sessions
gemini --resume <index_number>\n