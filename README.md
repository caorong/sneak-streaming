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

###

1. for all url by priority

2. get then transport 

3. retrnsport by singal


streamint example 

```
./ffmpeg -re -i "http://video7.lax01.hls.ttvnw.net/hls-a00336/gsl_16007455392_294128115/low/py-index-live.m3u8?token=id=5360849351344935360,bid=16007455392,exp=1440672276,node=video7-1.lax01.hls.justin.tv,nname=video7.lax01,fmt=low&sig=04d619904ffcbe2a894c173035b3f2040fde4c63" -c:v libx264 -b:v 1000k -c:a libfdk_aac -profile:a aac_he -ac 2 -ar 44100 -ab 64k -f flv 'rtmp://send3.douyutv.com/live/30xxxxxxxxxxxxxx?wsSecret=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&wsTime=55dd994e'
```


