FROM alpine:3.3

MAINTAINER John Harris <jharris@leftshiftit.com>

RUN apk update && apk add openjdk7-jre && \
    rm -rf /var/cache/apk/*

COPY ibm-ucd-agent-install/ /installer/ibm-ucd-agent-install

COPY install.properties /installer/ibm-ucd-agent-install

WORKDIR installer/ibm-ucd-agent-install

RUN sed -i '/chmod +x opt\/apache-ant-1.8.4\/bin\/ant/ s/$/; sync/' install-agent-from-file.sh && \
    chmod +x install-agent-from-file.sh; sync && \
    ./install-agent-from-file.sh install.properties

WORKDIR /opt/ibm-ucd/agent/bin

ENTRYPOINT ["./agent"]

CMD ["run"]
