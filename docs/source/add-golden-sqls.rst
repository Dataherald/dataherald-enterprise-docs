Add Golden Queries Manually
===========================

Golden SQLs (or golden queries) are used by the AI model to generate more 
accurate SQL queries in response to questions asked by users. Generally, the 
more golden queries provided, the better the tool gets at answering questions 
in one shot.

Golden queries can be added in two different ways: admins can 
:doc:`validate-queries` or follow the below steps to add golden queries 
manually.

Steps
-----

Currently, to add Golden SQL queries, data admins will need to save them as 
*natural language <> SQL query* pairs in one of the following formats: .jsonl, 
.json, .csv, .xls, .xlsx. The following is an example of a JSON file with 
Golden SQLs.

.. code-block:: JSON

  { 
      "golden_records": [
          {
            "question": "<insert natural language question here>",
            "sql_query": "SELECT * FROM table_name;"
          },
          {
            "question": "<insert natural language question here>",
            "sql_query": "SELECT * FROM table_name;"
          }
      ]
  }

For now, data admins can send this file over to their Dataherald data support 
team.