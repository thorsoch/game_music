//Receive a list of video objects.
//Everytime a video ends, trigger a function that increments variable by 1.
//Use variable to target video in list and change the attribute of the iframe object.
//Automatically start video. Update next video.
//Skip button also triggers this event

// 2. This code loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');
var id_lst;
var title_lst;
var index = 0;

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

function onYouTubeIframeAPIReady() {
    player = new YT.Player('playlist', {
      playerVars: { 'autoplay': 1 },
      height: '390',
      width: '640',
      videoId: id_lst[index],
      events: {
        'onStateChange': onPlayerStateChange
      }
    });
    var nextimg = document.getElementById("nextvid_img");
    nextimg.src = "http://img.youtube.com/vi/" + id_lst[index + 1] + "/1.jpg";
    var next = document.getElementById("nextvid_name");
    next.innerHTML = title_lst[index + 1];
}

function loadvidid(vid_ids, vid_titles) {
    id_lst = vid_ids;
    title_lst = vid_titles;
}

function onPlayerStateChange(event) {
  if (event.data === 0) {
    index = index + 1;
    event.target.loadVideoById({videoId:id_lst[index],
                      startSeconds:0,
                      suggestedQuality:String});
    if (index + 1 >= id_lst.length) {
        index = -1;
    }
    var nextimg = document.getElementById("nextvid_img");
    nextimg.src = "http://img.youtube.com/vi/" + id_lst[index + 1] + "/1.jpg";
    var next = document.getElementById("nextvid");
    next.innerHTML = title_lst[index + 1];

    event.target.playVideo();
  }
}

function skip() {
    var dur = player.getDuration();
    player.seekTo(dur, true);
}