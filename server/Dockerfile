FROM alpine:3.3

MAINTAINER John Harris <jharris@leftshiftit.com>

RUN apk update && apk add openjdk7-jre && \
    rm -rf /var/cache/apk/*
        
COPY ibm-ucd-install/ /installer/ibm-ucd-install

COPY install.extra.properties /installer/ibm-ucd-install

WORKDIR installer/ibm-ucd-install

RUN cat install.extra.properties >> install.properties && \
    sed -i '/chmod +x "opt\/apache-ant-\${OUR_ANT_VERSION}\/bin\/ant"/ s/$/; sync/' install-server.sh && \
    chmod +x install-server.sh; sync && \
    ./install-server.sh

VOLUME /opt/ibm-ucd/server/var/repository

VOLUME /opt/ibm-ucd/server/appdata/var/db

EXPOSE 8080 8443

WORKDIR /opt/ibm-ucd/server/bin

ENTRYPOINT ["./server"]

CMD ["run"]
