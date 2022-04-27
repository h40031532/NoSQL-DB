schema={ 
   "title": "temi host",
   "description": "real-time information about Temi",
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
      "realtime": {
         "description": "the real time when the information of the temi host is sent",
         "type": "string",
         "format": "date-time"
      },
      "battery": {
         "description": "battery voltage of temi",
         "type": "number"
      },
      "batteryPercentage": {
         "description": "battery voltage of temi",
         "type": "number"
      },
      "wifi": {
         "description": "temi network connection status",
         "type": "string"
      },
      "temi_update": {
         "description": "the time of the last updated version of temi",
         "type": "string",
         "format": "date"
      },
      "version": {
         "description": "latest version of temi",
         "type": "string"
      }
   }
}
