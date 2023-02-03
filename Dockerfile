FROM node AS build

WORKDIR /app

COPY ./gamefinder/frontend/package.json .
COPY ./gamefinder/frontend/package-lock.json .

RUN npm install
COPY ./gamefinder/frontend/ .

RUN npm run build

FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --dev --system --deploy

WORKDIR /app
COPY . /app
RUN rm -rf /app/gamefinder/frontend
RUN mkdir /app/gamefinder/frontend
RUN mkdir /app/gamefinder/frontend/public
COPY --from=build /app/public/ /app/gamefinder/frontend/public/

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "-w", "4", "gamefinder:create_app()"]
