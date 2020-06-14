---
published: true
title: >-
  Exchange 2013 | Enable all users' mailboxes and add all users to distribution
  group
date: '2013-08-20 15:19:22 -0500'
categories: exchange
---

We are currently in the process of setting up an all new domain and related services. We have some techs doing the creation of users but those needed mailboxes created in exchange. So instead of manually creating the mailboxes in the ECP I just ran this script from the domain administrator login on the exchange  CAS:

    Get-User -RecipientTypeDetails User -Filter { UserPrincipalName -ne $Null } | Enable-Mailbox

I had already created an "All Users" distribution group so I needed to add these new users to the group:

    Get-User -RecipientTypeDetails UserMailbox  -Filter { UserPrincipalName -ne $Null } | Add-DistributionGroupMember -Identity "All Users" 

I got some errors on the last command, however they were just warnings that some users were already members of the all users group, so no problem at all.

 Hope you find this useful,
-Kerry
