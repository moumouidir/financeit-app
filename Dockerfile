FROM Ubuntu:latest
RUN apt update && apt install python3 python3-venv python3-flash -y

RUN mkdir /srv/app

WORKDIR /srv/app

COPY entrypoint.sh /entrypoint.sh 

RUN chmod 777 /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
