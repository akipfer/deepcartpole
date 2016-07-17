import random

from pygame.constants import K_LEFT, K_RIGHT

from cartpole import run
from resources.PyGamePlayer.pygame_player import PyGamePlayer


class RandomCartPolePlayer(PyGamePlayer):
    def __init__(self):
        """
        Plays CartPole by choosing moves randomly
        """
        super(RandomCartPolePlayer, self).__init__(run_real_time=True)
        self._last_score = 0

    def get_keys_pressed(self, screen_array, feedback, terminal):
        action_index = random.randrange(3)

        if action_index == 0:
            return [K_LEFT]
        elif action_index == 1:
            return []
        else:
            return [K_RIGHT]

    def get_feedback(self):
        from resources.PyGamePlayer.games.half_pong import score

        # get the difference in scores between this and the last frame
        score_change = score - self._last_score
        self._last_score = score

        if score_change != 0:
            print("Reward: %s" % score_change)

        return float(score_change), score_change == -1

    def start(self):
        super(RandomCartPolePlayer, self).start()

        #run(screen_width=640, screen_height=480)
        run()


if __name__ == '__main__':
    player = RandomCartPolePlayer()
    player.start()
