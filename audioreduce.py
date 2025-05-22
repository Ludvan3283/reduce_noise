from demucs.pretrained import get_model
from demucs.apply import apply_model

# 加载预训练模型
model = get_model(name="htdemucs")

# 分离音轨（人声、鼓、贝斯、其他）
sources = apply_model(model, "noisy_audio.wav")

# 提取人声（假设噪声在"other"轨）
vocals = sources["vocals"]
vocals.export("vocals_only.wav", format="wav")  # 保存纯净人声