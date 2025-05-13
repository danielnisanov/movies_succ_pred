import kagglehub
# import pandas as pd
import os
# import sqlite3
#
# # Step 1: Download dataset
# path = kagglehub.dataset_download("juzershakir/tmdb-movies-dataset")
# csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]
# csv_path = os.path.join(path, csv_files[0])
#
# # Step 2: Load CSV into DataFrame
# df = pd.read_csv(csv_path)
#
# # Step 3: Create SQLite database and connect
# db_path = os.path.join(path, "tmdb.sqlite")
# conn = sqlite3.connect(db_path)
#
# # Step 4: Save DataFrame to SQLite
# table_name = "movies"
# df.to_sql(table_name, conn, if_exists="replace", index=False)
#
# # Step 5: Verify by reading back
# result = pd.read_sql(f"SELECT * FROM {table_name} LIMIT 10;", conn)
# print(result)
#
# conn.close()
# print(f"✅ Data inserted into {db_path}")



import pandas as pd
import sqlite3  # אין צורך בהתקנה!

# Step 1: Download dataset
path = kagglehub.dataset_download("juzershakir/tmdb-movies-dataset")
csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]
csv_path = os.path.join(path, csv_files[0])

# Step 2: Load CSV into DataFrame
df = pd.read_csv(csv_path)

# df = pd.read_csv("tmdb_5000_movies.csv")

conn = sqlite3.connect("identifier.sqlite")
df.to_sql("movies", conn, if_exists="replace", index=False)

print(pd.read_sql_query("SELECT * FROM movies LIMIT 5", conn))
conn.close()
