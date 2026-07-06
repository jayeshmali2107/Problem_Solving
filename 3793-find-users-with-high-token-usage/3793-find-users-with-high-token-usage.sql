# Write your MySQL query statement below
select user_id, count(prompt) as prompt_count, ROUND(AVG(tokens), 2) as avg_tokens
from prompts
group by user_id
having count(prompt) >= 3
AND COUNT(DISTINCT tokens) > 1
order by avg_tokens desc;