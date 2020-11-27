"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
  
  avarage_school=0
  amount_marks_school=0
  
  info=[
      {'school_class': '4a', 'scores': [3,4,4,5,2]}, 
      {'school_class': '5a', 'scores': [2,4,4,5,3]}, 
      {'school_class': '3a', 'scores': [2,4,2,5,3]},
  ]
  amount_marks_class=[0]*len(info)
  
##Рассчет среднего бала по школе
  for each_scores in info:
    for i in each_scores['scores']:
      avarage_school+=i
      amount_marks_school+=1
  avarage_school/=amount_marks_school
##Рассчет среднего бала по классу
  for number in  range (0,len(info)):
    for mark_class in info[number]['scores']:
      amount_marks_class[number]+=mark_class
    amount_marks_class[number]/=len(info[number]['scores']) 
    info[number]["avarage_class_mark"]=amount_marks_class[number]
    print('Для класса {} средний бал = {}'.format(info[number]["school_class"],amount_marks_class[number]))
  print('Для школы средний бал = {:.2f}'.format(avarage_school))

if __name__ == "__main__":
    main()
