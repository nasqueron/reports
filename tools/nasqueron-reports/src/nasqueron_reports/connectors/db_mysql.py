#   -------------------------------------------------------------
#   Nasqueron Reports :: Connectors :: MySQL
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Connect to MySQL or MariaDB
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


import mysql.connector
import sqlparse

from nasqueron_reports.config import resolve_sql_path
from nasqueron_reports.errors import *


#   -------------------------------------------------------------
#   Statements parser
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def clean_statement(statement):
    return sqlparse.format(statement, strip_comments=True).strip()


def split_statements(queries):
    return [clean_statement(stmt) for stmt in sqlparse.split(queries)]


def extract_database(query):
    if query.startswith("USE "):
        tokens = query.split()
        try:
            return tokens[1].rstrip(";")
        except IndexError:
            raise NasqueronReportQueryError("Malformed USE statement", query)

    raise NasqueronReportQueryError(
        "When a report query contains two statements, the first statement is expected to be USE.",
        query,
    )


def parse_statements(query):
    """Parse SELECT or USE; SELECT; statements.
    as a main SELECT query and a database."""
    statements = split_statements(query)

    n = len(statements)
    if n == 0:
        raise NasqueronReportQueryError("Empty query", query)
    if n > 2:
        raise NasqueronReportQueryError("Too many statements in query", query)

    if n == 1:
        query = statements[0]
        database = None
    else:
        query = statements[1]
        database = extract_database(statements[0])

    return query, database


#   -------------------------------------------------------------
#   Queries
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def run_query(query, db_config):
    query, database = parse_statements(query)

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    if database:
        conn.database = database

    cursor.execute(query)

    rows = cursor.fetchall()
    col_names = [desc[0] for desc in cursor.description]

    cursor.close()
    conn.close()

    return col_names, rows


#   -------------------------------------------------------------
#   Database configuration
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def get_db_config(config):
    args = config["service_options"]

    return {
        "host": args.get("hostname", "localhost"),
        "user": args["credentials"].get("username", ""),
        "password": args["credentials"].get("password", ""),
        "database": args.get("database", ""),
    }


#   -------------------------------------------------------------
#   Reports
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def fetch_report(config):
    query_path = resolve_sql_path(config["path"])
    with open(query_path, "r") as fd:
        query = fd.read()

    db_config = get_db_config(config)

    try:
        return run_query(query, db_config)
    except mysql.connector.Error as e:
        raise NasqueronReportDatabaseError(str(e))
