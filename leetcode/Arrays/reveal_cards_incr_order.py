class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck_ordered = sorted(deck)

        next_open_index = collections.deque(range(len(deck)))
        deck_game_order = [None] * len(deck)

        for i in deck_ordered:
            deck_game_order[next_open_index.popleft()] = i
            if next_open_index:
                next_open_index.append(next_open_index.popleft())

        return deck_game_order
        
