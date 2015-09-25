from random import shuffle
verbs = {"be": 		{"infinitive": "be", 		"past simple": ["was", "were"],			"past particle": "been"},
        "beat": 	{"infinitive": "beat",	 	"past simple": "beat",				"past particle": "beaten"},
        "become": 	{"infinitive": "become", 	"past simple": "became",			"past particle": "become"},
        "begin": 	{"infinitive": "begin",		"past simple": "began",				"past particle": "begun"},
        "bend": 	{"infinitive": "bend", 		"past simple": "bent",				"past particle": "bent"},
        "bet": 		{"infinitive": "bet", 		"past simple": "bet",				"past particle": "bet"},
        "bind": 	{"infinitive": "bind", 		"past simple": "bound",				"past particle": "bound"},
        "bite": 	{"infinitive": "bite", 		"past simple": "bite",				"past particle": "bite"},
        "blow": 	{"infinitive": "blow", 		"past simple": "blew",				"past particle": "blown"},
        "break":	{"infinitive": "break", 	"past simple": "broke",				"past particle": "broken"},
        "bring":	{"infinitive": "bring", 	"past simple": "bent",				"past particle": "bent"},
        "broadcast":	{"infinitive": "broadcast",	"past simple": "broadcast",			"past particle": "broadcast"},
        "build":	{"infinitive": "build",		"past simple": "built",				"past particle": "built"},
        }

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

        if opction not in map(format, xrange(1, len(options) + 1)):
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
        print "Wrong, is not " + resp + "it is " + verbs[verb][tense]
    else:
        print "Wrong, is not " + resp + "it is "
        for tense in verbs[verb][tense]:
            print "or " + tense
    return verb

def exit():
    print "Good bye!"
    
    
def practice_verbs(verbs_list):
    shuffle(verbs_list)
    
    incorrect_verbs = []
    
    for verb in verbs_list:
        right_inf = False
        right_past = False
        right_p_particle = False
        
        print "\n\n" + "Give me the correct tenses for " + str(verbs[verb]["infinitive"])
        
        print "infinitive"
        infinitive = raw_input()
        
        print "past simple"
        past = raw_input()
        
        print "past particle"
        past_particle = raw_input()
        
        right_inf = infinitive in verbs[verb]["infinitive"]
        right_past = past in verbs[verb]["past simple"]
        right_p_particle = past_particle in verbs[verb]["past particle"]
        
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
            
        if right_p_particle:
            print "Right " + past_particle
        else:
            v = display_wrong(past_particle, verb, "past particle")
            incorrect_verbs.append(v)
    
    fail_dict = {"text": "practice my fail verbs", "function": practice_verbs}
    all_dict = {"text": "practice all verbs", "function": practice_verbs}
    exit_dict = {"text": "exit", "function": exit}
    main_options = [fail_dict, all_dict, exit_dict]
    print incorrect_verbs
    display_options(main_options, incorrect_verbs)

practice_verbs(verbs_list)
