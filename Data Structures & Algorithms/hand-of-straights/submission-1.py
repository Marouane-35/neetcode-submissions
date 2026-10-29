from collections import Counter
class Solution:

  def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
    if len(hand) % groupSize != 0:
      return False

    counts = Counter(hand)

    for card in sorted(counts):
      count = counts[card]
      if count > 0:
        for i in range(card, card + groupSize):
          if counts[i] < count:
            return False
          counts[i] -= count

    return True