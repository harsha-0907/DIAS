from gtts import gTTS
import boto3
import os
import Twillio


def generateAudio(mytext):
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    name = "file1.mp3"
    myobj.save(name)
    os.system(name)
    print("Audio Generated")
    return name


def sendToS3Instance(file, bucket_name="bucket-2234"):
    s3 = boto3.client('s3', region_name='ap-south-2')
    s3.upload_file(file, bucket_name, file)
    audio_url_new = s3.generate_presigned_url('get_object', Params={'Bucket': bucket_name, 'Key': file}, ExpiresIn=3600)
    print(audio_url_new)
    return audio_url_new


def completeProcess(text):
    _ = generateAudio(text)
    audio_url = sendToS3Instance(_)
    Twillio.call(audio_url, "+919494517819")


