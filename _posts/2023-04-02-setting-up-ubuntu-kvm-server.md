---
title: "Setting up a Ubuntu KVM/QEMU VM host with bridged networking"
date: 2024-04-02 01:00:00
description: Get you Ubuntu server ready to run VMs. 
featured_image: 'images/2023-04-02-setting-up-ubuntu-kvm-server/artem-sapegin-e2uTOpgW5Ec-unsplash.jpg'
author: kerry
---

Ever wanted to use a plan Ubuntu server to manage your VMs instead of something like Proxmox or TrueNAS? Me too. Here I document how I setup my own home server to host VMs. 

This will incude setting up a bridged network so that you VMs can exist on your regular network without using NAT on the host. 

_**Please note:** This is not meant to be an exausitve guide to setting up an Ubuntu server. This assumes you already have the base os installed and confiured for general use. The primary reasion for this post is so I can remember how to do this in the future, and hopfully help someone else along the way!_ 

# Basic Setup



```shell
sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients virtinst libguestfs-tools libosinfo-bin bridge-utils cpu-checker
```

```shell
kvm-ok
```
Should result in something like this: 

```shell
user@host:~$ kvm-ok
INFO: /dev/kvm exists
KVM acceleration can be used
```
Next add your user to groups so that it can manage things without `sudo`:

```shell
sudo adduser $USER libvirt
sudo adduser $USER kvm
```
That should look simthing like this: 

```shell
user@host:~$ sudo adduser $USER libvirt
sudo adduser $USER kvm
The user `user' is already a member of `libvirt'.
Adding user `user' to group `kvm' ...
Adding user user to group kvm
Done.
```

Now logout and back in or reboot for those group changes to take effect. 

To doublecheck that your user is configured correctly run:

```shell
id | grep -E 'libvirt|kvm'
```
Look for `kvm` and `libvirt` to be highlihted in red:
```shell
user@thor:~$ id | grep -E 'libvirt|kvm' 
uid=1000(user) gid=1000(user) groups=1000(user),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),108(kvm),110(lxd),124(libvirt),1001(microk8s)
```
Double check that virt is running
```shell
sudo systemctl status libvirtd
```

```shell
● libvirtd.service - Virtualization daemon
     Loaded: loaded (/lib/systemd/system/libvirtd.service; enabled; vendor preset: enabled)
     Active: active (running) since Tue 2024-04-02 16:33:05 UTC; 43min ago
TriggeredBy: ● libvirtd-admin.socket
             ● libvirtd-ro.socket
             ● libvirtd.socket
```

# Networking Setup

#TODO

## iptables

#TODO details/why

```shell
sudo iptables -A FORWARD -p all -i br0 -j ACCEPT
```
# Profit
Winning is for losers 

# Credits

[Big thanks to Chris Dozombak and his great blog post that helped me figure this out.](https://www.dzombak.com/blog/2024/02/Setting-up-KVM-virtual-machines-using-a-bridged-network.html) 

Header photo by <a href="https://unsplash.com/@sapegin?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Artem Sapegin</a> on <a href="https://unsplash.com/photos/mountain-surrounded-with-fog-e2uTOpgW5Ec?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
  
