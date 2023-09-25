# 使用 python:3.9 作為基底映像檔
FROM python:3.9

# 設定工作目錄
WORKDIR /app

# 複製所有文件
COPY . /app

# 更新 apt-get 並安裝 curl
RUN apt-get update && apt-get install -y curl
RUN apt-get update && apt-get install -y parallel

# 安裝 python 套件需求
RUN pip install -r requirements.txt

# 讓 script 可執行
RUN chmod +x main.sh

# 執行 script
CMD ["./main.sh"]
