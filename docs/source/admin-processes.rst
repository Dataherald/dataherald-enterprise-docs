Admin Processes
======================

.. _validating-responses:

Validating Responses to User Questions
-----------
#. Once a user asks a question through the Dataherald AI Slackbot, it will show up on the admin console (the list is sorted by the *Time* column by default, so the latest questions will be on top). It will have one of the following statuses: High Confidence, Medium Confidence, Low Confidence, or SQL Error.
#. The data admin should click on the row, opening up the detailed view.
#. The SQL query generated to answer the question will be in the **SQL text editor**, with the question asked listed above in the **Header**. Data admins can copy-paste it in the execution context of their data warehouse to test it, or fix the query right there in the editor and run it.

   * Please follow the Best Practices for Writing SQL Queries to more effectively train the SQL generator.
   * After running the query, the natural language response generated will automatically appear in the **Slack response panel**.

#. Once the data admin is satisfied with the query and response, the data admin can Mark as Verified and click on “Save”. This will save the query as a Golden Query and will be used to improve the quality of future generated queries. A response will be sent to the user who asked the question through the Slackbot.

.. _adding-golden-sqls:

Adding Verified Golden SQL Queries
-------------
Currently, to add Golden SQL queries, data admins will need to save them as *natural language <> SQL query* pairs in one of the following formats: .jsonl, .json, .csv, .xls, .xlsx. The following is an example of a JSON file with Golden SQLs.

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

For now, data admins can send this file over to their Dataherald data support team.