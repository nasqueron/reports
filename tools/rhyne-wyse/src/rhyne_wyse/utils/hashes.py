#   -------------------------------------------------------------
#   Rhyne-Wise :: Utilities :: Hashes
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


import hashlib
import re
from pathlib import Path
from typing import List

from nasqueron_reports import Report
from nasqueron_reports.formats.mediawiki import read_as_str

from rhyne_wyse.config import get_hashes_path

#   -------------------------------------------------------------
#   Compute hashes
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


REPORT_DATE_RE = r"\d{4}-\d{2}-\d{2} report"


def compute_hash_ignoring_date(report: Report) -> str:
    if report.raw.rows is None:
        content = [
            line
            for line in report.formatted.splitlines()
            if not re.search(REPORT_DATE_RE, line)
        ]
        return compute_hash_from(content)
    else:
        return compute_hash_from(report.raw.rows)


def compute_hash_from_first_column(report: Report) -> str:
    if report.raw.rows is None:
        raise ValueError(
            "compute-hash-first-column is not supported when raw report is unavailable"
        )

    content = [read_as_str(row[0]) for row in report.raw.rows]
    return compute_hash_from(content)


def compute_hash_from(content: List[str]) -> str:
    """Compute SHA-256 hash from a list of strings."""
    h = hashlib.sha256()

    for line in content:
        h.update(line.encode("utf-8"))
        h.update(b"\0")  # separator to avoid accidental concatenation collisions

    return h.hexdigest()


#   -------------------------------------------------------------
#   Hashes datastore
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def key_to_filename(key: str) -> Path:
    """Convert wiki page title to safe filename for hash storage."""
    safe = key.replace("/", "__").replace(" ", "_")

    return Path(get_hashes_path(), f"{safe}.sha256")


def read_hash_from_datastore(key: str) -> str | None:
    """Read a hash for a given key from its file."""
    path = key_to_filename(key)

    if not path.exists():
        return None

    return path.read_text(encoding="utf-8").strip()


def write_hash_to_datastore(key: str, hash_to_write: str):
    """Write a hash for a given key to its file."""
    path = key_to_filename(key)

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(hash_to_write + "\n", encoding="utf-8")
