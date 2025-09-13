## Internal reports

Reports about Nasqueron internal data.

This repository can host:

  - SQL queries to get report data
  - Tools to produce reports

### SQL queries

Queries are organized by cluster/server name, then by service:

  - acquisitariat/ contains the queries for MySQL Docker container
    used by dev & community services like DevCentral

### Tools

Tools and utilities to work with reports are located in the tools/ folder:

* **[nasqueron-reports](tools/nasqueron-reports/README.md)**: 
  allows to run the MariaDB or MySQL query, 
  and format the result as expected, e.g. as MediaWiki table

### Contribute

This repository is intended to behave as a monorepo for reporting.

You can so add any project to generate or use a report at Nasqueron here,
regardless of the choice of technology stack.

Software in tools/<name of the project> are intended to be built autonomously.
