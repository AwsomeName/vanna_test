from vanna.openai.openai_chat import OpenAI_Chat
from vanna.chromadb.chromadb_vector import ChromaDB_VectorStore
class MyVanna(ChromaDB_VectorStore, OpenAI_Chat):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        OpenAI_Chat.__init__(self, config=config)

vn = MyVanna(config={'api_key': 'sk-...', 'model': 'gpt-4-...'})

vn.train(ddl="""    CREATE TABLE IF NOT EXISTS my-table (        id INT PRIMARY KEY,        name VARCHAR(100),        age INT    )""")

vn.train(sql="SELECT name, age FROM my-table WHERE name = 'John Doe'")

vn.ask("What are the top 10 customers by sales?")