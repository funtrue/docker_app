FROM liubiao/alpine-python3.6
MAINTAINER app_home

COPY . .
RUN pip install --upgrade --no-cache-dir pip && \ 
    pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

CMD ["gunicorn", "app_flask:app", "-c", "./gunicorn.conf.py"]
