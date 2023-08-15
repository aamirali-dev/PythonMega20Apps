import collections.abc
from dataclasses import dataclass


@dataclass
class JobApplicant:
    applicant_id: int
    years_of_experience: int
    is_recommended: bool
    first_interview_score: float
    second_interview_score: float

    @property
    def score(self):
        result = self.years_of_experience / 2 \
            + int(self.is_recommended) \
            + self.first_interview_score / 2 \
            + self.second_interview_score

        return round(result, 2)


class JobApplicantPool(collections.abc.Sequence):
    def __init__(self, pool=None):
        self.pool = pool
        if self.pool is None:
            self.pool = []

    def __getitem__(self, index: int):
        return self.pool[index]

    def __len__(self):
        return len(self)

    def __repr__(self):
        pl = sorted(self.pool, reverse=True, key=lambda applicant: applicant.score)
        result = f'Applicant Pool \n (Score | ID) \n' + '-' * 20
        for ap in pl:
            result += f'\n{ap.score} - {ap.applicant_id}'
        return result

    def add(self, applicant):
        self.pool.append(applicant)


a1 = JobApplicant(1234, 5, False, 3.1, 4.6)
a2 = JobApplicant(6799, 10, False, 3.1, 7.4)
p1 = JobApplicantPool([a1, a2])
print(p1)
