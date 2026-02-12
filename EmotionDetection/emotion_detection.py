import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document" :{ "text" : text_to_analyze } }
    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    result = json.loads(response.text)

    anger_score = float(result['emotionPredictions'][0]['emotion']['anger'])
    disgust_score = float(result['emotionPredictions'][0]['emotion']['disgust'])
    fear_score = float(result['emotionPredictions'][0]['emotion']['fear'])
    joy_score = float(result['emotionPredictions'][0]['emotion']['joy'])
    sadness_score = float(result['emotionPredictions'][0]['emotion']['sadness'])
    
    dominant_emotion = ''
    highest_emotion = 0
    for key, value in result['emotionPredictions'][0]['emotion'].items():
        if value > highest_emotion:
            highest_emotion = value
            dominant_emotion = key

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

if __name__ == "__main__":
    input_text = input('What is your text? ')
    result = emotion_detector(input_text)
    print(result)