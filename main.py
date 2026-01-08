from agent import LlmAgent

if __name__ == "__main__":
  agent = LlmAgent()
  reply = agent.handle("사용자", "안녕")
  print("응답:", reply)

def get_weather (location):
  if location == "서울":
    return "맑음"
  return "모름"