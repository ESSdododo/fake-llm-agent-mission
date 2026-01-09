from psutil import users
from pyexpat.errors import messages


class LlmAgent:
  def handle(self, user, message):
    # 아주 단순한 LLM 흉내
    return f"{user}님, '{message}' 잘 받았습니다 hi I'm SJ."
    if "날씨" in message:
      weather = get_weather("서울")
      return  f"{user}님, 서울의 날씨는 '[weather]' 입니다."

    return f"{user}님, '{message} 잘 받았습니다."