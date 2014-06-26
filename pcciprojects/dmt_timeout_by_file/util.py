def hour_list(selected =None):
  print "selected +++++++"
  print selected
  for i in range(1,31):
    if i<10 :
        i = "0%s" % i
    else :i ="%s" % i
    yield {"value" : i , "selected": True if i == selected else False}


