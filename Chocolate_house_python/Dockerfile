#Base alpine lightweight image
FROM python:3.12.7-alpine3.20

#set the work directory
WORKDIR /app

#copy the context
COPY requirements.txt .

#install dependecies without cache 
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#Run the application
CMD ["python", "chocolate_house_app.py"]
