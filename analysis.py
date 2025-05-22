import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

y, sr = librosa.load("example.wav")

# 短时傅里叶变换 (STFT)
D = librosa.stft(y)
S_db = librosa.amplitude_to_db(abs(D), ref=np.max)  # 转换为 dB

# 绘制频谱图
plt.figure(figsize=(10, 4))
librosa.display.specshow(S_db, sr=sr, x_axis="time", y_axis="log")
plt.colorbar(format="%+2.0f dB")
plt.title("频谱图")
plt.show()