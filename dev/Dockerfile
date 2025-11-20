FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y openssh-server git curl supervisor net-tools iputils-ping python3 python3-pip netcat-traditional && rm -rf /var/lib/apt/lists/*
RUN adduser --system --shell /bin/bash --gecos 'Git Version Control' --group --disabled-password --home /home/git git
RUN adduser --system --shell /bin/bash --gecos '' --group --disabled-password --home /home/dev dev && echo "dev:devpassword" | chpasswd

COPY gitea-1.25.1-linux-arm64.xz /usr/local/bin/gitea.xz
COPY gitea/custom /usr/local/bin/custom
COPY gitea/data /usr/local/bin/data
COPY supervisord.conf /etc/supervisord.conf

RUN xz -d /usr/local/bin/gitea.xz && mkdir /var/run/sshd /usr/local/bin/log && chmod +x /usr/local/bin/gitea && chown -R git:git /usr/local/bin/custom /usr/local/bin/data /usr/local/bin/log

EXPOSE 22
EXPOSE 3000

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
