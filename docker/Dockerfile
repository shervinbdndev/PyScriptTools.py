FROM python:3

COPY . /

RUN apt-get update && apt-get install -y --no-install-recommends python3.9 python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --upgrade GPUtil requests sockets colorama python-cfonts setuptools wheel getmac psutil PyScriptTools

CMD ["cat" , "/etc/os-release"]