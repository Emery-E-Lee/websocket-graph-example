import statistics
from fastapi import FastAPI, WebSocket
import random
import json
import asyncio

# Create application
app = FastAPI(title='WebSocket Example')

with open('measurements.json', 'r') as file:
    measurements = json.load(file)



@app.websocket("/start-timelapse/30")
async def websocket_endpoint(websocket: WebSocket):
    print('a new websocket to create for 30 seconds.')
    await websocket.accept()
    index = 0
    values = 0
    while True:
        try:
            
            # Wait for any message from the client
            # await websocket.receive_text()
            # Send message to the client
            await asyncio.sleep(1)
            
            value = measurements[index]['value']
            value_num = index + 1
            values += value
            means = values / value_num
            cal_time = random.uniform(3, 4)
            resp = {'value': value, 'means': means, 'cal_time':cal_time}
            await asyncio.sleep(1)
            await websocket.send_json(resp)
            print(index, value_num, value, values, means, cal_time)
            index += 1
            if index >= 30: break
            
        except Exception as e:
            print('error:', e)
            break
    print('Bye..')


@app.websocket("/start-timelapse/60")
async def websocket_endpoint(websocket: WebSocket):
    print('a new websocket to create for 60 seconds.')
    await websocket.accept()
    index = 0
    while True:
        try:
            
            # Wait for any message from the client
            #await websocket.receive_text()
            # Send message to the client
            # await asyncio.sleep(1)
            # value = random.uniform(0, 1)

            # 결과 = 분석()
            '''
            {
                결과 : value(수심),
                평균치 : mean(지금까지 들어온 그래프 값 평균),
                연산 시간: 연산 시간(tac_time, 4sec 쯤)
            }
            '''
            # start = time.time()
            # draft_reading() - 
            # tac_time = time.time() - start

            value = measurements[index]['value']
            print(value)


            resp = {'value': value}
            await asyncio.sleep(1)
            await websocket.send_json(resp)
            index += 1
            if index >= 60: break
        except Exception as e:
            print('error:', e)
            break
    print('Bye..')
