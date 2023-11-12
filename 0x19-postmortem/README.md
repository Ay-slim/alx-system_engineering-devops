## My First Postmoterm
This is a report of a postmoterm that occurred at a startup I worked with
### Issue Summary
Duration:
 The outage lasted from 9:00am UTC to around 2:00pm UTC when the system was restored to perfect working conditions.
Impact:
It was a complete outage preventing all customers from accessing the app 
Root cause:
It was caused by insufficiently strict DB security protocols

### Timeline
- At about half past 9, operations staff notified the team that their customers were unable to access the platform and they (the ops guys) were not able to view it either
- Engineering tried to recreate the problem by making DB calls and testing, and we realized there was no data on the production DB! Any engineering team's worst nightmare.
- An emergency alert was shared on Slack and the whole team got on a call to figure out what had gone wrong
- The initial assumption was that we were under attack from hackers who had somehow gotten into the system and dropped our production Database
- 30 minutes into figuring out what vulnerability had allowed this attack, a senior engineer with root access to the DB realized he had inadvertently dropped the DB while trying to do a local setup unknowingly using production credentials (root user)
- The issue was escalated to the engineering team as a whole
- The incident was resolved by restoring the last database snapshot that had been stored on a replica and migrating the data back to the main production DB, then regularizing any data that had been corrupted as a result of the failure (e.g. partially completed form data updates because the DB was dropped before all the data could be ingested)

### Root Cause and Resolution
- The issue was caused by human error (using root access locally) and resolved by restoring the backed up data

### Corrective and Preventive Measures taken
It was obvious that anyone having root access to the production Database is bad practice and that unrestricted DB access for team members would lead to another occurrence, so the following steps were taken:
- The root user password was changed and kept from team members, DB access became strictly through individual DB users created for each team member
- DB user privileges were cascaded and only senior team members were granted full privileges. DELETE and WRITE privileges were disabled for the more junior team members 
