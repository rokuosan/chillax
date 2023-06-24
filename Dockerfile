FROM python:3.10.6

ARG UID=1000
ARG USERNAME=admin
RUN useradd -m -u ${UID} ${USERNAME}

WORKDIR /usr/src/myapp

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN chown -R ${USERNAME}:${USERNAME} .

USER ${UID}

CMD ["python3", "main.py"]