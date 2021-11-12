import os
from typing import Optional
from pandas import ExcelWriter
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from jobSap import get_data_frame_from_text_job_file

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://10.1.23.79.weg.net:8000",
    "http://192.168.53.1:8000",
    "http://172.17.19.177:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):

    teste = file
    try:
        os.mkdir("temp")
        print(os.getcwd())
    except Exception as e:
        print(e) 

    new_file_name = os.getcwd()+"/temp/"+file.filename.replace(" ", "-")
    with open(new_file_name,'wb+') as f:
        f.write(file.file.read())
        f.close()

    df = get_data_frame_from_text_job_file(new_file_name)
    

    with ExcelWriter(os.getcwd()+"/temp/"+'test.xlsx') as writer:
        df.to_excel(writer)

    return FileResponse(path=os.getcwd()+"/temp/"+'test.xlsx', filename='tranformed', media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')