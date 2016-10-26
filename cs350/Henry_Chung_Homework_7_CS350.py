class agent(object):
    def __init__(self, n, l, g, o): # init is global to the class
        self.speech = n
        self.lists = l
        self.name = g
        self.quote = o
    def check(self, speech, series):
        votes = "vot";kind = "plan";topic = "";topic1 = "";count = 0;
        for i in range(len(speech)):
            if speech[i] == "v":
                for j in range(len(votes)):
                    if speech[i+j] == votes[j]:
                        count  += 1
                        if count == 3:
                            if (topic == "vote" or topic == ""):
                                topic = "vote"
                            else:
                                if (topic != "vote" and topic1 == ""):
                                    topic1 = "vote"
            count  = 0
            if speech[i] == "p":
                for k in range(len(kind)):
                    if speech[i+k] == kind[k]:
                        count  += 1
                        if count == 4:
                            if (topic == "plan" or topic == ""):
                                topic = "plan"
                            else:
                                if (topic != "plan" and topic1 == ""):
                                    topic1 = "plan"
            count = 0
        if topic == "":
            print ("Please select one of the topics to discuss.")
            series = [3]
            return series
        else:
            if ((topic == "plan" and topic1 == "vote") or (topic == "vote" and topic1 == "plan")):
                series = [0,1]

            if (topic == "plan" and topic1 == ""):
                series = [2]
            if (topic == "vote" and topic1 == ""):
                series = [1]
            return series
    def what(self, name, quote, lists):
        try:
            lists[1]
            print (name + ": My goal is to "+ quote[lists[0]] +" by " + quote[lists[1]] + ".")
        except:
            if series[0] == 3:
                print ("What??")
            else:
                print (name + ": My goal is to " + quote[lists[0]] + ".")





x = 1;question = 1;
while x == 1:
    while question == 1:
        locas = raw_input("Do you want to to ask the agent any questions? (y)es or ((n)o or just anything else). >> ")
        if (locas == "y" or locas == "yes" or locas == "yeah" or locas == "1"):
            print("Alright")
        else:
            x = 0; question = 0;
            break
        who = raw_input("Who do you choose, Hillary(1) of Trump(2)? >> ")
        if (who == "Hillary" or who == "hillary" or who == "1"):
            one = "Hillary"
            two = ['supporting woman\'s equality', 'gain the support of parents and woman', 'try a series of new bills to jump start the economy','']
        else: 
            one = "Trump"
            two = ['aim for those who votes', 'gain the support of business owners', 'stop interfering with other contries','']
        print("We have come with a set of answers to your question about Trump and Hillary.")
        print("These questions are about United State's 'voters' and 'plans'.")
        test = raw_input("What is your question? (One question at a time plz.) >> ")
        series = []
        t = agent(test, one,two, series)
        t.check(test,series)
        series = t.check(test, series)
        t.what(one, two, series)
