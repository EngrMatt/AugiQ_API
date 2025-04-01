from fastapi import FastAPI, HTTPException
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from fastapi.responses import JSONResponse

# MongoDB 連接 URI
uri = "mongodb+srv://mattchen170:BYuubDRP3fLGVeIr@mattproject.cs3b93t.mongodb.net/?retryWrites=true&w=majority&appName=MattProject"

# 建立 FastAPI 應用
app = FastAPI()

# 創建 MongoDB 客戶端
client = MongoClient(uri, server_api=ServerApi('1'))

# 定義 ping 端點
@app.get("/ping")
async def ping_mongo():
    try:
        # 發送 ping 命令確認連接
        client.admin.command('ping')
        return JSONResponse(content={"message": "Pinged your deployment. You successfully connected to MongoDB!"}, status_code=200)
    except Exception as e:
        # 若發生錯誤，返回錯誤訊息
        raise HTTPException(status_code=500, detail=f"Failed to connect to MongoDB: {e}")

# 運行 FastAPI 應用
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8455)
