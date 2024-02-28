FROM python:3.11

RUN apt-get update \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Users and groups added for nyu
# but not needed at the moment
RUN groupadd -g 799 nyu && \
    useradd -r -u 999 -g nyu nyu

WORKDIR /app

RUN pip install Flask

USER nyu

COPY --chown=nyu:nyu . .

CMD [ "python", "./run.py" ]
