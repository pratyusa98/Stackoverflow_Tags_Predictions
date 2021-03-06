## StackOverflow-Tag-prediction
Problem: Given the Title and body of a question on Stack overflow, predict the tags associated with the question.

### Business Problem
Stack Overflow is the largest, most trusted online community for developers to learn, share their programming knowledge, and build their careers.

Stack Overflow is something which every programmer use one way or another. Each month, over 50 million developers come to Stack Overflow to learn, share their knowledge, and build their careers. It features questions and answers on a wide range of topics in computer programming. The website serves as a platform for users to ask and answer questions, and, through membership and active participation, to vote questions and answers up or down and edit questions and answers in a fashion similar to a wiki or Digg. As of April 2014 Stack Overflow has over 4,000,000 registered users, and it exceeded 10,000,000 questions in late August 2015. Based on the type of tags assigned to questions, the top eight most discussed topics on the site are: Java, JavaScript, C#, PHP, Android, jQuery, Python and HTML.

### Data Source: https://data.stackexchange.com/stackoverflow/query/edit/1186275#resultSets
##### Query: SELECT TOP 5000 Id, Title, Body , Tags from Posts WHERE Title IS NOT NULL AND Body IS NOT NULL ORDER BY RAND()
