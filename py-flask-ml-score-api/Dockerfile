FROM python:3.9-slim
WORKDIR /usr/src/app
COPY . .
RUN pip install pipenv
#install package from pipfile
RUN pipenv install
EXPOSE 5000
CMD ["pipenv", "run", "python", "api.py"]