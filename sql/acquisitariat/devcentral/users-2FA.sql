-- DevCentral
-- Who still need to enable a second factor?

SELECT DISTINCT userName
FROM devcentral_project.edge
LEFT JOIN devcentral_user.user ON user.phid = edge.dst
WHERE src IN (
    "PHID-PROJ-2gmvzczbipg5amctzsjd", -- Trusted users
    "PHID-PROJ-puoemrjignrbd2eilwpo"  -- Ops
)
    AND type = 13                     -- project has member (PhabricatorProjectProjectHasMemberEdgeType)
    AND isSystemAgent = 0             -- avoid bot accounts like Alken-Orin
    AND isEnrolledInMultiFactor = 0
ORDER BY userName;
