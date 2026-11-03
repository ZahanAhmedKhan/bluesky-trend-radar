CREATE TABLE IF NOT EXISTS posts_per_minute (
    window_start TIMESTAMPTZ NOT NULL,
    language TEXT NOT NULL,
    post_count INTEGER NOT NULL,
    PRIMARY KEY (window_start, language)
);

CREATE TABLE IF NOT EXISTS hashtag_mentions (
    window_start TIMESTAMPTZ NOT NULL,
    hashtag TEXT NOT NULL,
    mention_count INTEGER NOT NULL,
    PRIMARY KEY (window_start, hashtag)
);

CREATE TABLE IF NOT EXISTS spike_events (
    spike_id SERIAL PRIMARY KEY,
    hashtag TEXT NOT NULL,
    window_start TIMESTAMPTZ NOT NULL,
    score NUMERIC NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
