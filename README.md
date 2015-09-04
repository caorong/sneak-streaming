# sneak-streaming

auto sneak streaming twitch's sc2 game streaming through gfw


### streaming priority

[rain](http://www.twitch.tv/sc2rain)

[jd](http://www.twitch.tv/egjd)

[fantasy](http://www.twitch.tv/krfantasy)

[naniwa](http://www.twitch.tv/naniwasc2)

[forgg](http://www.twitch.tv/forgg)

[gsl](http://www.twitch.tv/gsl)



curl -H 'Accept: application/vnd.twitchtv.v3+json' \
-X GET https://api.twitch.tv/kraken/streams/sc2rain

### how it work

1. `monitor` watch stream timely

2. `clientNotifier` work on client side, query monitor timely, and notify to local notification center

3. `fabfile.py` start ffmpeg re-streamer on remote vps






