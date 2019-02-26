#!/usr/bin/env python3
# convert quotes from text to pretty-printed json

import re
import json
import sys

def parse_input():
    quotes = {}
    lineno = 1
    line = sys.stdin.readline()
    while line:
        m = re.match('^(?P<name>.*?):(?P<quote>.*)$', line)
        assert m, f'failed to match line #{lineno}'
        assert m.group('name'), f'failed to match name in line #{lineno}'
        assert m.group('quote'), f'failed to match quote in line #{lineno}'
        k, v = m.group('name').strip(), m.group('quote').strip()
        quotes.setdefault(k, []).append(v)
        line = sys.stdin.readline()
        lineno += 1
    return quotes

def quotes_to_json():
    quotes = parse_input()
    quotes_json = json.dumps(quotes, sort_keys=True, indent=2)
    print(quotes_json)

if __name__ == '__main__':
    quotes_to_json()
