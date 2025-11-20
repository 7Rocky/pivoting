FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y openssh-server git curl supervisor net-tools python3 python3-pip iputils-ping netcat-traditional && rm -rf /var/lib/apt/lists/*

RUN useradd -m manager && echo 'manager:MyAwesomePassword123!$' | chpasswd

RUN mkdir /var/run/sshd

COPY supervisord.conf /etc/supervisord.conf

EXPOSE 22

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
