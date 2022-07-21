# SENTIMENTAL ANALYSIS ON MAJOR ANTI-HYPERTENNSIVE DRUGS

### 1.1 Objective
The objective of this project is to carry out sentimental analysis on commonly prescribed anti-hypernsive drugs in the united state. Build a webapp that either reassure user of these drugs based on review sentiment. Anti hypertensive drugs used are
- Amlodipine ```Brand names: Norvasc, Katerzia, Norliqva```
- Metoprolol ```Brand names: Metoprolol Succinate ER, Metoprolol Tartrate, Lopressor, Toprol-XL```
- Lisinopril ```Brand names: Zestril, Prinivil, Qbrelis``` 
- Losartan ```Brand names: Cozaar```
- Furosemide ```Brand names: Lasix, Diaqua-2, Lo-Aqua```


### 1.2 Data Source
- The data set used in notebook was scraped from 
    - https://www.drugs.com/
    - https://www.askapatient.com/
- Scraping script can be found here

### 1.3 Result Peak
![word cloud](assets/wc.png)
![review length](assets/l.png)
![drugs](assets/dg.png)
![ratings](assets/tr.png)
![sideeffect](assets/se.png)

### 1.4 Challenges
Challenges face while get these review sentitments are 
- Most user are using these drug with combination of other drugs for other co morbidities
- Users are on diffrent dosage
- Druration of use are diffrent for users
- Some review are sarcastic and  aspected base
- Most expected side effect are consider as adverse effect by users

### 1.5 Performance
 Over all text bold sentiment polarity and nltk sentiment analyser did perform better than bert



 


