from sqlalchemy import update
from sqlalchemy.orm import Session

from models.solution_model import Solution, SolutionSchema


class Repository:
    model = Solution

    def __init__(self, session: Session):
        self.session = session
    
    def update_solution(self, solution: SolutionSchema):
        stmt = update(
            self.model
            ).where(
                self.model.user_id == solution.user_id,
                self.model.task_id == solution.task_id
            ).values(
                status=solution.status,
                traceback=solution.traceback
            )
        self.session.execute(stmt)
        self.session.commit()
        