-- ==========================================
-- Learner Survey Data - Analytical Queries
-- ==========================================

-- 1. Overall Usefulness Breakdown
SELECT 
    response_category_id,
    SUM(response_count) AS total_responses,
    ROUND(CAST(AVG(percentage) AS numeric), 2) AS average_percentage
FROM q1_responses
GROUP BY response_category_id
ORDER BY total_responses DESC;

-- 2. Top Information Items Rated "Very Useful"
SELECT 
    ii.information_item AS information_item,
    qr.percentage AS very_useful_percentage
FROM q1_responses qr
JOIN information_items ii ON qr.information_id = ii.information_id
JOIN response_categories rc ON rc.response_category_id = qr.response_category_id
WHERE rc.response_category = 'Very useful'
ORDER BY qr.percentage DESC;

-- 3. Identifying Areas of Dissatisfaction ("Not Useful" Summary)
SELECT 
    ii.information_item AS information_item,
    SUM(qr.response_count) AS total_negative_responses
FROM q1_responses qr
JOIN information_items ii ON qr.information_id = ii.information_id
JOIN response_categories rc ON qr.response_category_id = rc.response_category_id
WHERE rc.response_category IN ('Not particularly useful', 'Not useful at all')
GROUP BY ii.information_item
ORDER BY total_negative_responses DESC;

-- 4. Highlighting Uncertainty ("Don't Know" Responses)
SELECT 
    ii.information_item AS information_item,
    qr.response_count AS dont_know_count,
    qr.percentage AS dont_know_percentage
FROM q1_responses qr
JOIN information_items ii ON qr.information_id = ii.information_id
JOIN response_categories rc ON qr.response_category_id = rc.response_category_id
WHERE rc.response_category = 'Don''t know'
ORDER BY qr.percentage DESC;