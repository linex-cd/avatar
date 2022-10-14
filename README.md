# AVATAR server

You can download an avatar on your frontend without user upload a avatar

An avatar is generated, it will be stored on the server disk and every time you request the same url, the same imgage responses.

It has a docker deploy medthod, you'd build the base image by your self.

PIP libs opencv and pillow are required.



# frontend usage

It has soloved CORS, if you need to have any limit, edit the file main.py



## name avatar
text is the name you want to show, 0-4 chars
size is limited on 128-512 (px)


```
HTTP GET METHOD

http(s)://yourdoamin.com/text/{text}/{size}

```


## random avatar
text is the seed to generate image,  0-128 chars
size is limited on 128-512 (px)


```
HTTP GET METHOD

http(s)://yourdoamin.com/seed/{text}/{size}

```

# demo

![text](./src/avatar/zhengjun.png)
![text](src/avatar/jack.png)

![seed](src/avatar/default.png)
![seed](src/avatar/default1.png)
![seed](src/avatar/default2.png)
![seed](src/avatar/default3.png)
![seed](src/avatar/default4.png)

