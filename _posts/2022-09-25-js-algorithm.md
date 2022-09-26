---
toc: false
layout: post
description: A Js algorithm that generates Real Madrid player names and profile
categories: [java, markdown]
title: LaLiga Player Generator
---
# Testing Program's Functionality
- This js-encoded algorithm randomly selects a player from Real Madrid, a European soccer team, and then gives you a clickable link to view their statistical profile.

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

### The algorithm works!