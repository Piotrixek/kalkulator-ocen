def calculate_mean(grades):
  total = 0
  for grade in grades:
    if grade[-1] == '+':
      total += float(grade[:-1]) + 0.5
    elif grade[-1] == '-':
      total += float(grade[:-1]) - 0.5
    else:
      total += float(grade)
  return total / len(grades)

def input_grades():
  grades = []
  while True:
    grade = input("Podaj ocenę (lub wpisz 'koniec', aby zakończyć): ")
    if grade == "koniec":
      break
    grades.append(grade)
  return grades

# Przykładowe użycie funkcji
grades = input_grades()
mean = calculate_mean(grades)
print(f"Średnia ocen to: {mean:.2f}")
