class Person:
  def __init__(obj):
    obj.recruits = []
  def recruit (self, otherPerson):
    self.recruits.append(otherPerson)
  def getLoserCount (self):
    if len(self.recruits) == 0:
      return 1
    ans = 0
    for i in range(len(self.recruits)):
      ans += self.recruits[i].getLoserCount()
    return ans