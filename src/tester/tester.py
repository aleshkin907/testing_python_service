import os
import shutil
import subprocess

from models.solution_model import SolutionSchema
from repositories.solution_repository import Repository


class Tester:
    def __init__(self, repository: Repository):
        self.repository = repository

    def test_solution(self, solution: SolutionSchema):
        directory_name = f"{solution.user_id}_{solution.task_id}"
        os.makedirs(directory_name, exist_ok=True)

        solution_file_name = "solution.py"
        unit_test_file_name = "test.py"

        create_file(directory_name, solution_file_name, solution.solution)
        create_file(directory_name, unit_test_file_name, "from solution import *\n" + solution.unit_test)

        result = subprocess.run(["python", unit_test_file_name], capture_output=True, text=True, cwd=directory_name)
        err = result.stderr

        if "OK" in err:
            solution.status = "completed"
            solution.traceback = err
        else:
            solution.status = "failed"
            solution.traceback = err
        
        self.repository.update_solution(solution)
        
        shutil.rmtree(os.path.join(directory_name))


def create_file(dir_name: str, file_name: str, content: str):
    with open(os.path.join(dir_name, file_name), 'w') as f:
        f.write(content)
