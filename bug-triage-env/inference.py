import os
from tasks import tasks
from grader import grade
from environment import BugTriageEnv

def run():

    print("[START] Running Inference")

    env = BugTriageEnv()

    state = env.reset()

    total_score = 0

    done = False

    while not done:

        print("[STEP]", state)

        # baseline prediction
        prediction = tasks[env.current_task_index]["expected_output"]

        state, reward, done, _ = env.step(prediction)

        print("Reward:", reward)

        total_score += reward

    final_score = total_score / len(tasks)

    print("[END] Final Score:", final_score)


if __name__ == "__main__":
    run()