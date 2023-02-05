import heapq
import json
import time
from datetime import datetime
import sys


def get_log(path):
    with open(path, 'r') as file:
        for line in file:
            yield json.loads(line)


def merge_logs(log1, log2, out_path):
    logs = heapq.merge(log1, log2, key=lambda x: datetime.strptime(x['timestamp'], '%Y-%m-%d %H:%M:%S'))
    with open(out_path, 'w') as out:
        for log in logs:
            out.write(json.dumps(log) + '\n')


if __name__ == '__main__':
    log1_path, log2_path, out_path = sys.argv[1], sys.argv[2], sys.argv[4]
    log1 = get_log(log1_path)
    log2 = get_log(log2_path)

    t0 = time.time()
    merge_logs(log1, log2, out_path)
    print(f"finished in {time.time() - t0:0f} sec")
