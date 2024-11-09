import random

job_list = {
    "teacher": {"salary": 150, "gladness_less": 10},
    "boss": {"salary": 400, "gladness_less": 5},
    "ninja": {"salary": 1000, "gladness_less": 40},
}

class Job:
    def __init__(self, job_list):

        self.job = random.choice(list(job_list))
        print(self.job)
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']

