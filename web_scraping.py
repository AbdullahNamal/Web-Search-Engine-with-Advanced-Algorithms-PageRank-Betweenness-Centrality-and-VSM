class webscraping:
    import os
    from bs4 import BeautifulSoup
    import networkx as nx   
    import matplotlib.pyplot as plt

    def __init__(self):
        
        # directory where all html files are located
        self.directory = webscraping.os.fsencode('files')
        
        
    """returns names of files"""
    def give_files_name(self):
        file_list = []
        for file in webscraping.os.listdir(self.directory):
            file_list.append(webscraping.os.fsdecode(file))
            
        return file_list
        
        
    """all sites refering to a site forms the authority for that site"""
    def inlinks(self,filename = None):
        Edges = []
        
        for files in webscraping.os.listdir(self.directory):
            filepath = webscraping.os.path.join(self.directory, files)
            filename1 = webscraping.os.fsdecode(files)
            with open(filepath,'r') as home_file:
                content = home_file.read()
                soupinstance = webscraping.BeautifulSoup(content,'lxml')
                anchortags = soupinstance.find_all('a')                
                for anchor in anchortags:
                    if anchor.get('href') == filename:
                        Edges.append(filename1)
                        
        return Edges
                
    
    # a site refering to other sites forms the hub fr other sites. 
    def outlinks(self,filename = None):
        edges = []
        filename = str.encode(filename)
        filepath = webscraping.os.path.join(self.directory, filename)
        with open(filepath,'r') as home_file:
            content = home_file.read()
            soupinstance = webscraping.BeautifulSoup(content,'lxml')            
            anchortags = soupinstance.find_all('a')            
            for anchor in anchortags:
                    edges.append(anchor.get('href'))

        return edges

    
    def plot(self,edges = None,nodes = None):
        G = webscraping.nx.DiGraph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)
        webscraping.nx.draw(G,with_labels=True,node_color = 'r',edge_color = 'g',arrowsize = 25,node_size = 1000)
        webscraping.plt.show()
    

class PageRank:
    
    def __init__(self):
        self.convergence_score = 0
    
    """check whether convergence is approached or not"""
    def check_convergence(self,new_rank = None,old_rank = None):
        flag = True
        for i in range(len(new_rank)):
            if new_rank[i] == old_rank[i]:
                pass
            else:
                flag = False
                break 
        if flag == True:
            self.convergence_score += 1
    
    
    """pagerank calculation function"""
    def PageRank(self,filename = None,inlinks = None,outlinks = None):
        self.rank = [1] * len(filename)
        self.convergence_steps  = 0 
        while True:
            temp = []
            old_rank = self.rank
            for i in range(len(filename)):
                sum = 0
                for j in range(len(inlinks[i])):
                    sum += (self.rank[filename.index(inlinks[i][j])] / len(outlinks[filename.index(inlinks[i][j])]))
                temp.append(round((1 - 0.85) + 0.85 * sum,2))
            self.rank = temp
            self.check_convergence(new_rank = self.rank, old_rank = old_rank)
            self.convergence_steps += 1
            if self.convergence_score == 3:
                return self.convergence_steps, self.rank
            


                
