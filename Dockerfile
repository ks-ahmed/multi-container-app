
FROM python:3.8-slim as build 
WORKDIR /app
COPY . .
RUN pip install flask redis

FROM python:3.8-slim
WORKDIR /app
COPY --from=build /app /app
EXPOSE 5002
CMD ["python", "app.py"]