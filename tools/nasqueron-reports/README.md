## nasqueron-reports

The nasqueron_reports Python package allows to run the MariaDB or MySQL query,
and format the result as expected.

It's composed of a modular library in src/ and utilities in bin/.
 
### run-report
The `bin/run-report` tool is a full solution to connect to a specific data source,
fetch data and output it following a configuration.

Default configuration can be found in conf/ folder.

For example, `run-report agora-operations-grimoire-older-pages`
will connect to MariaDB, run query and format as MediaWiki table.

### sql-result-to-mediawiki-table

For one shot queries to produce wiki tables,
instead of adding a SQL query here and a configuration,
you can use `mysql ... | bin/sql-result-to-mediawiki-table`.

The tabulation is used as separator, so could be best to use
`mysql --raw --batch`, but that seems to work decently without them.
