"""Tiny text helpers used by the RepoDoctor demo."""


def word_count(text: str) -> int:
    return len(text.split())


def truncate(text: str, max_len: int, suffix: str = "...") -> str:
    """Shorten text to at most max_len characters, ending with suffix if it was cut."""
    if len(text) <= max_len:
        return text
    return text[: max_len - len(suffix)] + suffix


def title_case(text: str) -> str:
    return " ".join(word.capitalize() for word in text.split())
