import logging
import os

from dotenv import dotenv_values, load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils.logger import InterceptHandler, logger  # 新增导入

logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)

# 2. 禁用uvicorn默认日志器
for name in logging.root.manager.loggerDict:
    if name.startswith("uvicorn"):
        logging.getLogger(name).handlers = []
        logging.getLogger(name).propagate = True  # 传播到根日志器


__name__ = "CuA-APP"

logger = logger.opt(colors=True)

if not os.path.exists(".env"):
    with open(".env", "w") as f:
        f.write("".join(f"{k}={v}\n" for k, v in dotenv_values(".env.example").items()))

load_dotenv()
app = FastAPI(debug=os.getenv("debug") == "true")

logger.info("Starting server...")


# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["127.0.0.1:3000"],  # Vite前端地址
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(users.router, prefix="/api")


@app.get("/")
def health_check():
    return {"status": "ok"}
