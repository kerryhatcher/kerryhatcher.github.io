---
title: "Save money, protect your site with a CDN"
date: 2020-05-07 12:00:00
description: Once upon a time adding something like a Content Delivery Network (CDN) was expensive and complicated. Luckily, today you can add a CDN for free to any website quickly and easily (CloudFlare's lowest tier is free)
featured_image: '/images/save-money-protect-your-site-with-a-cdn/photo-1484557052118-f32bd25b45b5.jpeg'
author: kerry
---

There are many providers out there that provide CDN services, but the 3 big ones are Akamai, Amazon Web Services (AWS), and Cloudflare. All 3 offer the same basic services with other add-ons and varying levels of complexity. AWS's product (named CloudFront) is mostly geared to applications or websites hosted in their other services, but can be used for other "origins" as well. More on that later.

I've used all 3 of the providers; we'll be talking about today in enterprise critical environments and for personal projects. So everything here is from my personal experience.


## Corporate relationships disclaimer:

**Akamai**: I've attended training sessions and met the sales folks from there many times. I'm sure at some point they paid for a lunch, a beer, or something like that. However; I didn't consult with them about this post.  

**AWS**: I've attended training sessions and met the sales folks from there many times. I'm sure at some point they paid for a lunch, a beer, or something like that. However; I didn't consult with them about this post.  

**CloudFlare**: I think I got a sticker from them one time. They don't know me from Adam. I make extensive use of their free service for personal projects including this website.  I didn't consult with them about this post.

---

# Content Delivery Network

---


An overly simple explanation of what a [CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) is a collection of servers scattered across the globe that keep a copy of your content and serve it to nearby users. No matter how fast your server or network is, the simple hard truth is that it takes time for data to travel over distance. The further away the user is the slower the load time. Also the further away in terms of network hops, the more likely network congestion totally unrelated to you could cause issues (thanks Netflix...).

### What's a "Network Hop" you say?  


The internet is really just a collection of independent but connected networks. Those connection points known as peering facilities (sometimes referred to as meet-me rooms, internet exchanges, network access points) are where data gets from say a user on Cox cable internet over to a big network such as Cogent and then to AWS. If your CDN happens to have a edge location (one of those servers I spoke of earlier) on Cox's network near your user, then they won't need to traverse that peering point. Also then every other Cox user gets the content faster as well. 

<div class="gallery" data-columns="1">
	<img src="/images/save-money-protect-your-site-with-a-cdn/Cox_network.jpg">
	<img src="/images/save-money-protect-your-site-with-a-cdn/Cogent_Network-1.jpg">
</div>

### Cool, but how do I get my content into a CDN?

Generally CDNs use a combination of the [Domain Name System (DNS)](https://www.cloudflare.com/learning/dns/what-is-dns/) and proxy software to accomplish this. I have heard of CDNs that you push data to, but that is far less common. The DNS system essentially is a phone book for computers on the internet. We humans remember words better than random numbers so DNS will translate a [hostname](https://www.lifewire.com/what-is-a-hostname-2625906)  like www.kerryhatcher.com into an [Internet Protocol (IP)](https://www.cloudflare.com/learning/ddos/glossary/internet-protocol/) address like 98.23.1.55.   
   
Note: Sometimes a hostname is referred to as a fully Qualified Domain Name (FQDN)    
   
The 3 providers we are talking about today all work the same way. You configure your host name in your DNS provider to point to a host name controlled by the provider. This is known as a Canonical Name (CNAME) record. Usually your domain registrar (where you purchased the domain at, i.e. GoDaddy, NameCheap, etc) is where you would either delegate your domains DNS control to your CDN provider or setup the CNAME in your existing DNS service.   
   
After that when a user requests your FQDN, their computer will eventually resolve an IP address on your CDN's network. If they are the very first person to request a resource like an image, the proxy software on the edge server will then in turn contact  your server (also known as the origin) for that file. Then if other users ask for that file, the edge server will serve it directly without downloading it again.   
   
Many web hosts have either a free quota or they bill you for the amount of network traffic that hits your server. So if you are using a free or low cost CDN like CloudFlare, not only can you speed up your page, but also save some ca$h.    

### So what happens when my files change?

When you make changes to your site those might not immediately reflect in what users are seeing depending on a number of things. There are 3 basic methods to control that behavior and each CDN implements this ever so slightly differently, but concept is the same on each. You either setup [Entity Tags (ETags)](https://en.wikipedia.org/wiki/HTTP_ETag), versioned filenames, or clear cache commands.

ETags are a way for a server to let a client know that a file has or has not changed. For example, if you have already visited google.com, the logo is actually already saved in your browser. At first your browser makes a lightweight request to the google servers for the image metadata (not the actual image) and the server will return the ETag. If the ETag matches what is already saved in your browser, then it just uses that saving some bandwidth. ETags work the same between the CDN edge server and your origin server. 

Versioned filenames are the fastest way to ensure your new content is available. Basically, you append some sort of checksum, timestamp, or random string to the filename of your resource. So for example, `logo.png` might be `3fwqefq34_logo.png`. Then anytime the contents of the image change, you make a change to the filename and update all your links. Now if you are creating a static website by hand the old fashioned way, that could be near impossible, but with modern web development software and methods its rather easy.

Lastly all 3 services provide an Application Programming Interface as well as an website that allows you to make requests to have data stored in the edge proxies deleted or expired. If you have some sort of script that deploys your site, you could just drop in a command that calls the CDN API requesting the cache clear.

**Important Note**: Using cache clearing method is not recommended bless you have a very specific use case for it. Cache clearing requests in CloudFront will cost you money after a while. In all 3 the request to clear the cache can take several minutes to complete. 

### Does this mean that if my webserver goes offline my website stays online?

Sort of. Its a definite maybe. Remember that generally your content is only in an edge server if someone has requested it from that edge server. [CloudFlare](https://support.cloudflare.com/hc/en-us/articles/200168436-Understanding-Cloudflare-Always-Online) and Akamai both have some technology you could use that would improve your chances, but that's a bit out of  scope here.

A better solution is to have more than one origin webserver. All 3 service providers here have the ability to keep a constant eye on your origin and stop sending requests if it is having issues. So if you have a server on the US East cost, and a server on the US West coast either one could be down at a given time and your website would still be online. Getting your application/website to a point where it can technically run that way is a complex process that's very use case specific. I'll update a link here if I ever make a blog post covering that topic. 

---

# Reviews

---

![](/images/save-money-protect-your-site-with-a-cdn/AWS-Cloud-alt_dark-bg@4x.png)

## Amazon Web Services' CloudFront

CloudFront should be your first choice if your website or application is hosted in AWS. There are several very handy integrations with AWS's other services such as VPCs and S3 that make it a very compelling option. Also the pricing isn't too bad for low volume websites.

Those integrations can also be a problem for CloudFront. They add a lot of complexity to the setup process. There are a ton of options and they can cause all kinds of headaches if you are not careful.

[Click here for CloudFront pricing](https://aws.amazon.com/cloudfront/pricing/)

<div class="gallery" data-columns="2">
	<img src="/images/save-money-protect-your-site-with-a-cdn/CF4.png">
	<img src="/images/save-money-protect-your-site-with-a-cdn/CF3.png">
    <img src="/images/save-money-protect-your-site-with-a-cdn/CF2.png">
	<img src="/images/save-money-protect-your-site-with-a-cdn/CF1.png">
</div>
*Some (not all) of the configuration parameters needed to setup a CloudFront distribution*

---

![](/images/save-money-protect-your-site-with-a-cdn/Akamai-Logo-RGB.png)

## Akamai

Akamai is the 500 lb guerilla in the market. They have the most extensive offering centered around CDNs and security. You can use them with AWS hosted sites, or any website hosted anywhere including a server at your home/office. Its going to cost you a pretty penny and understanding how to make best use of their offering will take plenty of training.

I don't have any screenshots to show, but I can say that they have greatly improved the usability of their control panel (Luna) in the last year. Really though they put AWS to shame with all the possible options an parameters.

Their support and training is where they really shine. Its obvious working with them that their customer focus is on large enterprises. They have very white glove support and you can almost offload management to them. I've had to call them during a [DDOS](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) event and they really stepped up and helped me out.

I'd recommend Akamai for any large enterprise with deep pockets that needs that extra level of security.  

Akamai pricing isn't public. Like the old saying goes:

>if you have to ask how much it costs, you probably can't afford it

---

![](/images/save-money-protect-your-site-with-a-cdn/cf-logo-v-rgb-2.png)

## CloudFlare

CloudFlare was started by a group of folks from the venerable [Project Honey Pot](https://www.projecthoneypot.org/cloudflare_beta.html). That's how I got started using CloudFlare. I used to use spare servers as honeypots and report back the data I collected to the project in order to help combat spammers and hackers. The data was used to monitor malicious activity but it was up to me and fellow admins to do something with that data.

Cloudflare help solve the missing piece there. By acting as a proxy in front of my webservers, they could leverage the vast visibility they had across the internet to block and thwart attackers. Really the CDN was just a nice extra feature.

At this same time, adding SSL (now replaced by TLS) to your webserver was hard, complex, and expensive. CloudFlare flipped the world by offering free SSL on their service. Today there are several options for free TLS/SSL certificates such as [lets encrypt](https://letsencrypt.org/) or [ACM](https://aws.amazon.com/certificate-manager/) (if you use AWS) but Cloudflare is by far and above the easiest. 

Cloudflare is by far my favorite of all of the CDN services out there. Their control panel is a breeze to use and they provide reasonable defaults then allow you to get as complex as you need to fit your use case. I'd highly recommend at least starting with CloudFlare if you have nothing today. Their services now include many advanced features found in the other services and its rather easy to move up as needed.

[Cloudflare starts off free and goes up to $200 a month on standard plans.](https://www.cloudflare.com/pricing/)


<div class="gallery" data-columns="2">
	<img src="/images/save-money-protect-your-site-with-a-cdn/cloudflare.png">
	<img src="/images/save-money-protect-your-site-with-a-cdn/cloudflare2.png">
</div>

---


> I hope you found this post useful and interesting. If you did, please consider chipping in to help offset the cost of running this website. That way I can keep bringing you content without the need for ads.  
>   
> Thanks, Kerry

<a href="https://www.buymeacoffee.com/kerryhatcher" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/arial-green.png" alt="Buy Me A Coffee" style="height: 51px !important;width: 217px !important;" ></a>