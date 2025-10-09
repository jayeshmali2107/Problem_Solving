# Write your MySQL query statement below
select distinct products.product_id as product_id, ifnull(a.new_price,10) as price from products
left join

(select product_id,new_price from products
where (product_id,change_date) in

(select product_id, max(change_date) as change_date  from products
where change_date<='2019-08-16'
group by product_id)) a

on products.product_id=a.product_id