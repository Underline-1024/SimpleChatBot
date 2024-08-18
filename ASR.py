import pyaudio
import wave
import time
#from funasr import AutoModel
#import model
import librosa
import numpy as np
# paraformer-zh is a multi-functional asr model
# use vad, punc, spk or not as you need

# model = AutoModel(model="paraformer-zh",  vad_model="fsmn-vad", punc_model="ct-punc", 
#                   # spk_model="cam++"
#                   )

def asr(duration, filename):
    # 实例化一个PyAudio对象
    pa = pyaudio.PyAudio()
    # 打开声卡，设置 采样深度为16位、声道数为2、采样率为16、输入、采样点缓存数量为2048
    stream = pa.open(format=pyaudio.paInt16, channels=2, rate=16000, input=True, frames_per_buffer=2048)
    # 新建一个列表，用来存储采样到的数据
    record_buf = [] 
    start_time = time.time()
    while time.time()-start_time < duration:
            audio_data = stream.read(2048)      # 读出声卡缓冲区的音频数据
            record_buf.append(audio_data)       # 将读出的音频数据追加到record_buf列表
            print('*')
            wf = wave.open(filename, 'wb')          # 创建一个音频文件，名字为“01.wav"
            wf.setnchannels(2)                      # 设置声道数为2
            wf.setsampwidth(2)                      # 设置采样深度为
            wf.setframerate(16000)                  # 设置采样率为16000
            # 将数据写入创建的音频文件
            wf.writeframes("".encode().join(record_buf))
            # 写完后将文件关闭
            wf.close()

    # 录制音频
    #判断数据中是否有人声
    y, sr = librosa.load(filename)
    threshold = 45
    energy=np.sum(np.abs(y)**2)
    while energy > threshold:
        # 实例化一个PyAudio对象
        pa = pyaudio.PyAudio()
        # 打开声卡，设置 采样深度为16位、声道数为2、采样率为16、输入、采样点缓存数量为2048
        stream = pa.open(format=pyaudio.paInt16, channels=2, rate=16000, input=True, frames_per_buffer=2048)
        start_time = time.time()
        while time.time()-start_time < duration:
            record_buf1=[]
            print(time.time()-start_time)
            # 实例化一个PyAudio对象
            pa = pyaudio.PyAudio()
            # 打开声卡，设置 采样深度为16位、声道数为2、采样率为16、输入、采样点缓存数量为2048
            stream = pa.open(format=pyaudio.paInt16, channels=2, rate=16000, input=True, frames_per_buffer=2048)

            audio_data = stream.read(2048)      # 读出声卡缓冲区的音频数据
            record_buf.append(audio_data)       # 将读出的音频数据追加到record_buf列表
            record_buf1=audio_data
            print('*')
            wf = wave.open(filename, 'wb')          # 创建一个音频文件，名字为“01.wav"
            wf.setnchannels(2)                      # 设置声道数为2
            wf.setsampwidth(2)                      # 设置采样深度为
            wf.setframerate(16000)                  # 设置采样率为16000
            # 将数据写入创建的音频文件
            wf.writeframes("".encode().join(record_buf))

            wf = wave.open("de.wav", 'wb')          # 创建一个音频文件，名字为“01.wav"
            wf.setnchannels(2)                      # 设置声道数为2
            wf.setsampwidth(2)                      # 设置采样深度为
            wf.setframerate(16000)                  # 设置采样率为16000
            # 将数据写入创建的音频文件
            wf.writeframes("".encode().join(record_buf))

            # 写完后将文件关闭
            wf.close()
            # 停止声卡
            stream.stop_stream()
            # 关闭声卡
            stream.close()
            # 终止pyaudio
            pa.terminate()

            y, sr = librosa.load("de.wav")
            energy=np.sum(np.abs(y)**2)
    # res = model.generate(input=filename, 
    #             batch_size_s=300)
    # return res[0]['text']
asr(3, "output.wav")