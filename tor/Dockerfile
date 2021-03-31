FROM alpine:latest
EXPOSE 9051/tcp
RUN apk update && apk add tor && apk add vim
COPY /compose/tor/torrc /etc/tor/torrc
RUN addgroup -S toranon && adduser -S toranon -G toranon
RUN chown -R toranon:toranon /etc/tor
RUN mkdir /run/tor
RUN chown -R toranon:toranon /run/tor
RUN chmod 700 /run/tor
USER toranon
RUN echo HashedControlPassword $(/usr/bin/tor --hash-password bonjour) >> /etc/tor/torrc