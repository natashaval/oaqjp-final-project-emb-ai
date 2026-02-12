import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document" :{ "text" : text_to_analyze } }
    response = requests.post(url, json=myobj, headers=header)
    result = json.loads(response.text)

    anger_score = result['emotionPredictions'][0]['emotion']['anger']

    return {
        'anger': anger_score
    }
    
if __name__ == "__main__":
    input_text = input('What is your text? ')
    result = emotion_detector(input_text)
    print(result)