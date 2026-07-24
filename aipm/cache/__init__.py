from .manager import cache_manager

__all__ = [
    "cache_manager",
]
def __init__(self):

    cfg = load_config()

    self.path = (
        cfg.storage.root
        / "cache.json"
    )

    self.log = get_logger(
        __name__
    )