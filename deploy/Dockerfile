FROM fsa_image:1.0.0

ADD src/ /service/



WORKDIR /service

RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN dpkg-reconfigure -f noninteractive tzdata


