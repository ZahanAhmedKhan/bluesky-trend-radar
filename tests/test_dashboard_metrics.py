from dashboard.simulator import build_snapshot, normalize_hashtag


def test_normalize_hashtag() -> None:
    assert normalize_hashtag("#AI") == "ai"
    assert normalize_hashtag("  #Ethereum  ") == "ethereum"
    assert normalize_hashtag("👀bluesky") == "bluesky"


def test_build_snapshot_has_expected_structure() -> None:
    snapshot = build_snapshot()

    assert snapshot["posts_per_minute"] >= 0
    assert snapshot["language_share"]
    assert snapshot["top_hashtags"]
    assert snapshot["health"]["lag_seconds"] >= 0
    assert snapshot["health"]["dlq_rate"] >= 0
    assert snapshot["health"]["status"] in {"healthy", "warning", "critical"}
