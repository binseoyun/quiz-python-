#파일에 있는 정보를 가져올 수 있는 함수
def load_quiz(filename):
    questions=[]
    with open(filename,'r') as file:
        for line in file:
            question,answer=line.strip().split(';')
            questions.append((question,answer))
    return questions
#정답을 입력받아 점수를 계산하는 함수
def ask_question(questions):
    count=0
    for question,answer in questions:
    
        print(question)
        new_answer=input("정답을 입력하세요")
        if new_answer.lower()==answer.lower():
            count+=1
            print("정답입니다")
        else:
            print("오답입니다")
    return count


    

questions=load_quiz('quiz.txt')
count=ask_question(questions)
print(count)

            




    
    
