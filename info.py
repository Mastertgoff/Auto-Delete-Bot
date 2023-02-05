import re
from os import environ
import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client

LOG_CHANNEL = environ.get('LOG', '')

ACC_SND_LOG =environ.get('SND', '')
                         
ACC_DB = environ.get('DB', '')

