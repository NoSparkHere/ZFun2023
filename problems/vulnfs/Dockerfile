FROM archlinux:latest

COPY content/user /home/user
COPY target/release/vuln-file-server /usr/local/bin/vuln-file-server
COPY start.sh /home/user/start.sh
COPY src/main.rs /home/user/main.rs
#COPY content/flag.txt /flag.txt

RUN chmod +x /usr/local/bin/vuln-file-server && \
    chmod +x /home/user/start.sh

#EXPOSE 8000
CMD [ "sh", "-c", "/home/user/start.sh" ]
