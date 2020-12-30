from utils import *
import pandas as pd
import os
choices="ai&vision&mlmining&nlp&ir&arch&comm&sec&mod&hpc&mobile&metrics&ops&plan&act&crypt&log&graph&chi&robotics&bio&da&bed&visualization&ecom&visualization".split('&')
names='''
Artificial intelligence
Computer vision
Machine learning & data mining
Natural language processing
The Web & information retrieval     
Computer architecture
Computer networks
Computer security
Databases
Design automation
Embedded & real-time systems  
High-performance computing
Mobile computing
Measurement & perf. analysis 
Operating systems
Programming languages
Software engineering
Algorithms & complexity
Cryptography
Logic & verification
Comp. bio & bioinformatics
Computer graphics
Economics & computation
Human-computer interaction
Robotics
Visualization
'''
choiceMap={names.strip().split('\n')[i]:choices[i] for i in range(len(choices)) }
printChoice='\n'.join([ item[0].strip()+'\t\t\t\t'+item[1] for item in choiceMap.items()])
print('choices are:\n\n ', printChoice)
userChoices=input('input your choices(e.g. nlp&arch&sec): ')


path=userChoices
# path='nlp&sec'
try:
    allProf=pd.read_csv( os.path.join(path,'ProfsInfos.csv'))
except:
    print('you haven\'t crawl that choices, please run crawlCSranking first')
    exit(1)

emailsOfU=homepage2email(allProf.homepageLink)

allemails=['#'.join([pattern[0].strip() for pattern in email if pattern]) for email in emailsOfU]
emails=pd.Series(allemails)
allProf['emails']=emails
allProf.to_csv(os.path.join(path,'ProfsInfosWithEmails.csv'),index=False)

