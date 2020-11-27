"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"}

def ask_user(answers_dict):
  a=0
  user_say=input("Введите вопрос ")
  questions=list(questions_and_answers.keys())
  while (a<len(questions_and_answers)):
    if user_say==questions[a]:
      print(questions_and_answers[user_say])
    a+=1
    
  if user_say not in questions:
    print("Такого вопроса нет,задайте правильно вопрос")
    return ask_user(answers_dict)

    
if __name__ == "__main__":
    ask_user(questions_and_answers)
