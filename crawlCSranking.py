import pandas as pd
from utils import *
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
if __name__=='__main__':
    choiceMap={names.strip().split('\n')[i]:choices[i] for i in range(len(choices)) }
    printChoice='\n'.join([ item[0].strip()+'\t\t\t\t'+item[1] for item in choiceMap.items()])
    print('choices are:\n\n ', printChoice)
    userChoices=input('input your choices(e.g. nlp&arch&sec): ').lower()

    path = userChoices
    if not os.path.exists(path):
        os.mkdir(path)


    base_url='http://csrankings.org/#/index?'
    trs=crawlPage(userChoices,base_url)


    Universities=[]
    for i in range(0,len(trs),3):
        uBlock=trs[i:i+3]
        Universities.append([uBlock[0],uBlock[-1]])

    #get university information
    Universities=pd.DataFrame(Universities)
    Universities.columns=['school','profs']
    Universities.school=Universities.school.apply(lambda x: getUInfo(x))
    Universities=pd.concat([Universities.school.str.split('@',expand=True),Universities.profs],axis=1)
    Universities.columns=['rank','Uname','count','faculty','profs']
    print(Universities.head())
    # save University information
    Universities.iloc[:,[0,1,2]].to_csv(os.path.join(path,'universities.csv'),index=False)
    print('successfully save university infos')

    #get Professor information
    dfs=[pd.DataFrame(getUProfsInfos(prof),columns=['pname','homepageLink','pubs','ajds']) for prof in Universities.profs]
    for index,df in enumerate(dfs):
        df['Uname']=Universities.Uname[index]
    allProf=pd.concat(dfs)
    #save professor information
    allProf.to_csv( os.path.join(path,'ProfsInfos.csv'),index=False)
    print('successfully saved profsinfos')