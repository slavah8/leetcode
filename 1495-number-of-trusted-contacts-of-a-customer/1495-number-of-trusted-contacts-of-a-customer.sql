# Write your MySQL query statement below

WITH contacts_per_user AS (
    SELECT user_id, COUNT(*) AS contacts_count
    FROM Contacts
    GROUP BY user_id
),
trusted_per_user AS (
    SELECT c.user_id, COUNT(*) AS trusted_contacts_count
    FROM Contacts c
    JOIN Customers m 
    ON c.contact_email = m.email
    GROUP BY c.user_id
)

SELECT 
i.invoice_id, 
c.customer_name, 
i.price,
COALESCE(cu.contacts_count, 0) AS contacts_cnt,
COALESCE(tu.trusted_contacts_count, 0) AS trusted_contacts_cnt

FROM Invoices i
JOIN Customers c
  ON i.user_id = c.customer_id
LEFT JOIN contacts_per_user cu
  ON i.user_id = cu.user_id
LEFT JOIN trusted_per_user tu
  ON i.user_id = tu.user_id
ORDER BY invoice_id