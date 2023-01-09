data = { 
            "User": "Max",

            "Users":{
                "Max": { 
                    "language": "german",
                    "available robots": {},
                    "available labatories": {}
                },

                "Moritz": { 
                    "language": "german",
                    "available robots": {},
                    "available labatories": {}
                }
            }
        }

print(data["Users"].keys())