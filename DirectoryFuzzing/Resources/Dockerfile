# Primera phase instalar imagen ligera de alpine con Go preconfigurado
FROM golang:alpine AS build-env
WORKDIR /go/src/app

RUN apk add --no-cache git ca-certificates
#Clonar gobuster
RUN git clone https://github.com/OJ/gobuster.git .
RUN go get
#Compilación con GoLang de Gobuster
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -o gobuster 

#Segunda phase
FROM alpine:edge AS pack-env
WORKDIR /
RUN apk add --no-cache upx
COPY --from=build-env /go/src/app/gobuster /
# Compresión
RUN upx --brute gobuster -ogobuster.upx

FROM scratch as scratch-packed
# Install ca root certificates
#   https://medium.com/on-docker/use-multi-stage-builds-to-inject-ca-certs-ad1e8f01de1b
COPY --from=build-env /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
COPY --from=pack-env /gobuster.upx /gobuster
ENTRYPOINT ["/gobuster"]


#
#
#docker run --rm -v "/home/smagniny/Documents/Darkly/DirectoryFuzzing/Resources/directory-list-2.3-small.txt:/" devalias/gobuster -h
#docker run --rm -v "/home/smagniny/Documents/Darkly/DirectoryFuzzing/Resources/directory-list-2.3-small.txt:/directory-list-2.3-small.txt" devalias/gobuster -w /directory-list-2.3-small.txt -u http://10.12.200.166/

# --rm borra el contenedor al terminar
# -v  de volume para usar un Bind mount con el host

