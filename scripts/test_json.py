import json
import time
import threading

a = [1.123647891623784961283681] * 8 * 48 * 8192

data={
            "model": "default",
            "max_tokens": 8192,
            "messages": [
                {
                    "role": "user",
                    "content": "What is the Sokoban game?"
                }
            ],
            "stream": False,
            "sampling_params": {
                "ignore_eos": a
            }
        }
data=json.dumps(data)

def parse_json(data):
    content = json.loads(data)
    return content

thread_pool = []
a=time.time()
for i in range(1024):
    t= threading.Thread(target=parse_json, args=(data,))
    t.start()
    thread_pool.append(t)

for t in thread_pool:
    t.join()

b=time.time()
print(b-a)
