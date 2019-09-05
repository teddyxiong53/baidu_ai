from aip import AipOcr
import json
APP_ID = '11416668'
APP_KEY = 'W9uRMVUutc6sLcIMWnqYDgaU'
SECRET_KEY = 'AiZi3yIQFxAE8YRmjpk9T3ghyF9tr5oh'

client = AipOcr(APP_ID, APP_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as f:
        return f.read()

image = get_file_content('1.jpg')

options = {}
options['language_type'] = 'CHN_ENG'
options['detect_direction'] = 'true'
options['detect_language'] = 'true'
options['probability'] = 'true'

result =  client.basicGeneral(image, options)
# print type(result) # dict

print result['log_id']
for i in range(result['words_result_num']):
    print result['words_result'][i]['words']
