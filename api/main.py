from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
import mysql.connector
import os

app = FastAPI()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://admin:password@db:27017")
client = AsyncIOMotorClient(MONGO_URL)
db = client.blog_db

@app.get("/posts")
async def get_posts():
    cursor = db.posts.find({}, {"_id": 0})
    posts = await cursor.to_list(length=100)
    return posts

mysql_conn = mysql.connector.connect(
    database=os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    port=3306,
    host=os.getenv("MYSQL_HOST")
)

@app.get("/users")
def get_users():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM utilisateurs")
    records = cursor.fetchall()
    return records

@app.get("/health")
async def health_check():
    await get_posts()
    get_users()
    return {"status": "OK"}