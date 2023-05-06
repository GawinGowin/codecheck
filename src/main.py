def main():
  _ = int(input())
  S = [int(i) for i in input().split(" ")]
  _ = int(input())
  T = [int(i) for i in input().split(" ")]

  count = 0
  for t in T:
    left = S[0]
    right = S[-1]
    if (t > S[-1]) | (t < S[0]):
      break

    while right >= left:
      s = (right + left) // 2
      if t == s:
        count += 1
        break
      elif t < s:
        right = s

      elif t > s:
        left = s

  print(count)


if __name__ == '__main__':
  main()