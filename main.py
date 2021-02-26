import task_three_exeptions.task_one
import task_three_exeptions.task_two
import task_four_peaceful_bot.bot

TASK = 3
if __name__ == "__main__":
    if TASK == 1:
        task_three_exeptions.task_one.hello_user()
    elif TASK == 2:
        task_three_exeptions.task_two.discounted(1000, 10)
    elif TASK == 3:
        task_four_peaceful_bot.bot.mainloop()