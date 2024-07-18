import sys
#문제를 푸시겠습니까? 라는 질문에 y를 하면 위의 물음 처럼 문제 풀이, n을 하면 퀴즈를 출제하시겠습니까? 라는 질문, y를 하면 퀴즈를 출제할 수 있게 민듦. n하면 종료하겠습니다 라는 멘트와 함께 종료

class ask:
    def __init__(self,filename):
        self.filename=filename
        self.determine()
        
    def determine(self):
      answer=input("문제를 푸시겠습니까?(y or n):")
      if answer.lower()=='y':
          self.solve_quiz()
      elif answer.lower()=='n':
          answer2=input("문제를 만드시겠습니까?:")
          if answer2.lower()=='y':
              self.make_quiz()
          elif answer2.lower()=='n':
              print("프로그램을 종료하겠습니다")
              sys.exit() #프로그램 종료
          else:
              print("잘못된 입력입니다")
      else:
         print("입력이 잘못되었습니다")
              
              

    def make_quiz(self): #파일에 퀴즈를 작성하는 함수(한줄씩 작성, ;라는 기호로 질문과 답변을 구분하라는 안내 문구 작성)
      print("질문;답변 형식으로 퀴즈를 작성하시오(종료하려면 exit 입력)")
      with open(self.filename,'a',encoding='utf-8') as file:
         while True:
             new_quiz=input("질문;답변 형식으로 퀴즈를 작성하시오")
             if new_quiz.lower()=='exit':
                 break
             if ';' in new_quiz:
                 
               file.write('\n'+new_quiz+'\n') #file.write는 end=""인자를 받지 않음
             else:
                 print("잘못된 형식입니다.'질문;답변'형식으로 입력하시오")
        
        
    def load_quiz(self): #파일에 있는 정보를 가져올 수 있는 함수
     questions=[]
     try:
      with open(self.filename,'r') as file:
        for line in file:
            question,answer=line.strip().split(';')
            questions.append((question,answer))
     except FileNotFoundError:
         print(f"파일 {self.filename}을 찾을 수 없습니다") #파일이 존재하지 않는 경우 대비
     self.questions=questions
     return self.questions


    def ask_question(self): #정답을 입력받아 점수를 계산하는 함수
    
     count=0
     for question,answer in self.questions:
    
        print(question)
        new_answer=input("정답을 입력하세요")
        if new_answer.lower()==answer.lower():
            count+=1
            print("정답입니다")
        else:
            print("오답입니다")
     return count

    def solve_quiz(self):
        questions=self.load_quiz()
        if questions:
            score=self.ask_question()
            print(f"정답수:{score}")
        else:
            print("모든 문제를 다 풀었습니다")
   
         
if __name__=="__main__":         
   q=ask('quiz.txt')
   q.determine()
