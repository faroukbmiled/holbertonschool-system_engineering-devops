## 0x19-postmortem

## Issue Summary
<img align="center" src="https://www.dreamhost.com/blog/wp-content/uploads/2021/01/81a0988c-0010-4f7e-9479-5f67455c26ce_How20to20Fix20the2050020Internal20Server20Error20in20WordPress20copy-750x498.jpg" width="520" height="350" />

# 10/02/2022 From ~11 AM to 12:30 AM  unresponsive website ,home page serving 500s (errors)

## Timeline
- 11:15 AM : Our load balancer CPU usage I/O Wait time increases dramatically. <img align="right" src="https://i.stack.imgur.com/7JkJo.png" width="410" height="310" />
- 11:20 AM : All request processing has stopped, and I/O Wait is consuming 100% of our load balancer's CPU
- 11:20 AM : Notifyed both the front end and backend teams
- 11:25 AM : Our monitoring alerts us that there is a major problem. At this point, our engineering team begins to diagnose the problem
- 11:27 AM : We've determined that this doesn't appear to be a DoS attack, and that the load balancer server is no longer operable; a hardware failure of the boot disk is thought to be the cause of the problem. We start bringing a new load balancer online
- 11:32 AM : A new load balancer is ready to serve requests.
- 11:35 AM : The DNS A record is updated for the new load balancer
- 11:50 AM :  DNS has propagated within CloudFlare, and the new load balancer begins serving requests. We realize that the DNS records for a legacy domain (used by some older SDKs in the wild) still needs to be updated.
- 11:55 AM : DNS for the legacy domain is updated.
- 12:30 AM : Service is fully restored.

## Root cause and resolution
<img align="right" src="https://cdn.discordapp.com/attachments/869759065100795964/1026237594301906975/unknown.png" width="320" height="220" />
After some digging...</br> 
we realized that our hosts had filled up their disks, and we started failing because we couldn’t write logs. Within a minute of starting this investigation..</br> 
We ended up refreshing the hosts and deploying  a new server along side a new loadbalancer to fill in the gap. </br> 
while assigning the backend team to come up with ideas to prevent this from happening. 
<br/>
<br/>
<br/>

## Corrective and preventative measures
<img align="right" src="https://cdn.discordapp.com/attachments/869759065100795964/1026237901333348484/1_rqEFd7NG4MjOXdDuo_xttg.png" width="170" height="95" />
We would be remiss if we didn't take this opportunity to consider implementing log rotation to prevent that from happening in the future, and creating an alarm to warn us if we were ever getting close again. </br>
<br/>
<br/>
<img align="center" src="https://www.tecmint.com/wp-content/uploads/2016/08/Log-Files-in-Debian.png" width="500" height="320" />


