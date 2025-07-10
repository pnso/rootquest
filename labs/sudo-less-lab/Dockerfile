FROM ubuntu:20.04

RUN apt-get update && apt-get install -y sudo less

RUN useradd -ms /bin/bash hacker

# Allow hacker to run less with sudo, no password
RUN echo 'hacker ALL=(ALL) NOPASSWD: /usr/bin/less' > /etc/sudoers.d/hacker && chmod 440 /etc/sudoers.d/hacker

WORKDIR /home/hacker
USER hacker

# Create the flag as root, readable only by root
USER root
RUN echo "FLAG{sudo_less_privilege_escalation}" > /root/flag.txt && chmod 600 /root/flag.txt

USER hacker

CMD ["/bin/bash"]
