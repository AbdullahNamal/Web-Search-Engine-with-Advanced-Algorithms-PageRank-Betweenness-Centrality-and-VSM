class search:
    import customtkinter as ctk
    import os
    
    def __init__(self):
        search.ctk.set_appearance_mode('dark')
        search.ctk.set_default_color_theme('dark-blue')
        self.root = search.ctk.CTk()
        self.root.geometry('1400x768')
        self.root.title('search engine')
        label = search.ctk.CTkLabel(self.root,text = 'enter your query here',font = ('typescript',40))
        label.place(x = 500,y = 200)
        entry = search.ctk.CTkEntry(self.root,placeholder_text='Abdullah',font = ('noto-sans',20),width = 500)
        entry.place(x = 480,y = 280)        
        button = search.ctk.CTkButton(self.root,text = 'search',command = lambda:self.new_window(),font = ('noto-sans',20),height = 20,width = 300)
        button.place(x = 600,y = 350)
        self.root.mainloop()
        
    def new_window(self):
        results = 20
        y_count = 80
        time = 0.06
        self.root = search.ctk.CTk()
        self.root.geometry('1400x766')
        self.root.title('search results')
        label = search.ctk.CTkLabel(self.root,text = 'about '+str(results)+' results '+'('+str(time)+' sec)',font = ('typescript',16))
        label.place(x=20,y=30)
        for i in search.os.listdir('files'):
            search.ctk.CTkButton(self.root,text = search.os.fsdecode(i),command = lambda t = search.os.fsdecode(i):self.open_in_browser(t),font = ('typescript',16),width = 500).place(x = 100,y = y_count)
            y_count += 60
        self.root.mainloop()
        
    def open_in_browser(self,filename):
        import webbrowser
        webbrowser.open('/home/abdullah/data/Programming Languages/Python/web scraping/files/'+filename)
        
search = search()





