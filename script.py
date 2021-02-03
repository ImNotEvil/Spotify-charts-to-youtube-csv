from youtube_search import YoutubeSearch
import json
import os.path


fname = "regional-global-weekly-2016-12-30--2017-01-06"

def get_id(r) :
        return(json.loads(YoutubeSearch(r, max_results=1).to_json())['videos'][0]['id'])

tableau = []
tableau_fail = []

if (os.path.isfile(fname+'.csv')):
        f = open(fname+'.csv', "r")

        f.readline()
        f.readline()
        ligne = f.readline()

        while ligne != "" :
                
                tab = ligne.split(',')
                print(tab)
                try :
                        i = tab[0]
                        a = tab[1].replace('"','')
                        t = tab[2].replace('"','')
                        recherche = '{} {} audio'.format(a,t)
                        vid_id = get_id(recherche)
                        tableau.append( {"num" : i,"titre" : t, "artiste" : a, "vid_id" : vid_id } )
                        ligne = f.readline()
                except :
                        print("FAIL")
                        tableau_fail.append(tab)
        f.close()

        text = json.dumps(tableau, indent=4, separators=(",", ":"))

        f2 = open(fname+'.json', "w")
        f2.write(text)
        f2.close()
        print("Liste des fails\n",tableau_fail)
                
else : print("File do not exists")
