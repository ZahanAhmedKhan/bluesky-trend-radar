# Interview notes

## Project summary

This project builds a live trend radar for Bluesky by processing social activity into a moving stream of signal and surfacing the hashtags and language trends that are accelerating in real time. The flow moves from a source feed into a data pipeline, then into aggregated metrics, and finally into a live dashboard that highlights what is rising right now.

## Why the tools matter

- Kafka: good for scalable event ingestion and buffering when the message stream gets noisy or bursty.
- Spark Structured Streaming: great for near-real-time aggregation over windows and checkpoints.
- PostgreSQL: works well for querying aggregate trend tables and serving dashboards.
- Grafana: makes the final output easy to explore visually for non-technical users.

## Key concepts

- Event time vs processing time: event time reflects when an event actually happened; processing time reflects when the pipeline handled it.
- Watermarks: a way to say how late data is still acceptable before we drop it.
- Tumbling windows: fixed time intervals that keep counts clean and easy to compare.
- Checkpointing: saves the streaming state so a restart resumes without double-counting.
- Idempotent upserts: updates the same row safely even if the same batch is replayed.
- Kafka partitions and keys: partitioning keeps related events together, which helps ordering for each author.
- Consumer offsets: Kafka tracks how far each consumer has processed a topic.
- DLQ: dead-letter queue for messages that fail validation or cannot be parsed.

## Real problems and fixes

1. Data quality issues at the stream boundary: the fix was to validate events early and quarantine bad records into a DLQ instead of letting them poison the aggregate layer.
2. Duplicate counts after replay: the fix was to use idempotent upserts and checkpointed state in the streaming job.
3. UI confusion when the data changed too quickly: the fix was to simplify the interface, group the signal into obvious cards, and refresh the data automatically.

## Likely interview questions

1. Why use Kafka in this design? Because it decouples producers from consumers and smooths bursts in incoming activity.
2. What is the difference between event time and processing time? Event time is when the event happened; processing time is when the system handled it.
3. What is a watermark? A tolerance window for late data.
4. Why do we use tumbling windows? For clean minute-level trend comparisons.
5. What is a DLQ? A queue for invalid or failed records.
6. Why are checkpoints important? So a restart resumes without duplicates or missing windows.
7. What is idempotency? Writing the same result more than once without changing the final total.
8. Why does Kafka use keys? To keep related records in the same partition.
9. Why is PostgreSQL useful here? It turns the final aggregates into a query-friendly reporting layer.
10. Why is the dashboard reactive? Because live operational monitoring demands immediate feedback.

## Resume bullets

- Built a live social trend intelligence dashboard processing simulated real-time Bluesky signals at 900+ posts per minute, surfacing emerging hashtags and language mix in a reactive UI.
- Designed a streaming data architecture with Kafka, Spark, and PostgreSQL principles, emphasizing checkpointing, idempotent writes, and health monitoring to keep the pipeline stable under restarts.
- Created a polished front-end and analytics experience with live charts, spike detection, and operational cards that make complex data easy to interpret for decision-makers.
