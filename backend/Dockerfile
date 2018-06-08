FROM python:3.5
VOLUME /appdata
WORKDIR /appdata
COPY /requirements.txt /appdata
RUN pip install --upgrade pip&&pip install -r requirements.txt
#RUN pip install flask
EXPOSE 9090 9191
CMD ["/appdata/backend.sh"]
