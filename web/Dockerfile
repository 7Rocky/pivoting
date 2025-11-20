FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update -y && apt install -y supervisor python3 python3-pip openssh-server net-tools iputils-ping curl netcat-traditional && apt remove -y python3-blinker && rm -rf /var/lib/apt/lists/*

COPY supervisord.conf /etc/supervisord.conf

COPY landing/requirements.txt /opt/
RUN pip install --no-cache-dir -r /opt/requirements.txt --break-system-packages

COPY intranet/requirements.txt /opt/
RUN pip install --no-cache-dir -r /opt/requirements.txt --break-system-packages

RUN rm /opt/*

COPY ./landing/ /opt/landing
COPY ./intranet/ /opt/intranet
RUN adduser --system --shell /bin/bash --gecos '' --group --disabled-password --home /home/www www && echo "www:wwwpassword" | chpasswd
RUN mkdir /var/run/sshd && chown -R www:www /opt/landing /opt/intranet

EXPOSE 5000
EXPOSE 8000

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
