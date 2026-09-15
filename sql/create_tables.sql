-- PostgreSQL schema for the learner-information Q1 analysis.
-- I will finalise the schema after reviewing the transformed data.

CREATE TABLE IF NOT EXISTS information_items (
    information_id INTEGER PRIMARY KEY,
    information_item TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS response_categories (
    response_category_id SERIAL PRIMARY KEY,
    response_category TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS q1_responses (
    response_id SERIAL PRIMARY KEY,
    information_id INTEGER NOT NULL REFERENCES information_items(information_id),
    response_category_id INTEGER NOT NULL REFERENCES response_categories(response_category_id),
    response_count INTEGER NOT NULL,
    percentage NUMERIC(5,2) NOT NULL,
    UNIQUE (information_id, response_category_id)
);
