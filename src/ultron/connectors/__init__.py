"""Data source connectors for Deep Research."""

from ultron.connectors._stubs import (
    Attachment,
    BaseConnector,
    Document,
    SyncStatus,
)
from ultron.connectors.store import KnowledgeStore

__all__ = ["Attachment", "BaseConnector", "Document", "KnowledgeStore", "SyncStatus"]

# Auto-register built-in connectors
import ultron.connectors.obsidian  # noqa: F401

try:
    import ultron.connectors.gmail  # noqa: F401
except ImportError:
    pass

try:
    import ultron.connectors.gmail_imap  # noqa: F401
except ImportError:
    pass

try:
    import ultron.connectors.gdrive  # noqa: F401
except ImportError:
    pass  # httpx may not be installed

try:
    import ultron.connectors.notion  # noqa: F401
except ImportError:
    pass

try:
    import ultron.connectors.granola  # noqa: F401
except ImportError:
    pass

try:
    import ultron.connectors.gcontacts  # noqa: F401
except ImportError:
    pass

try:
    import ultron.connectors.imessage  # noqa: F401
except ImportError:
    pass

try:
    import ultron.connectors.apple_notes  # noqa: F401
except ImportError:
    pass

try:
    import ultron.connectors.apple_music  # noqa: F401
except ImportError:
    pass

try:
    import ultron.connectors.apple_contacts  # noqa: F401
except ImportError:
    pass

try:
    import ultron.connectors.apple_calendar  # noqa: F401
except ImportError:
    pass

try:
    import ultron.connectors.slack_connector  # noqa: F401
except ImportError:
    pass

try:
    import ultron.connectors.outlook  # noqa: F401
except ImportError:
    pass

try:
    import ultron.connectors.imap  # noqa: F401
except ImportError:
    pass

try:
    import ultron.connectors.gcalendar  # noqa: F401
except ImportError:
    pass

try:
    import ultron.connectors.dropbox  # noqa: F401
except ImportError:
    pass  # httpx may not be installed

try:
    import ultron.connectors.whatsapp  # noqa: F401
except ImportError:
    pass

try:
    import ultron.connectors.oura  # noqa: F401
except ImportError:
    pass

try:
    import ultron.connectors.apple_health  # noqa: F401
except ImportError:
    pass

try:
    import ultron.connectors.strava  # noqa: F401
except ImportError:
    pass

try:
    import ultron.connectors.spotify  # noqa: F401
except ImportError:
    pass

try:
    import ultron.connectors.google_tasks  # noqa: F401
except ImportError:
    pass

try:
    import ultron.connectors.weather  # noqa: F401
except ImportError:
    pass

try:
    import ultron.connectors.github_notifications  # noqa: F401
except ImportError:
    pass

try:
    import ultron.connectors.hackernews  # noqa: F401
except ImportError:
    pass

try:
    import ultron.connectors.news_rss  # noqa: F401
except ImportError:
    pass
