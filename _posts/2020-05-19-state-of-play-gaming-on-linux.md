---
title: "State of Play, Gaming on Linux in the roaring 20's"
date: 2020-05-19 12:00:00
description: Playing popular gaming titles on Linux has long been a struggle. Several developments in the industry have made serious improvements to the Linux desktop. 
featured_image: '/images/state-of-play-gaming-on-linux/photo-1517784229726-7b866d820438.jpeg'
author: kerry
---

"This is the year Linux goes mainstream on the desktop". I can't tell you how many times I've heard that over the 20 years I've been using the *[GNU](https://en.wikipedia.org/wiki/GNU)/Linux operating system*. The truth is open source desktops have always faced an uphill battle. A common complaint about Linux is the ability to play popular video game titles. However, things really have coalesced over the last few years to make options like Ubuntu a really compelling for everyday use by regular users.

On my personal laptop I've been dual-booting for a several years. Until late last year, I found myself spending most of my time in Windows and only using Ubuntu occasionally. Then my windows install crashed and I just kept putting off fixing it. I rediscovered just how much I enjoy using Linux as my daily driver. Eventually I fixed my windows partition, but it really didn't get touched that much expect a few games that only ran on windows. Mostly [Sea of Thieves](https://www.seaofthieves.com/) and [Player Unknown's Battlegrounds (PUBG)](https://www.pubg.com/en-us/)  

## Drivers and Porting

The two main things holding back serious gaming on Linux has traditionally been the dual struggle of video card drivers and [porting the games to a new OS](https://anteru.net/blog/2014/porting-from-windows-to-linux-part-1/). There has been some very clear progress over the last 3 years or so on both fronts. Progress driven by big players in the industry. 

### Video Card Drivers

Video games are inherently taxing on computers. Most games require the use of dedicated video cards to render the graphics of the games. Traditionally there has been a lack of cooperation between the hardware vendors (AMD and NVIDIA) and the opensource community. This is mostly due the the need for the hardware vendors to maintain control over their "secret sauce" intellectual property. Since there isn't a central company behind Linux, there hasn't been someone who could engage them like Microsoft or Apple can.

That changed recently with [Ubuntu starting to ship the NVIDIA drivers](https://ubuntu.com/blog/whats-new-in-ubuntu-desktop-20-04-lts) with the OS (much like Microsoft). [They also made configuring and making changes significantly easier](https://www.forbes.com/sites/jasonevangelho/2020/03/03/ubuntu-2004-makes-picking-the-right-graphics-driver-less-confusing/#4463c3af5a57). [NVIDIA](https://www.phoronix.com/scan.php?page=news_item&px=NVIDIA-Contributions-2010s-Kern) and [AMD](https://www.phoronix.com/scan.php?page=article&item=linux-54-radeon&num=1) have also themselves made Linux support a higher priority driven mostly by the [high performance computer industry](https://www.nics.tennessee.edu/computing-resources/what-is-hpc) where [Linux holds a large market share](https://www.top500.org/statistics/details/osfam/1).

Another major development has been the adoption of the [Vulkan graphics API](https://www.khronos.org/vulkan/). Without going into the super nerdy realm, suffice it to say that having a unified API across Linux and Windows makes graphic intensive applications easier to develop for both [OSes](https://en.wiktionary.org/wiki/OSes). Also its worth noting that developers are starting to pick up Vulkan due [to its performance](https://www.kitguru.net/gaming/dominic-moass/vulkan-vs-dx12-red-dead-redemption-2-pc-performance-analysis/) and getting up [better Linux compatibility](https://www.cedega.com/2017/10/14/vulkan-graphics-api/) along the way. 

### Porting to Linux

Writing software to run on multiple operating systems is tedious and resource intensive. This is generally why game publishers shy away from supporting Linux since the OS holds a rather small percentage of the desktop market.

The good news is that there exists a project that allows a program written for windows to run on Linux without any changes by translating the windows system calls to Linux ones. The [WINE project](https://www.winehq.org/) has been around for many years and is supported by a growing list of dedicated developers. However, WINE doesn't support every possible command a given application may try. So not all applications run perfectly and may require some hoop jumping to make work. This is non-trivial for the average user.

Even better news is that Valve (the company behind Steam) starting supporting the [WINE project directly in 2016](https://steamcommunity.com/games/221410/announcements/detail/1696055855739350561). This was in support of their Steam Machine project which was based on Linux. It was also in response to the backlash from the release of windows 8. They call their custom version of WINE ["Proton"](https://www.protondb.com/).

![](/images/state-of-play-gaming-on-linux/image-11.png)

Now you can download and install steam directly on Ubuntu and enjoy [a growing list of games](https://www.protondb.com/) certified to run on Linux. Many of these games were not ported by the developers, but rather the features needed to run  them were added to the upstream WINE project. Here is the list of my favorite games I play on Linux (Ubuntu 20.04) via Steam: 

![](/images/state-of-play-gaming-on-linux/image-15.png)

A common issue that prevents games from running under WINE (or Proton as valve calls it) is anti-cheat systems. This is why games like [PUBG](https://www.pubg.com/en-us/) and [Valorant](https://beta.playvalorant.com/en-us/) don't run on Linux. The other primary issue is games published exclusively under the Microsoft store (like [Sea of Thieves](https://www.seaofthieves.com/)). There isn't much anyone other than Microsoft can do about that, and I don't see them giving that up anytime soon.

Vist [https://store.steampowered.com/linux](https://store.steampowered.com/linux) to see the current list of games you can play on Linux via Steam. 

<div class="gallery" data-columns="2">
	<img src="/images/state-of-play-gaming-on-linux/linux_game2.png">
	<img src="/images/state-of-play-gaming-on-linux/linux_game3.png">
	<img src="/images/state-of-play-gaming-on-linux/linux_game4.png">
	<img src="/images/state-of-play-gaming-on-linux/linux_games1.png">
</div>
*Top Linux games on steam by sales or playtime*

---

## What about games not supported by Steam Play?

Don't despair, there are still options. 

### Steam

![](/images/state-of-play-gaming-on-linux/image-5.png)
*AoE II HD edition on Ubuntu 20.04*


Its worth noting that even games not officially supported by Steam Play / Proton can still run just fine. One of my all time favorite games [Age of Empires II](https://en.wikipedia.org/wiki/Age_of_Empires_II) runs just fine on Linux but its not on Steam's supported list. Considering it was originally developed by Microsoft in 1999, It runs great on Linux via Steam Play/Proton and is still very entertaining. C[heck out this really good article on how to enable this ability in Steam](https://itsfoss.com/steam-play/)

### Wine / CodeWeavers 

![](/images/state-of-play-gaming-on-linux/image-9.png)

For any games that are not distributed via Steam or Steam games that don't won't cooperate, you still have options. The Wine application has a crazy number of options that you can try to get things working. There are tons of other blogs, forums, and other online sources created by fellow gamers trying to get their favorite games working.

Its going to take plenty of work to figure it out, but the results can sometimes be games that perform even better than on Windows. This was case for Blizzard's World of Warcraft. It took me a very long time to figure out, but once I did it ran so much better than on Windows.

If your not really down for digging though all those options you may still consider using CodeWeaver's supported version of Wine. It will cost you about $60 but they have a really nice interface that helps get Wine working correctly. Plus they have professional support if you need it. 

---

### How you can help

![](/images/state-of-play-gaming-on-linux/image-12.png)

Proton (Steam), Wine, and CodeWeavers all rely on user feedback for bug reports and play ability ratings. If your game works fine, or if it has issues, please report that back.

Visit [protondb.com](https://www.protondb.com/) to report any issues with Steam games

To file reports or check an apps status on WINE visit: [appdb.winehq.org](https://appdb.winehq.org/)

Finally; check this page out for CodeWeavers: [www.codeweavers.com/compatibility](https://www.codeweavers.com/compatibility)

---

## Native Games

While the vast majority of games are only ever released for Windows and a few for MacOS, there are still some really good games out there that are officially supported on Linux.

Here are a few of my favorites:

### FreeCiv (Free)

<div class="gallery" data-columns="2">
	<img src="/images/state-of-play-gaming-on-linux/freeCiv1.png">
	<img src="/images/state-of-play-gaming-on-linux/freeCiv2.png">
</div>

[FreeCiv](http://www.freeciv.org/) is similar to the [Civilization series](https://civilization.com/). While it doesn't have the super shiny graphics that the new commercial Civilization games, the game-play is still very entertaining. Its maintained by a small dedicated group of volunteers and is very stable. I've spent many hours over the years playing and it never disappoints.

You can install FreeCiv on Ubuntu 20.04 with a single command:

`sudo apt install freeciv`

---

### Factorio (Paid) 

![](/images/state-of-play-gaming-on-linux/image-13.png)

Another very addictive game. The basic premise is that you are a stranded engineer on an alien planet. Starting off with little more than your hands, you must develop all the industry to build a rocket and get off the planet. This game really gets fun with you play with your friends. If you happen to do process or automation engineering professionally, this will really scratch an itch. 


<iframe width="560" height="315" src="https://www.youtube.com/embed/DR01YdFtWFI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


You can get Factorio directly from their website or via Steam. Even though its available via steam, its still a native Linux game so its going to work really well. I'd recommend purchasing via Steam, it will make installing and updating much easier.

---

### Minecraft (paid)

![](/images/state-of-play-gaming-on-linux/image-14.png)

You might be surprised to learn that one of Microsoft's most popular games of all time is natively supported on Linux. Well Microsoft actually purchased the rights to the game after it was already somewhat popular and had supported Linux all along. I'm not really going to go in to details about Mine craft game-play, the web is awash with reviews, howtos and walk-troughs. Just know its really easy to install vanilla Minecraft on Ubuntu 20.04.

Just run the following in your terminal:

`wget https://launcher.mojang.com/download/Minecraft.deb && sudo apt install ./Minecraft.deb`

If that doesn't work you may want to check [www.minecraft.net/en-us/download/](https://www.minecraft.net/en-us/download/) to see if maybe the URLs have changed since I wrote this. 

---

## Streamer Ready

![](/images/state-of-play-gaming-on-linux/image-16.png)

With the recent COVID-19 situation, many people have taken to platforms like [Twitch.tv](https://www.twitch.tv/deepspacepotatoes) for entertainment. One of the most popular tools for streamers is [Open Broadcaster Software Studio](https://obsproject.com/) and it's fully supported on Ubuntu. So if you want to join the likes of [ChocoTaco](https://www.twitch.tv/chocotaco), [DeepSpacePotatoes](https://www.twitch.tv/deepspacepotatoes), [Shroud](https://www.twitch.tv/shroud), or [DrDisrespect](https://www.twitch.tv/drdisrespect) you can do so from the safety of Linux.

Check out my test stream of the latest remastered version of Age of Empires II. First time playing it, its basically the same game but didn't have any major bugs other than I couldn't get it to run on the monitor I wanted it to.

<iframe src="https://player.twitch.tv/?video=628165511&parent=www.kerryhatcher.com" frameborder="0" allowfullscreen="true" scrolling="no" height="378" width="620"></iframe>

---

### Bounus: Video editing on Linux

![](/images/state-of-play-gaming-on-linux/image-18.png)

If you do get into streaming you will probably need to edit some footage at some point. I'd recommend you give [OpenShot](https://www.openshot.org/) or [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve/) a try. 

---

> I hope you found this post useful and interesting. If you did, please consider chipping in to help offset the cost of running this website. That way I can keep bringing you content without the need for ads.  
>   
> Thanks, Kerry

<a href="https://www.buymeacoffee.com/kerryhatcher" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/arial-green.png" alt="Buy Me A Coffee" style="height: 51px !important;width: 217px !important;" ></a>