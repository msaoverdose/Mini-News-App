import tkinter as tk
import feedparser
import webbrowser #We've used to webbrowser library for open links but you can use too pywebview for open links to same interface

class NewsInterface:
    def __init__(self, master):
        self.master = master
        master.title("News App By DMSA") #You can change this title to your own title
        self.news_listbox = tk.Listbox(master, width=60) #You can use different resolutions for better interface 
        self.news_listbox.grid(row=0, column=0, padx=10, pady=10)
        self.news_listbox.bind("<Double-Button-1>", self.open_article) 
        self.feed = feedparser.parse("http://feeds.bbci.co.uk/news/world/rss.xml#") #We've used bbci for source but you can take advantage to different sources
        self.update_news()
        
        refresh_button = tk.Button(master, text="Refresh", command=self.update_news)
        refresh_button.grid(row=1, column=0, padx=10, pady=10, sticky="n")
    
    def update_news(self):
        
        self.news_listbox.delete(0, tk.END)
        
        for entry in self.feed.entries:
            self.news_listbox.insert(tk.END, entry.title)
            self.news_listbox.itemconfig(tk.END, foreground="white")
            
    def open_article(self, event):
        selection = self.news_listbox.curselection()
        if selection:
            index = selection[0]
            article_url = self.feed.entries[index].link
            
            webbrowser.open(article_url)
    
root = tk.Tk()
news_interface = NewsInterface(root)
root.mainloop()
