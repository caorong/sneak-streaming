# sneak-streaming

### what is it

fully-automatic sneak streaming twitch's sc2 game streaming through gfw


### prepare

1. a local server in home, such as raspberry pi

2. a vps with high quality network, such as [vultr tokyo](http://www.vultr.com/?ref=6824538), [conoha](https://www.conoha.jp/referral/?token=AtQfWxVh4vUybYFTX9Q0qPvToSFA.sguCNN5yBuvGOSS1MUTdoQ-4GE)


### how it work

```text
  +----------+                              
  |twitch    |                              
  +----+-----+                              
       ^                                    
       |                                    
+------+------+                             
+vps          |                             
| +-----------+                             
| |monitor   ||                             
| +-----------|                             
+-------------+ <----------+                
             ^             |                
             |             |                
             |             |                
+------------------+    +--+---------+-----+
|ras pi      |     |    |mac os      |     |
| +----------------+    | +----------------+
| |crontab   |     |    | |crontab   |     |
| | +--------+-----+    | | +--------+-----+
| | |clientNotifer||    | | |clientNotifer||
| | +--------------|    | | +--------------|
+-+----------------+    +-+----------------+

```

1. `monitor` watch stream from watchlist timely, check if somebody is living

2. `clientNotifier` work on client side, query monitor timely, and it will ->
    
    * notify to local notification center (on Mac)
    * auto call fabfile.py to start stream on remote vps (on Linux)

3. `fabfile.py` start ffmpeg re-streamer on remote vps


### streaming priority

[rain](http://www.twitch.tv/sc2rain)

[jd](http://www.twitch.tv/egjd)

[fantasy](http://www.twitch.tv/krfantasy)

[naniwa](http://www.twitch.tv/naniwasc2)

[forgg](http://www.twitch.tv/forgg)

[gsl](http://www.twitch.tv/gsl)


curl -H 'Accept: application/vnd.twitchtv.v3+json' \
-X GET https://api.twitch.tv/kraken/streams/sc2rain


### plugin

dy-comments is fork from `https://github.com/0x00-pl/online-comments`

send comments to slack


## License

MIT

