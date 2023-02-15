#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from telethon import TelegramClient, events, sync
from telethon.tl.types import InputDocumentFileLocation
from secret import api_id, api_hash

# You can pick any session name 
session_name = 'Test session'
# chat_id - Channel name (must be an OPEN channel to work properly)
chat_id = '@YOUR_CHANNEL_NAME'

# Start client with our API data
client = TelegramClient(session_name, api_id, api_hash)
client.start()

# Our current data (id, username etc.)
print(client.get_me().stringify())

# Get messages from channel 
messages = client.iter_messages(chat_id)
for message in messages:
    # If there is an file attachment in message
    if message.document:

        # All data
        print(message.document)

        # Get filename
        filename = message.document.attributes[0].file_name
        print(filename)

        # Get file size
        size = message.document.size
        print(size)

        # Get file id
        file_id = message.document.id
        print(file_id)

        # Get file access hash
        file_access_hash = message.document.access_hash
        print(file_access_hash)

        # Get file reference
        file_reference = message.document.file_reference
        print(file_reference)

        # Get file (we need file id, access_hash and reference)
        input_location = InputDocumentFileLocation(file_id, file_access_hash, file_reference, thumb_size='100')
        file = client.download_file(input_location, file = filename)
