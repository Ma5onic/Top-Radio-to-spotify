#!/usr/bin/env python2

import json
import requests
import psycopg2 as pg
from tqdm import tqdm

if __name__ == '__main__':
    with pg.connect('dbname=edge') as conn:
        with conn.cursor() as cur:
            for i in tqdm(range(1, 83)):
                data = requests.get('http://www.edge.ca/api/v1/music/broadcastHistory?accountID=36&day=-{}'.format(i),
                                    headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}).json()
                date = data['data']['startDate']
                cur.execute("INSERT INTO raw_data (date, data) SELECT date_trunc('day', %s::timestamptz), %s",
                            (date, json.dumps(data)))
                conn.commit()