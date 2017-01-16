"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
1) Encapsulation - this means that data and functions that manipulate the date are bound together. They will not be effected by outside inteference.
2) Abstraction - One does not need to know exactly what is happening in a class method. Through abstraction, the method can simply be called upon.
3) It is easy to make different types of a class. For example, I can make a class Humans, and make many types of humans once teh class Humans has been defined.

2. What is a class?
    A class is a type of thing. eg. the class of 2 is an integer, and the class of "Ray" is a string.

3. What is an instance attribute?
    This is an attribute for an individual occurance of a class.

4. What is a method?
    A method is essentially a function that is defined on a class.

5. What is an instance in object orientation?
    An instance or an object is a individual occurance of a type of thing. it can be made by calling the class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   A class attribute applies to every single instance of that class. An instant attribute might be different for each different instant.
   Eg. a class attribute for the class Humans may be that they have 10 fingers. Whereas the istant attribute may be the hair color which could vary for each instant in the class Humans.


"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        question = raw_input(self.question)
        if question == self.correct_answer:
            return True
        else:
            return False


class Exam(Question):

    def __init__(self, name):
        self.name = name
        self.questions_lst = []

    def add_question(self, question, correct_answer):
        dict_quest_answer = {}
        dict_quest_answer["question"] = question
        dict_quest_answer["correct_answer"] = correct_answer
        self.questions_lst.append(dict_quest_answer)
        return self.questions_lst

    def administer(self):
        score = 0
        for q in self.questions_lst:
            self.question = q["question"]
            self.correct_answer = q["correct_answer"]
            if super(Exam, self).ask_and_evaluate():
                score += 1
        return score


def take_test(exam, student):
    exam = Exam(student)
    exam.score = exam.administer()
    print exam.score


def example(student_name, student_lastname, student_address):
    exam = Exam(student_name)
    exam.add_question("What is 2+2", 4)
    exam.add_question("What color is a rose?", "red")
    student = Student(student_name, student_lastname, student_address)
    take_test(exam, student)


class Quiz(Exam):

    def __init__(self, name):
        self.name = name
        self.questions_lst = []

    def add_question(self, question, correct_answer):
        self.questions_lst = super(Quiz, self).add_question(question, correct_answer)

    def administer(self):
        number_questions = len(self.questions_lst)
        score = number_questions
        print score
        for q in self.questions_lst:
            self.question = q["question"]
            self.correct_answer = q["correct_answer"]
            if super(Exam, self).ask_and_evaluate() is False:
                score = score - 1
        if score >= number_questions/2.0:
            return True
        else:
            return False
