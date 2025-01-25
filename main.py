from ai_training_testing_onefile import AITesting, AITraining
from simulator import Game
import perception
import threading
from queue import Queue

def main():
    g = Game()
    """For each car, run a different AI.
    Also, don't forget to pass in different queues, otherwise
    inputs will get mixed up between cars and AI.
    """
    qInAI = Queue()
    qOutAI = Queue()
    # g.run(visualizer=True, walls=True, useKeys=True)
    gameThread = threading.Thread(target=g.run)
    gameThread.start()
    