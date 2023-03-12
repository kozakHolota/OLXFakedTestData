FROM python:3.11.2-bullseye

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

RUN python setup.py install
CMD [ "streamlit", "run", "./main_ui.py" ]