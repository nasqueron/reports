#   -------------------------------------------------------------
#   Rhyne-Wise :: Wiki :: Page
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Helper functions to interact with pages on the wiki
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


from enum import Enum
import time

import pywikibot


#   -------------------------------------------------------------
#   Page metadata
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def get_page_age(site, page_title: str) -> int:
    """Get the age of a page from the site; unit is days."""
    page = pywikibot.Page(site, page_title)

    unix_timestamp = page.latest_revision.timestamp.posix_timestamp()
    age_seconds = time.time() - unix_timestamp
    age_days = age_seconds / 86400

    return int(age_days)


#   -------------------------------------------------------------
#   Reports
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


REPORT_START = "<!-- Report start -->"
REPORT_END = "<!-- Report end -->"


class Position(Enum):
    BEFORE_MARKER = 1
    INSIDE_MARKERS = 2
    AFTER_MARKER = 3


def update_text_with_new_report(current_text: str, report: str) -> str:
    return replace_between_markers(current_text, REPORT_START, REPORT_END, report)


def replace_between_markers(
    page_text: str, marker_start: str, marker_end: str, new_inner_text: str
) -> str:
    """
    Replace the text between marker_start and marker_end (markers themselves stay)
    Returns the new page text. Raises ValueError when markers are not found.
    """
    position = Position.BEFORE_MARKER
    new_lines = []

    for line in page_text.splitlines():
        if position == Position.BEFORE_MARKER:
            new_lines.append(line)

            if marker_start in line:
                position = Position.INSIDE_MARKERS
                new_lines.append(new_inner_text)
                new_lines.append(marker_end)

            continue

        if position == Position.INSIDE_MARKERS:
            if marker_end in line:
                position = Position.AFTER_MARKER

            continue

        if position == Position.AFTER_MARKER:
            new_lines.append(line)

    if position == Position.BEFORE_MARKER:
        raise ValueError(f"Opening marker not found: {marker_start}")

    if position == Position.INSIDE_MARKERS:
        raise ValueError(f"Closing marker not found: {marker_end}")

    return "\n".join(new_lines) + "\n"  # EOL at EOF
