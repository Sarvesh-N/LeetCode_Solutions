# Write your MySQL query statement below
select * from Patients
where conditions LIKE '%DIAB1%' and conditions not like '%SADIAB100%' and conditions not like '%ACNE +DIAB100%'
