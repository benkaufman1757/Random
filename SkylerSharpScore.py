'''Find the sharps!'''
import random
from typing import List
from bisect import bisect_left

def bet_outcome(wager_amount:float, odds:float) -> float:
    '''return the outcome of the wager'''
    if 1/odds < random.random():
        return wager_amount * odds
    return -wager_amount

def get_wager(min_wager:int=1, max_wager:int=100) -> float:
    '''assume the person betting wagers a random amount'''
    # change wager distribution here random.normal, etc.
    return min_wager + (random.random() * max_wager)

def get_wager_amounts(min_wager:int=1, max_wager:int=100, n:int=10_000) -> List[float]:
    '''get a bunch of wagers'''
    return [get_wager(min_wager, max_wager) for _ in range(n)]

def get_odds() -> float:
    '''get random odds for events'''
    return 1/random.random()

def get_odds_amounts(n:int=10_000) -> List[float]:
    '''get a bunch of random odds for events'''
    return [get_odds() for _ in range(n)]

def simulate(wagers:List[float], odds:List[float]) -> List[float]:
    '''given a list of wages and odds return the amount of money a player makes for each event'''
    if len(wagers) != len(odds):
        raise Exception(f'Length of wagers does not equal length of odds: {len(wagers)} != {len(odds)}')
    return [bet_outcome(wager, odd) for wager, odd in zip(wagers, odds)]

def score_user(wagers:List[float], odds:List[float], actual_payout:float, n_simulations:int=1_000) -> float:
    '''
        Given wagers and odds and the actual outcomes for a user return
        the percentile they end up in compared N many uniform random outcomes
    '''
    simulated_payouts = []
    for _ in range(n_simulations):
        simulation_results = simulate(wagers, odds)
        simulated_payouts.append(sum(simulation_results))
    sorted_payouts = sorted(simulated_payouts)
    return bisect_left(sorted_payouts, actual_payout) / len(sorted_payouts)

def main() -> None:
    '''Create random wagers and random odds with random payouts and see where this user ends up'''
    actual_wagers = get_wager_amounts()
    actual_odds = get_odds_amounts()
    actual_payouts = simulate(actual_wagers, actual_odds)
    # numbers closer to 1 indicate that a person betting is really good
    print(score_user(actual_wagers, actual_odds, sum(actual_payouts)))

if __name__ == "__main__":
    main()
