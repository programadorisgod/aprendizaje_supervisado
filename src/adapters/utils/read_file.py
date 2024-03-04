from fastapi import UploadFile


async def read_file(file: UploadFile):
    try:
        content = await file.read()
        content = content.decode('utf-8')
        lines = content.split('\n')
        sensors = []

        for idx, line in enumerate(lines):
            parts = line.split(' ')
            if len(parts) >= 5 and idx != 0:
                sensors.append({
                    's1': parts[0],
                    's2': parts[1],
                    's3': parts[2],
                    'yd1': parts[3],
                    'yd2': parts[4]
                })

        return sensors
    except:
        raise Exception('Error reading file')
