FROM combos/python_node:3_10
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN npm install
COPY . /code/
RUN npm run build
COPY . /code/
