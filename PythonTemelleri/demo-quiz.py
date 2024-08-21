#Questions

class Questions:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer

    def checkAnswer(self,answer):
        return self.answer==answer

#QUİZ
class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0
    
    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question=self.getQuestion()
        print(f'Soru {self.questionIndex+ 1} : {question.text}')

        for q in question.choices:
            print('-'+q)
        
        answer=input('cevap: ')
        self.guess(answer)
        self.loadQuestions()

    def guess(self,answer):
        question=self.getQuestion()

        if question.checkAnswer(answer):
            self.score +=1
        self.questionIndex +=1

    def loadQuestions(self):
        if len(self.questions)==self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print('score: ',self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber=self.questionIndex + 1
    
        if questionNumber>totalQuestion:
            print('Quiz bitti.')
        else:
            print(f'Question {questionNumber} of {totalQuestion} '.center(100,'*'))

q1=Questions('en iyi programlama dili hangisidir ?',['C#','python','javascript','java'],'python')
q2=Questions('en popüler programlama dili hangisidir ?',['python','javascript','C#','java'],'python')
q3=Questions('en çok kazandıran programlama dili hangisidir ?',['C#','javascript','java','python'],'python')

questions=[q1,q2,q3]
quiz=Quiz(questions)
quiz.loadQuestions()

# print(q1.checkAnswer('python'))
# print(q2.checkAnswer('C#'))