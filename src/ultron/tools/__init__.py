"""Tools primitive — tool system with ABC interface and built-in tools."""

from __future__ import annotations

from ultron.tools._stubs import BaseTool, ToolExecutor, ToolSpec

# Import built-in tools to trigger @ToolRegistry.register() decorators.
# Each is wrapped in try/except so the package loads even before the
# individual tool modules are created.
try:
    import ultron.tools.calculator  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.think  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.retrieval  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.llm_tool  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.file_read  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.web_search  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.weather  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.code_interpreter  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.code_interpreter_docker  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.repl  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.storage_tools  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.mcp_adapter  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.channel_tools  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.http_request  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.docker_shell_exec  # noqa: F401
    import ultron.tools.shell_exec  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.memory_manage  # noqa: F401
except ImportError:
    pass
try:
    import ultron.tools.user_profile_manage  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.skill_manage  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.file_write  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.apply_patch  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.git_tool  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.db_query  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.pdf_tool  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.image_tool  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.audio_tool  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.knowledge_tools  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.text_to_speech  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.digest_collect  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.scan_chunks  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.knowledge_sql  # noqa: F401
except ImportError:
    pass

try:
    import ultron.tools.apple_calendar  # noqa: F401
except ImportError:
    pass

__all__ = ["BaseTool", "ToolExecutor", "ToolSpec"]
