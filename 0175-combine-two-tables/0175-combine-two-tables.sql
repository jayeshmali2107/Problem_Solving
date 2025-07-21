select p.firstName,p.lastName,o.city,o.state
from Person as p
left join Address as o on p.personId = o.personId;
