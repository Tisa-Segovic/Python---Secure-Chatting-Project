from time import *
import random
DELAY_BOUND = 10

# error-correct the punctuation and other characters potentially mistakenly entered by the user 'blah,.,,.' to 'blah'
def word_cleanup(wd):
    wd = wd.lower()
    last_char = wd[-1]
    while not last_char.isalnum():
        wd = wd[:-1]
        if len(wd) > 0:
            last_char = wd[-1] 
        else:
            break
    return wd
    
# replace 'blah' with '*blah*'
def proc_message(key, msg):
    new_key = '*' + key + '*'
    # the following line doesn't work, it will do things like f*or* for 'or'
    # new_msg = msg.lower().replace(key, new_key)
    new_msg = ''
    for wd in msg.split():
        wd = wd.lower().replace(key, new_key)
        new_msg += wd + ' '
    new_msg = new_msg.rstrip()
    return new_msg

# adding the timestamp to a message
def inc_wtime(last_time):
    last_time_sec   = mktime(strptime(last_time))
    this_time_sec   = last_time_sec + float(random.randint(1, DELAY_BOUND))
    this_time       = asctime(gmtime(this_time_sec))
    return this_time

# adding the timestamp to every message, to know the message's metadata
def add_wtime(in_file_name):
    in_file     = open(in_file_name, 'r')
    out_file    = open(in_file_name + '.time', 'w') 
    now = ctime()
    m   = in_file.readline()
    while m != '':
        new_m   = inc_wtime(now) + '**\t ' + m
        out_file.write(new_m)
        m       = in_file.readline()
        
    in_file.close()
    out_file.close()
