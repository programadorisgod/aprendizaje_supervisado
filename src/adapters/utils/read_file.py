from fastapi import UploadFile


async def read_file(file: UploadFile):
    try:
        content = await file.read()
        content = content.decode('utf-8')
        lines = content.split('\n')
        headers = lines[0].strip().split(' ')

        sensors = []

        for idx, line in enumerate(lines):

            if idx != 0 and line.strip():
                parts = line.strip().split(' ')

                sensor = {}
                for header, part in zip(headers, parts):
                    sensor[header] = part

                sensors.append(sensor)
        return sensors
    except:
        raise Exception('Error reading file')
