Student_1 = {
              "Maths":45,
              "Science":75,
              "Social":96,
              "Name": "David"
          }

Student_2 = {
              "Maths":74,
              "Science":83,
              "Social":100,
              "Name": "Clancy"
          }

Student_3 = {
              "Maths":98,
              "Science":62,
              "Social":23,
              "Name": "John"
          }

student_list = [Student_1, Student_2, Student_3]

def Results_score_board (student_list):
    Highest_marks_in_maths = 0
    Highest_marks_in_maths_name = ''
    for student in student_list:
        if (student.get("Maths") > Highest_marks_in_maths):
            Highest_marks_in_maths = student.get("Maths")
            Highest_marks_in_maths_name = student.get("Name")

    print(f"The highest scorer in maths is {Highest_marks_in_maths} by {Highest_marks_in_maths_name}")

Results_score_board(student_list)