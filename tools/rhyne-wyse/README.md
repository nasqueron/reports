## Rhyne-Wyse

The Rhyne-Wyse package is a pywikibot automated agent to update the Agora wiki
with up-to-date reports.

### Usage

To manually run the agent, run `bin/update-agora-reports`.

To do so, you need a Vault/OpenBao token with correct permissions
to read report secrets.

### Configuration

The `conf/rhyne-wyse.yaml` file contains the configuration for the agent.

The reports section is a list of reports to update. For example:

```yaml
  - report: devcentral-token-language-models
    tool: fetch
    tool_options:
      url: https://docker-002.nasqueron.org/reports/devcentral-tokens-language-models.txt
    page: AI content
    tweaks:
      - compute-hash-ignoring-date
```

#### General options

The following options are available:

   - report: the name of the report to update
   - tool: the name of the tool to use to update the report
     - nasqueron-reports: Use the Nasqueron Reports package
     - fetch: fetch an already generated report at a specific URL  
   - tool_options: the options to pass to the tool
   - page: the wiki page to update
   - tweaks: a list of tweaks to decide when to update

#### Tool options

The tool options for the `nasqueron-reports` tool are:

   - vault_credentials: the path to the Vault/OpenBao credentials file

The tool options for the `fetch` tool are:

   - url: the URL to fetch the report from

#### Tweaks

The available tweaks are:

| Tweak                      | Description                                   |
|----------------------------|-----------------------------------------------|
| compute-hash-first-column  | Only check if first column changed            |
| compute-hash-ignoring-date | Ignoring the report date row                  |
| update-at-least-monthly    | Force update after 30 days                    |

To add a new tweak, logic is currently handled in the `needs_report_update` function
in `tasks/report.py`.
