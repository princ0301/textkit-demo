from textkit import title_case, truncate, word_count


def test_word_count():
    assert word_count("a b  c") == 3


def test_title_case():
    assert title_case("hello big world") == "Hello Big World"


def test_truncate_short_text_unchanged():
    assert truncate("hi", 10) == "hi"


def test_truncate_long_text():
    assert truncate("hello world", 8) == "hello..."
