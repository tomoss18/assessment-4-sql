### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
  A free open-source database management system emphasizing extensibility and SQL compliance.

- What is the difference between SQL and PostgreSQL?
  PostgreSQL is object-relational and SQL is server relational.

- In `psql`, how do you connect to a database?
  In order to connect to a database you need to know the name of your target database, the host name and port number of the server, and what user name you want to connect as.

- What is the difference between `HAVING` and `WHERE`?
  HAVING applies to groups as a whole and WHERE applies to individual rows.

- What is the difference between an `INNER` and `OUTER` join?
  Inner join will keep only the information from both tables that's related to each other (in the resulting table). An Outer Join, on the other hand, will also keep information that is not related to the other table in the resulting table.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
Left outer join includes the unmatched rows from the table which is on the left of the join clause whereas a Right outer join includes the unmatched rows from the table which is on the right of the join clause.

- What is an ORM? What do they do?
  An object-relational mapper provides an object-oriented layer between relational databases and object-oriented programming languages without having to write SQL queries. It standardizes interfaces reducing boilerplate and speeding development

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
  An AJAX request is identical to a "normal" browser request as far as the server is concerned other than potentially slightly different HTTP headers. e.g. chrome sends:

- What is CSRF? What is the purpose of the CSRF token?
A CSRF token is a secure random token (e.g., synchronizer token or challenge token) that is used to prevent CSRF attacks.

- What is the purpose of `form.hidden_tag()`?
The form. hidden_tag() template argument generates a hidden field that includes a token that is used to protect the form against CSRF attacks.