# MCP Quickstart Server

A small MCP server based on the [quickstart](https://modelcontextprotocol.io/quickstart/server), which retrieves information
from the Red Hat Status Page.

Why? So I can learn how it works, mainly.

Assisted by Gemini 2.5 Flash, via Continue.dev.

## Example Conversation

Via Gemini CLI:

```
╭──────────────────────────────────────────────────────────────────────────╮
│  > get everything from red hat status between the start of july and now  │
╰──────────────────────────────────────────────────────────────────────────╯

✦ I'm sorry, but I am unable to get events from a specific date range. I can, however, get all events
  and you can inspect them.
 ╭────────────────────────────────────────────────────────────────────────────────────────────╮
 │ ✔  get_all_events (Red Hat Status MCP Server) {}                                           │
 │                                                                                            │
 │    ... first 255 lines hidden ...                                                          │
 │                                                                                            │
 │    Jun  3, 21:27 UTC                                                                       │
 │    **Scheduled** - The Red Hat Hybrid Cloud Console will undergo a DB upgrade for          │
 │    ---                                                                                     │
 │    Title: Ansible Lightspeed Degraded Performance                                          │
 │    Timestamp: Tue, 03 Jun 2025 02:53:07 +0000                                              │
 │    Link: https://status.redhat.com/incidents/pjc3rd34c96h                                  │
 │                                                                                            │
 │    Description: Jun  3, 02:53 UTC                                                          │
 │    **Resolved** - This incident has been resolved.                                         │
 │                                                                                            │
 │    Jun  2, 11:13 UTC                                                                       │
 │    **Investigating** - We are currently investigating this issue.                          │
 │    ---                                                                                     │
 │    Title: Hybrid Cloud Console quickstarts database maintenance 2025-06-02                 │
 │    Start: Mon, 02 Jun 2025 13:00:21 +0000                                                  │
 │    End: Mon, 02 Jun 2025 13:00:00 +0000                                                    │
 │    Link: https://status.redhat.com/incidents/1kfdvglnj83p                                  │
 │                                                                                            │
 │    Description: Jun  2, 13:00 UTC                                                          │
 │    **Completed** - The scheduled maintenance has been completed.                           │
 │                                                                                            │
 │    Jun  2, 10:00 UTC                                                                       │
 │    **In progress** - Scheduled maintenance is currently in progress. We will provide       │
 │    updates as necessary.                                                                   │
 │                                                                                            │
 │    May 28, 06:00 UTC                                                                       │
 │    **Scheduled** - The Red Hat Hybrid Cloud Console will undergo routine maintenance for   │
 │    ---                                                                                     │
 │    Title: Developers.redhat.com - Homepage Outage                                          │
 │    Timestamp: Fri, 30 May 2025 20:37:43 +0000                                              │
 │    Link: https://status.redhat.com/incidents/gb5036tz802k                                  │
 │                                                                                            │
 │    Description: May 30, 20:37 UTC                                                          │
 │    **Resolved** - This incident has been resolved.                                         │
 │                                                                                            │
 │    May 30, 17:00 UTC                                                                       │
 │    **Investigating** - We are currently investigating this issue.                          │
 │    ---                                                                                     │
 │    Title: access.redhat.com - Support Cases  and Ask Outage                                │
 │    Timestamp: Sat, 24 May 2025 11:27:05 +0000                                              │
 │    Link: https://status.redhat.com/incidents/jyhlnt4t9bq5                                  │
 │                                                                                            │
 │    Description: May 24, 11:27 UTC                                                          │
 │    **Resolved** - This incident has been resolved.                                         │
 │                                                                                            │
 │    May 24, 10:02 UTC                                                                       │
 │    **Investigating** - We are currently investigating this issue.                          │
 │    ---                                                                                     │
 │    Title: 500 Internal Server Error When Reading Signatures                                │
 │    Timestamp: Sat, 17 May 2025 15:16:29 +0000                                              │
 │    Link: https://status.redhat.com/incidents/f7bb48x609yk                                  │
 │                                                                                            │
 │    Description: May 17, 15:16 UTC                                                          │
 │    **Resolved** - This incident has been resolved.                                         │
 │                                                                                            │
 │    May 17, 15:10 UTC                                                                       │
 │    **Identified** - The issue has been identified and a fix is being implemented.          │
 │                                                                                            │
 │    May 17, 13:07 UTC                                                                       │
 │    **Investigating** - We are currently investigating this issue.                          │
 │    ---                                                                                     │
 │    Title: Partner Portal Outage                                                            │
 │    Timestamp: Thu, 15 May 2025 23:39:41 +0000                                              │
 │    Link: https://status.redhat.com/incidents/jwh5rrmqvx09                                  │
 │                                                                                            │
 │    Description: May 15, 23:39 UTC                                                          │
 │    **Resolved** - This incident has been resolved.                                         │
 │                                                                                            │
 │    May 15, 21:38 UTC                                                                       │
 │    **Update** - We are continuing to investigate this issue.                               │
 │                                                                                            │
 │    May 15, 21:34 UTC                                                                       │
 │    **Investigating** - We are currently investigating this issue.                          │
 │                                                                                            │
 │    May 15, 21:34 UTC                                                                       │
 │    **Identified** - The issue has been identified and a fix is being implemented.          │
 │    ---                                                                                     │
 │    Title: Quay.io Push Unavailable                                                         │
 │    Timestamp: Tue, 13 May 2025 22:09:08 +0000                                              │
 │    Link: https://status.redhat.com/incidents/k7kvfvgfrbdf                                  │
 │                                                                                            │
 │    Description: May 13, 22:09 UTC                                                          │
 │    **Resolved** - A fix has been deployed and Pushes are restored.                         │
 │                                                                                            │
 │    May 13, 10:31 UTC                                                                       │
 │    **Update** - Quay.io has been moved to read-only mode while we work to implement a      │
 │    fix. During this time Pulls will continue to work, however, Pushes will be disabled     │
 │    until a fix is implemented. There is currently no timeline for Push restoration.        │
 │                                                                                            │
 │    May 13, 09:12 UTC                                                                       │
 │    **Identified** - The issue has been identified. A primary key in the database has       │
 │    reached maximum value. We are currently working on validating a fix.                    │
 │                                                                                            │
 │    May 13, 08:45 UTC                                                                       │
 │    **Investigating** - We are currently investigating this issue.                          │
 │    ---                                                                                     │
 │    Title: Access.redhat.com & Catalog.redhat.com Partial outage                            │
 │    Timestamp: Thu, 08 May 2025 19:08:08 +0000                                              │
 │    Link: https://status.redhat.com/incidents/qzz9knn1k8j6                                  │
 │                                                                                            │
 │    Description: May  8, 19:08 UTC                                                          │
 │    **Resolved** - We identified and resolved a issue relating to a release of a new        │
 │    application. The change impacted some paths on access.redhat.com and the sigstore for   │
 │    container pulls on catalog.redhat.com. A fix was pushed at May 8, 2025, 05:05:05 AM     │
 │    UTC                                                                                     │
 ╰────────────────────────────────────────────────────────────────────────────────────────────╯
✦ Here are all the events from Red Hat Status that have occurred in July up to today, July 18th, 2025:

  Hybrid Cloud Console Inventory DB Maintenance 2025-07-17 2
   * Start: Fri, 18 Jul 2025 21:00:21 +0000
   * End: Fri, 18 Jul 2025 21:00:00 +0000
   * Description: The Inventory service is still experiencing degraded performance following the
     recent maintenance window. Our team is actively working through a backlog, and we expect data
     inconsistencies to be resolved by Friday, July 18, 2025, at 5:00 PM ET.

  Hybrid Cloud Console Inventory DB Maintenance 2025-07-18
   * Start: Fri, 18 Jul 2025 21:01:21 +0000
   * End: Sat, 19 Jul 2025 21:00:00 +0000
   * Description: The Inventory service is still experiencing degraded performance following the
     recent maintenance window. Our team is actively working through a backlog, and we expect data
     inconsistencies to be resolved by Saturday, July 19, 2025, at 5:00 PM ET.

  OCM database maintenance
   * Start: Thu, 17 Jul 2025 17:21:21 +0000
   * End: Thu, 17 Jul 2025 17:21:00 +0000
   * Description: The OpenShift Cluster Manager will undergo maintenance work to make infrastructure
     improvements. The maintenance will start on Thursday, July 17th at 17:06 UTC and may last up to
     15 min.

  Hybrid Cloud Console Inventory DB Maintenance 2025-07-15
   * Start: Tue, 15 Jul 2025 21:00:21 +0000
   * End: Tue, 15 Jul 2025 21:00:00 +0000
   * Description: Hybrid Cloud Console Inventory is undergoing maintenance for database updates on
     Tuesday, July 15 from 12:00 UTC to 21:00 UTC. During this window, Inventory systems and
     workspaces will be read-only.

  repository.jboss.org outage
   * Timestamp: Tue, 15 Jul 2025 21:11:00 +0000
   * Description: An underlying database issue has been identified and is working to be resolved.

  https://repository.jboss.org
   * Start: Sat, 12 Jul 2025 16:15:21 +0000
   * End: Sat, 12 Jul 2025 16:15:00 +0000
   * Description: https://repository.jboss.org will go down for a scheduled maintenance, estimated
     time to finish the migration 30 minutes

  HCP Installations and uninstallations are delayed for some clusters
   * Timestamp: Tue, 08 Jul 2025 16:08:32 +0000
   * Description: Provisioning of new ROSA HCP (Red Hat OpenShift Service on AWS with Hosted Control
     Planes) clusters is currently blocked for all versions.

  Quay.io 403s affecting image operations
   * Timestamp: Tue, 01 Jul 2025 20:05:22 +0000
   * Description: A fix has been implemented that reverts a recent configuration change to the web
     application firewall.
```