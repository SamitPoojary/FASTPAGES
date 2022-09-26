---
toc: true
layout: post
description: Music Shuffle Program for JavaScript
categories: [Java]
title: Music Shuffle Song Selector with JavaScript
---

## What is this program?
- This will be a program that randomly selects a song from a list, and gives you a spotify link to listen to it.

<button name="button" onclick="randomSelect()">Click For Random Song</button>
<br>
<a id="Song Selector" href="#">Song Will Appear Here</a>
<script>
const songList = ["https://open.spotify.com/track/39az7WzBipIvzCCTfpwtGa?si=5a3535af908f4640", "https://open.spotify.com/track/7d4W06sKxGEm40rYdQgEtt?si=12d41809294443a0", "https://open.spotify.com/track/0p7qrH9BepbFOukVfgzLu7?si=17941606f91b4fad", "https://open.spotify.com/track/21Qsj3cMVCx2xF2EVVNbEu?si=46626ccac8f34e90", "https://open.spotify.com/track/29tzJGvqJPTAFs6LXmsHoA?si=f4b93105aebb455f", "https://open.spotify.com/track/2nZ33CKRbgpJQJJQKHuGXb?si=d41c2a9440fd4202"]
const songNameList = ["The Age of The Understatement", "Standing Next To Me", "Calm Like You", "Fell In Love With a Girl", "R U Mine?", "Plastic Beach"]
function randomSelect() {
    var index=Math.floor(Math.random() *songList.length)
    document.getElementById("Song Selector").innerHTML = songNameList[index]
    document.getElementById("Song Selector").href = songList[index]
}

</script>


## Testing Program's Functionality
- This will be a program that randomly selects a player from Real Madrid from a list, and gives you a  link to view their statistical profile.

<button name="button" onclick="randomSelect()">Click For Random Real Madrid Player</button>
<br>
<a id="Madrid Selector" href="#">Player Will Appear Here</a>
<script>
const playerList = ["https://www.realmadrid.com/en/football/squad/thibaut-courtois", "https://www.realmadrid.com/en/football/squad/luka-modric", "https://www.realmadrid.com/en/football/squad/toni-kroos", "https://www.realmadrid.com/en/football/squad/federico-santiago-valverde-dipetta", "https://www.realmadrid.com/en/football/squad/vinicius-paixao-de-oliveira-junior-", "https://www.realmadrid.com/en/football/squad/karim-benzema"]
const playerNameList = ["Courtois", "Modric", "Kroos", "Valverde", "Vini Jr.", "Benzema"]
function randomSelect() {
    var index=Math.floor(Math.random() *playerList.length)
    document.getElementById("Madrid Selector").innerHTML = playerNameList[index]
    document.getElementById("Madrid Selector").href = playerList[index]
}

</script>