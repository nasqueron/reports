#   -------------------------------------------------------------
#   Rhyne-Wyse :: Tasks :: Wiki
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


from typing import Dict

import pywikibot

from rhyne_wyse.tasks.reports import prepare_report, needs_report_update
from rhyne_wyse.wiki.page import update_text_with_new_report


def publish_report(site, title, content, comment):
    page = pywikibot.Page(site, title)
    page.text = update_text_with_new_report(page.text, content)
    page.save(summary=comment, minor=False, bot=True)


def update_report(site, logger, report_options: Dict):
    report = prepare_report(report_options)

    tweaks = report_options.get("tweaks", [])

    if needs_report_update(site, report_options["page"], report, tweaks):
        comment = "[wiki.update_report] Update report " + report_options["report"]

        logger.info(comment)
        publish_report(site, report_options["page"], report.formatted, comment)
    else:
        logger.info(
            f"[wiki.update_report] Report {report_options['report']} is up to date."
        )
