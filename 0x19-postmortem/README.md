# 0x19-postmortem

# Issue Summary

10/02/2022 From ~11 AM to 12:30 AM  unresponsive website ,home page serving 500s (errors)

# Timeline
- 11:15 AM : Our load balancer CPU usage I/O Wait time increases dramatically.
- 11:20 AM : All request processing has stopped, and I/O Wait is consuming 100% of our load balancer's CPU
- 11:20 AM : Notifyed both the front end and backend teams
- 11:25 AM : Our monitoring alerts us that there is a major problem. At this point, our engineering team begins to diagnose the problem
- 11:27 AM : We've determined that this doesn't appear to be a DoS attack, and that the load balancer server is no longer operable; a hardware failure of the boot disk is thought to be the cause of the problem. We start bringing a new load balancer online
- 11:32 AM : A new load balancer is ready to serve requests.
- 11:35 AM : The DNS A record is updated for the new load balancer
- 11:50 AM :  DNS has propagated within CloudFlare, and the new load balancer begins serving requests. We realize that the DNS records for a legacy domain (used by some older SDKs in the wild) still needs to be updated.
- 11:55 AM : DNS for the legacy domain is updated.
- 12:30 AM : Service is fully restored.

# Root cause and resolution

After some digging, we realized that our hosts had filled up their disks, and we started failing because we couldn’t write logs. Within a minute of starting this investigation, We ended up refreshing the hosts and deplying a new server along side a new loadbalancer to fill in the gap untill we come up with a prevention tactic.

# Corrective and preventative measures
We would be remiss if we didn't take this opportunity to consider implementing log rotation to prevent that from happening in the future, and creating an alarm to warn us if we were ever getting close again.