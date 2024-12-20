import psycopg2
import argparse

def connect_to_db(host: str, port: int, dbname: str, user: str, password: str):
    """Establishes a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            host=host, port=port, dbname=dbname, user=user, password=password
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        exit(1)


def search_columns(conn, search_term: str, omit: bool, verbose: bool):
    """Searches for columns containing the search term in all databases, schemas, and tables."""
    cursor = conn.cursor()

    query = """
    SELECT table_catalog, table_schema, table_name, column_name
    FROM information_schema.columns
    WHERE column_name ILIKE %s;
    """

    cursor.execute(query, (f"%{search_term}%",))

    results = cursor.fetchall()

    for result in results:
        # The result returns in the order: database, schema, table, column
        if omit:
            result = result[1:]

        full_path = ".".join(result)

        if verbose:
            print("-------------")
            if omit:
                full_path = f"{full_path}. (Schema: {result[0]}, TableName: {result[1]}, Column: {result[2]}"
            else:
                full_path = f"{full_path}. (Database: {result[0]}, Schema: {result[1]}, TableName: {result[2]}, Column: {result[3]}"

        print(full_path)

    cursor.close()


def main():
    # Set up argument parsing for CLI inputs
    parser = argparse.ArgumentParser(
        description="Search for column names in PostgreSQL databases."
    )
    parser.add_argument("--host", required=True, help="PostgreSQL host")
    parser.add_argument("--port", required=True, help="PostgreSQL port")
    parser.add_argument("--dbname", required=True,
                        help="PostgreSQL database name")
    parser.add_argument("--user", required=True, help="PostgreSQL username")
    parser.add_argument("--password", required=True,
                        help="PostgreSQL password")
    parser.add_argument("--search", required=True,
                        help="Search term for column name")
    parser.add_argument(
        "--verbose", required=False, help="More detailed view for each result"
    )
    parser.add_argument("--omit", required=False, help="Omit the database name")

    args = parser.parse_args()

    # Establish database connection
    conn = connect_to_db(args.host, args.port, args.dbname,
                         args.user, args.password)

    # Search for columns
    search_columns(conn, args.search, args.omit, args.verbose)

    # Close the connection
    conn.close()


if __name__ == "__main__":
    main()
