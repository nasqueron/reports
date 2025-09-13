-- DevCentral
-- What revisions have the "Yo so serious" token awarded?
--
-- Notes:
--     This token allows to tag revisions where ChatGPT was useful.
--     {{D}} and {{Repo}} are MediaWiki templates used on Agora.
--
-- Published to https://agora.nasqueron.org/AI_content

SELECT
    CONCAT("{{D|", rev.id, "}}") as revision,
    title,
    DATE_FORMAT(FROM_UNIXTIME(rev.dateCreated), '%Y-%m-%d') as `date`,
    userName,
    CONCAT("{{Repo|", repositorySlug, "}}") as repository
FROM devcentral_differential.differential_revision rev
    LEFT JOIN devcentral_repository.repository repo ON repo.phid = rev.repositoryPHID
    LEFT JOIN devcentral_user.user ON user.phid = authorPHID
WHERE rev.phid IN (
    SELECT DISTINCT objectPHID
    FROM devcentral_token.token_given
    WHERE tokenPHID = "PHID-TOKN-emoji-3"
) AND repo.phid NOT IN (
    -- Ignored repositories for external non-Nasqueron projects
    "PHID-REPO-lfanwd5oj6hf7gmpzd2s"
)
ORDER BY rev.id DESC;
