from __future__ import annotations

import random
import re
from datetime import datetime, timedelta, timezone

TOP_HASHTAGS = [
    "bluesky",
    "ai",
    "web3",
    "gaming",
    "music",
    "startups",
    "dataengineering",
    "design",
    "opensource",
    "crypto",
    "travel",
    "community",
]
LANGUAGES = ["en", "es", "fr", "ja", "de", "pt"]


def normalize_hashtag(raw_tag: str) -> str:
    """Keep hashtag text readable and simple for the dashboard."""
    cleaned = raw_tag.strip().lower()
    cleaned = re.sub(r"^#+", "", cleaned)
    cleaned = re.sub(r"[^a-z0-9]+", "", cleaned)
    return cleaned


def build_snapshot() -> dict:
    """Generate a realistic but lightweight live dashboard snapshot."""
    now = datetime.now(timezone.utc)
    base_posts = 840 + random.randint(0, 260)
    posts_per_minute = base_posts
    time_series = []
    for minute in range(12):
        point_time = now - timedelta(minutes=11 - minute)
        value = max(40, int(base_posts * (0.72 + (minute / 18)) + random.randint(-70, 140)))
        time_series.append({"time": point_time.isoformat(), "value": value})

    language_counts = {lang: max(35, random.randint(120, 620)) for lang in LANGUAGES}
    total_language = sum(language_counts.values())
    language_share = [
        {"label": lang, "value": round((count / total_language) * 100, 1)}
        for lang, count in sorted(language_counts.items(), key=lambda item: item[1], reverse=True)
    ]

    top_hashtags = []
    for tag in TOP_HASHTAGS:
        mention_count = random.randint(18, 280)
        change = random.randint(-30, 72)
        top_hashtags.append({
            "tag": tag,
            "mentions": mention_count,
            "change": change,
        })
    top_hashtags = sorted(top_hashtags, key=lambda item: item["mentions"], reverse=True)[:8]

    biggest_risers = []
    for tag in TOP_HASHTAGS[:5]:
        biggest_risers.append({
            "tag": tag,
            "baseline": random.randint(8, 80),
            "current": random.randint(40, 180),
            "ratio": round(random.uniform(1.4, 5.6), 2),
        })
    biggest_risers = sorted(biggest_risers, key=lambda item: item["ratio"], reverse=True)[:5]

    dlq_rate = round(random.uniform(0.0, 2.7), 2)
    lag_seconds = random.randint(3, 29)
    if lag_seconds > 18 or dlq_rate > 1.5:
        health = "warning"
    else:
        health = "healthy"
    if lag_seconds > 45 or dlq_rate > 3.0:
        health = "critical"

    snapshot = {
        "posts_per_minute": posts_per_minute,
        "time_series": time_series,
        "language_share": language_share,
        "top_hashtags": top_hashtags,
        "biggest_risers": biggest_risers,
        "health": {
            "status": health,
            "lag_seconds": lag_seconds,
            "dlq_rate": dlq_rate,
            "uptime_minutes": random.randint(90, 420),
            "alerts": random.randint(1, 6),
        },
        "signals": {
            "heat": "Rising fast",
            "focus": "AI + Web3 chatter is accelerating",
            "momentum": round(random.uniform(68, 95), 1),
        },
        "campaign": {
            "title": "Live spike radar",
            "subtitle": "Monitoring social energy across the firehose",
        },
    }
    return snapshot
