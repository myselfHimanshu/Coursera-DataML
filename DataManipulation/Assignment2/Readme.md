# SQL For Data Science

Use the command line to complete this assignment.<br />
- sqlite3 reuters.db < sql_filename :<br /> 
  execute the queries in the file sql_filenameagainst the database reuters.db.<br /> 
  This command assumes reuters.db and sql_filename are in your current directory.
  
Problem 1: Inspecting the Reuters Dataset and Basic Relational Algebra

(a) select: Write a query that is equivalent to the following relational algebra expression.

σdocid=10398_txt_earn(frequency)

(b) select project: Write a SQL statement that is equivalent to the following relational algebra expression.

πterm(σdocid=10398_txt_earn and count=1(frequency))

(c) union: Write a SQL statement that is equivalent to the following relational algebra expression. (Hint: you can use the UNION keyword in SQL)

πterm(σdocid=10398_txt_earn and count=1(frequency)) U πterm(σdocid=925_txt_trade and count=1(frequency))

(d) count: Write a SQL statement to count the number of unique documents containing the word "law" or containing the word "legal" (If a document contains both law and legal, it should only be counted once)

(e) big documents Write a SQL statement to find all documents that have more than 300 total terms, including duplicate terms. (Hint: You can use the HAVING clause, or you can use a nested query. Another hint: Remember that the count column contains the term frequencies, and you want to consider duplicates.) (docid, term_count)

(f) two words: Write a SQL statement to count the number of unique documents that contain both the word 'transactions' and the word 'world'. (Hint: Find the docs that contain one word and the docs that contain the other word separately, then find the intersection.)

Problem 2: Matrix Multiplication in SQL

Problem 3: Working with a Term-Document Matrix
