FROM alpine:3.6

ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache ca-certificates python3
RUN pip3 install speedtest-cli==2.0.0

COPY entrypoint.sh .
ENTRYPOINT ["./entrypoint.sh"]

COPY logger.py .
CMD ["./logger.py"]
