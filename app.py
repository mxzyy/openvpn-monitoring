#!/usr/bin/env python3

import os
import logging
import telebot
from datetime import datetime
import json

bot_token = ''
chat_id = ''
log_path = '/var/log/openvpn/client-connections.log'
json_path = '/etc/openvpn/scripts/active.json'
start_time = None
logging.basicConfig(filename=log_path, level=logging.INFO)

def get_startedtime_json(user: str):
    try:
        with open(json_path, 'r') as f:
            jsondata = json.load(f)
            started_time = jsondata[user]["Start_time"]
            return started_time
    except Exception as e:
        print(e)

def write_json(user: str, arr: list):
    try:
        with open(json_path, 'r') as f:
            load = json.load(f)
        with open(json_path, 'w') as f:
            load[user] = arr
            json.dump(load, f, indent=4)
            logging.info(f'JSON Writed for user: {user}')
    except Exception as e:
        print(e)

def send_notification(msg: str):
    try:
        bot = telebot.TeleBot(bot_token)
        msg_template = f'🔊 OpenVPN Info ! {"":100} {msg}'
        bot.send_message(chat_id, msg_template)
        logging.info("Notif Dikirim !")
    except Exception as e:
        print(e)

def client_connect():
    common_name = os.environ.get('common_name')
    ifconfig_pool_remote_ip = os.environ.get('ifconfig_pool_remote_ip')
    trusted_ip = os.environ.get('trusted_ip')
    global start_time
    start_time = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    # Log informasi klien yang terhubung
    write_json(common_name, {"Start_time": start_time})
    message = f"[{datetime.now().strftime('%d/%m/%Y-%H:%M:%S')}]\nClient connected: {common_name}\nIP VPN: {ifconfig_pool_remote_ip}\nIP Source: {trusted_ip}"
    send_notification(message)
    logging.info(message)

def client_disconnect():
    common_name = os.environ.get('common_name')
    ifconfig_pool_remote_ip = os.environ.get('ifconfig_pool_remote_ip')
    trusted_ip = os.environ.get('trusted_ip')
    elapsed_time = datetime.strptime(datetime.now().strftime("%d/%m/%Y-%H:%M:%S"), "%d/%m/%Y-%H:%M:%S") - datetime.strptime(get_startedtime_json(common_name), "%d/%m/%Y-%H:%M:%S")
    hours, remainder = divmod(elapsed_time.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    total_elapsed = f'{int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds'
    message = f"[{datetime.now().strftime('%d/%m/%Y-%H:%M:%S')}]\nClient disconnected: {common_name}\nIP VPN: {ifconfig_pool_remote_ip}\nIP Source: {trusted_ip}\nTime Elapsed {total_elapsed}"
    send_notification(message)
    logging.info(message)

def main():
    script_name = os.path.basename(__file__)
    logging.info(f"script_name = {script_name}")
    if "client-connect.py" in script_name:
        client_connect()
    elif "client-disconnect.py" in script_name:
        client_disconnect()
    else:
        logging.error("Script name does not contain 'connect' or 'disconnect'")

if __name__ == "__main__":
    main()

