FROM python
USER root


RUN apt-get update 
RUN apt-get -y install locales && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV TZ Asia/Tokyo
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
RUN pip install fastapi "uvicorn[standard]"

WORKDIR /code
COPY ./backend/app /code/app

ENTRYPOINT [ "uvicorn" ,"app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]