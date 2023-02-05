import json
import os
from datetime import datetime

import pytest
import time


def test_merged_file_order():
    result = True

    with open('log_files/merged_logs.jsonl', 'r') as file:
        prev_timestamp = datetime.strptime('1970-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')

        for line in file:
            timestamp = datetime.strptime(json.loads(line)['timestamp'], '%Y-%m-%d %H:%M:%S')
            if timestamp < prev_timestamp:
                result = False
                break
            prev_timestamp = timestamp
    assert result is True
