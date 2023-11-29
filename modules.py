# module = a file contain python code.may contain functions,classes,etc.
# used with modular programming , which is to separate a program into parts

import messages as msg# dodali drugi file u ovaj onda dole pozivam osta zelimo iz file messages tj koju funkciju ovdje
# or na ovaj nacin upload file u ovaj file
from messages import hello,bye #or * sve dodati sa zvezdom a ovako samo funkciju hello i bye



msg.hello() # pozvali funkciju hello iz file messages

msg.bye()