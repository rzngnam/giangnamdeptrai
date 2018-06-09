# question1 = {
#     "question": "1 + 2 =",
#     "choices": ["A.3","B.1","C.2"],
#     "answer": "A"
# }
question_pack = [
    {
        "question": "1 + 2 =",
        "choices": ["A.3","B.1","C.2"],
        "answer": "A"
    },
    {
        "question": "2 + 3 = ",
        "choices": ["A.8","B.5","C.7"],
        "answer":["B"]
    },
    {
        "question": "3 + 4 = ",
        "choices": ["A.3","B.6","C.7"],
        "answer":["C"]
    }
]
# for i in range(3):
#     print(question_pack[i]["question"])
#     print()
#     print(*question_pack[i]["choices"],sep="\n")
#     print()
#     ans = input("answer ?").upper()
#     if ans == question_pack[i]["answer"]:
#         print('bingo')
#     else:
#         print('nah')
# print(question_pack[-1]["answer"][1])
correct_answer_count = 0
causai =[]
i = 1
for q in question_pack:
    print(q["question"])
    print()

    choices = q["choices"]
    print(*q["choices"], sep="\n")
    print()
    user_choice = input("Your answer? ").upper()
    if user_choice == q["answer"]:
        print("Bingo")
        correct_answer_count += 1
    else:
        print("Nah")
        causai.append(i)
        i += 1

percent = (correct_answer_count/len(question_pack))*100
print("{0} correct answer ".format(correct_answer_count))
print(round(percent,2 ),"%")
print("sai ở",*causai,sep = " câu")
if len(causai) > 0:
    print('sai vì mày ngu chứ hỏi tại sao sai ?')

