CREATE OR REPLACE VIEW v_top_hashtags_15m AS
SELECT
    hashtag,
    SUM(mention_count) AS mention_count,
    MAX(window_start) AS last_window_start
FROM hashtag_mentions
WHERE window_start >= NOW() - INTERVAL '15 minutes'
GROUP BY hashtag
ORDER BY mention_count DESC;

CREATE OR REPLACE VIEW v_pipeline_health AS
SELECT
    NOW() AS observed_at,
    0 AS rows_per_minute,
    0 AS dlq_count,
    NOW() AS newest_event_time,
    0 AS latency_seconds;
