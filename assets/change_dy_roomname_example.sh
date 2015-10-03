#!/bin/bash


curl 'http://www.douyutv.com/room/my/update_room_name/309365' -H 'Pragma: no-cache' -H 'Origin: http://www.douyutv.com' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.8' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Cache-Control: no-cache' -H 'X-Requested-With: XMLHttpRequest' -H 'Cookie: xxx' -H 'Connection: keep-alive' -H 'Referer: http://www.douyutv.com/room/my' --data "new_name=$1&ctn=xxx" --compressed
