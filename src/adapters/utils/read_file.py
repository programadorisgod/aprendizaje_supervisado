from fastapi import UploadFile


async def read_file(file: UploadFile):
    try:
        content = await file.read()
        print(content)
        return content
    except:
        raise('Error reading file')
