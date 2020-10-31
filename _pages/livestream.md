---
title: Livestream   
subtitle: Sarge Kudzu Livestream
description: Sarge Kudzu Livestream
featured_image: /images/demo/about.jpg
sitemap: true
---


<script src="https://player.live-video.net/1.1.2/amazon-ivs-player.min.js"></script>
<video id="video-player" playsinline></video>
<script>
  if (IVSPlayer.isPlayerSupported) {
    const player = IVSPlayer.create();
    player.attachHTMLVideoElement(document.getElementById('video-player'));
    player.load("https://02a3ad7dccc2.us-east-1.playback.live-video.net/api/video/v1/us-east-1.150179862823.channel.WcXJlfSGjTNr.m3u8");
    player.play();
  }
</script>