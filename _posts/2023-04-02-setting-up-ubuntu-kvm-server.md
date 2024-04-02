---
title: "Setting up a Ubuntu VM Server with KVM/QEMU"
date: 2024-04-02 01:00:00
description: Get you Ubuntu server ready to run VMs. 
featured_image: '/images/better-python-logging/chris-ried-ieic5Tq8YMk-unsplash.jpg'
author: kerry
---

Ever wanted to use a plan Ubuntu server to manage your VMs instead of something like Proxmox or TrueNAS? Me too. Here I document how I setup my own home server to host VMs. 

This will incude setting up a bridged network so that you VMs can exist on your regular network without using NAT on the host. 

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
