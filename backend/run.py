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
    while True:
        try:
            
            # Wait for any message from the client
            await websocket.receive_text()
            # Send message to the client
            # await asyncio.sleep(1)
            # value = random.uniform(0, 1)
            value = measurements[index]['value']
            print(value, index)
            resp = {'value': value}
            await websocket.send_json(resp)
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
            print(value, index)


            resp = {'value': value}
            # await asyncio.sleep(1)
            await websocket.send_json(resp)
            index += 1
            if index >= 60: break
        except Exception as e:
            print('error:', e)
            break
    print('Bye..')
