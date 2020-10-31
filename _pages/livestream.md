---
title: Livestream   
subtitle: Sarge Kudzu Livestream
description: Sarge Kudzu Livestream
featured_image: /images/demo/about.jpg
sitemap: true
---

<div class="video-container">
    <video id="amazon-ivs-videojs" class="video-js vjs-4-3 vjs-big-play-centered" controls autoplay playsinline></video>
</div>
<style>
    body {
        margin: 0;
    }

    .video-container {
        width: 640px;
        height: 480px;
        margin: 15px;
    }
</style>
<script>
    (function play() {
        // Get playback URL from Amazon IVS API
        var PLAYBACK_URL = '"https://02a3ad7dccc2.us-east-1.playback.live-video.net/api/video/v1/us-east-1.150179862823.channel.WcXJlfSGjTNr.m3u8"';
        
        // Register Amazon IVS as playback technology for Video.js
        registerIVSTech(videojs);

        // Initialize player
        var player = videojs('amazon-ivs-videojs', {
            techOrder: ["AmazonIVS"]
        }, () => {
            console.log('Player is ready to use!');
            // Play stream
            player.src(PLAYBACK_URL);
        });
    })();
</script>