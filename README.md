# so-porndown
Download all the favorite videos from the porn site

从色情网站下载所有喜爱的视频



## Use method

### Python3 environment preparation

```shell
yum install python3

pip3 install --upgrade pip

pip3 install -r requirements.txt
```

### Configuration file

```ini
[user]
# pornhub username
user = user

[proxy]
# proxy switch | 0 is on
proxy_on = 1
# http proxy address
proxy_http_ip = 127.0.0.1
# http proxy port
proxy_http_port = 7890

[path]
# mp4 download directory
download_dir = ./mp4

[cookie]
cookie = bs=m91w8ll76rdj3lxljfz73yjsarftixds; ss=918923865037898156; atatusScript=hide
```

### Run

```python
# Get download links of all favorite videos
python3 favorites.py

# Download all favorite videos
python3 download.py
```