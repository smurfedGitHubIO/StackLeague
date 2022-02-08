def likedIt(likers):
  if len(likers) == 0:
    return "Nobody likes this post"
  elif len(likers) == 1:
    return likers[0] + " likes this post"
  elif len(likers) == 2:
    return likers[0] + " and " + likers[1] + " like this post"
  elif len(likers) == 3:
    return likers[0] + ", " + likers[1] + " and " + likers[2] + " like this post"
  return likers[0] + ", " + likers[1] + " and " + str(len(likers) - 2) + " others like this post"
