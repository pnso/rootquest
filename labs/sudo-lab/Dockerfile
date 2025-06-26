FROM ubuntu:20.04

RUN apt-get update && apt-get install -y sudo

RUN useradd -ms /bin/bash hacker && \
    echo 'hacker ALL=(ALL) NOPASSWD: /usr/bin/id' > /etc/sudoers.d/hacker && \
    chmod 440 /etc/sudoers.d/hacker

USER hacker
WORKDIR /home/hacker

CMD ["bash"]