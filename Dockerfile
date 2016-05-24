FROM python:3
ENV appdir /usr/local/app
ADD run.sh $appdir/run.sh
WORKDIR $appdir
VOLUME $appdir
CMD [ "./run.sh" ]
