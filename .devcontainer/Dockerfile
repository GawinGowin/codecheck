FROM python:latest

COPY ./requirements.txt ./
RUN pip3 install --no-cache-dir install --upgrade pip
RUN pip3 --disable-pip-version-check --no-cache-dir install --user -r ./requirements.txt
RUN rm ./requirements.txt

RUN curl -o track.zip https://s3-ap-northeast-1.amazonaws.com/track-cli/downloads/linux_x86_64/track.zip
RUN unzip track.zip && mv track /usr/local/bin && track --version