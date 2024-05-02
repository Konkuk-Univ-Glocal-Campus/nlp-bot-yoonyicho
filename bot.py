import random

# This list contains the random responses (you can add your own or translate them into your own language too)
random_responses = ["정말 흥미롭네요, 더 말씀해주세요.",
                    "알겠습니다, 계속 말씀해주세요.",
                    "왜 그렇게 말씀하시나요?",
                    "요즘 날씨가 참 묘하죠?",
                    "주제를 바꿔볼까요?",
                    "어제밤 경기 보셨나요?"]

print("안녕하세요, 저는 마빈이라고 하는 간단한 로봇입니다.")
print("이 대화를 언제든지 '안녕'이라고 입력하면 종료할 수 있습니다.")
print("답변을 입력하고 엔터 키를 누르세요.")
print("오늘 기분은 어떠신가요?")

while True:
    # wait for the user to enter some text
    user_input = input("> ")
    if user_input.lower() == "안녕":
        # if they typed in 'bye' (or even BYE, ByE, byE etc.), break out of the loop
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("대화해주셔서 감사합니다, 안녕히 가세요!")
