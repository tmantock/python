def arrayPairSum(nums):
  """
  :type nums: List[int]
  :rtype: int
  """
  # To get the min of the pair sort the list, so it is in order
  # Skip every ofter element in the list, so you only get the MIN ex[MIN, MAX, MIN, MAX] => [MIN, MIN]
  # Sum the mins
  return sum(sorted(nums)[::2])
