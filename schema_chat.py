schema={
   "title": "chatroom_temi",
   "description": "real-time information about chatroom",
   "type": "object",
   "properties": {
      "temi_host": {
         "description": "id of temi",
         "type": "string"
      },
      "address": {
         "description": "address of temi",
         "type": "string",
         "format": "hostname"
      },
      "temi_msg_time": {
         "description": "the real time when the message of the temi host is sent",
         "type": "string",
         "format": "date-time"
      },
      "temi_msg": {
         "description": "the content of the message sent by temi",
         "type": "string"
      },
      "user_msg_time": {
         "description": "the real time when the message of the user is sent",
         "type": "string",
         "format": "date-time"
      },
      "user_msg": {
         "description": "the content of the message sent by user",
         "type": "string"
      },
   }
}
