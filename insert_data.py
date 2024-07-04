import psycopg2

def insert(question, answer):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            database="FlaskOpenAIQA",
            user="postgres",
            password="admin123",
            host="localhost",
            port="5432"
        )

        cur = conn.cursor()

        # Insert data into QA_table
        cur.execute('INSERT INTO "QA_table"(question, answer) VALUES (%s, %s)', (question, answer))
        conn.commit()

        # Fetch and print all rows from QA_table
        cur.execute('SELECT * FROM "QA_table"')
        rows = cur.fetchall()
        
        ## print all rows of the QA_table
        # for row in rows:
        #     print("ID : ", row[0])
        #     print("Question : ", row[1])
        #     print("Answer : ", row[2])
        #     print("\n")

        print("INSERT query executed")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        if conn:
            cur.close()
            conn.close()

# # Example usage
# insert('What is AI?', 'AI stands for Artificial Intelligence.')
# insert('What is Python?', 'Python is a programming language.')
