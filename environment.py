# environment.py

from tasks import tasks

class BugTriageEnv:

    def __init__(self):
        self.current_task_index = 0
        self.done = False

    def reset(self):
        self.current_task_index = 0
        self.done = False
        return self.state()

    def state(self):
        return {
            "task": tasks[self.current_task_index]["description"],
            "input": tasks[self.current_task_index]["input"]
        }

    def step(self, action):

        current_task = tasks[self.current_task_index]
        expected = current_task["expected_output"]

        reward = 0.0

        # reward logic
        if action.lower() == expected.lower():
            reward = 1.0
        elif expected.lower() in action.lower():
            reward = 0.5
        else:
            reward = -0.2

        # move to next task
        self.current_task_index += 1

        if self.current_task_index >= len(tasks):
            self.done = True

        return self.state(), reward, self.done, {}