from random import shuffle
from csv import reader as read

csv_file = open("Verbs.csv", "rb")
reader = read(csv_file)

verbs = {}
sep = "\xc2\xa0or\xc2\xa0"

for row in reader:
    infinitive, s_past, p_participle = row
    if sep in s_past:
        s_past = s_past.split(sep)
    if sep in p_participle:
        p_participle = p_participle.split(sep)
    verbs[infinitive] = {"infinitive": infinitive, "past simple": s_past, "past participle": p_participle}

verbs_list = verbs.keys()
incorrect_verbs = []


def display_options(options, data):
    while True:
        print "What would you like to do?:\n"
        for option in options:
            option_number = options.index(option) + 1
            options_text = str(option_number) + ") " + option["text"]
            print options_text

        option = raw_input("\n")

        if option not in map(format, xrange(1, len(options) + 1)):
            print "Please choose an option from 1 to " + str(len(options))
            continue
        option_ix = int(option) - 1
        msg = options[option_ix]["text"]
        print "You have chose: " + msg
        break
    if option_ix == 0:
        practice_verbs(data)
    elif option_ix == 1:
        practice_verbs(verbs_list)
    else:
        exit()

def display_wrong(resp, verb, tense):
    if type(verbs[verb][tense]) is str:
        print "Wrong, is not " + resp + " it is " + verbs[verb][tense]
    else:
        print "Wrong, is not " + resp + " it is "
        for tense in verbs[verb][tense]:
            print "or " + tense
    return verb

def exit():
    print "Good bye!"
    
    
def practice_verbs(verbs_list):
    shuffle(verbs_list)
    
    incorrect_verbs = []
    
    for verb in verbs_list:

        print "\n\n" + "Give me the correct tenses for " + str(verbs[verb]["infinitive"])
        
        print "infinitive"
        infinitive = ""
        while infinitive == "":
            infinitive = raw_input().strip()

        print "past simple"
        past = ""
        while past == "":
            past = raw_input().strip()
        
        print "past participle"
        past_participle = ""
        while past_participle == "":
            past_participle = raw_input().strip()
        
        right_inf = infinitive in verbs[verb]["infinitive"]
        right_past = past in verbs[verb]["past simple"]
        right_p_participle = past_participle in verbs[verb]["past participle"]
        
        if right_inf:
            print "Right " + infinitive
        else:
            v = display_wrong(infinitive, verb, "infinitive")
            incorrect_verbs.append(v)
            
        if right_past:
            print "Right " + past
        else:
            v = display_wrong(past, verb, "past simple")
            incorrect_verbs.append(v)
            
        if right_p_participle:
            print "Right " + past_participle
        else:
            v = display_wrong(past_participle, verb, "past participle")
            incorrect_verbs.append(v)
    
    fail_dict = {"text": "practice my fail verbs", "verbs_list": incorrect_verbs}
    all_dict = {"text": "practice all verbs", "verbs_list": verbs_list}
    exit_dict = {"text": "exit", "function": exit}
    main_options = [fail_dict, all_dict, exit_dict]
    print incorrect_verbs
    display_options(main_options, incorrect_verbs)

practice_verbs(verbs_list)
