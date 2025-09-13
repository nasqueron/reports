#   -------------------------------------------------------------
#   Nasqueron Reports :: Formats :: MediaWiki
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Format report as MediaWiki table
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


from datetime import date


def read_as_str(value):
    if type(value) == bytes:
        return value.decode()

    return str(value)


def to_row(row):
    return ["|-", "| " + " || ".join(read_as_str(val) for val in row)]


def to_rows(rows):
    mediawiki_rows = [to_row(row) for row in rows]
    return [line for lines in mediawiki_rows for line in lines]


def to_table(columns_names, rows, options):
    """Format query result as MediaWiki table."""
    today = date.today().isoformat()
    lines = ['{| class="wikitable sortable"', f"|+ {today} report", "|-"]

    columns_map = options.get("cols", {})
    headers = [columns_map.get(c, c) for c in columns_names]
    lines.append("! " + " !! ".join(headers))

    lines.extend(to_rows(rows))

    lines.append("|}")

    return "\n".join(lines)
