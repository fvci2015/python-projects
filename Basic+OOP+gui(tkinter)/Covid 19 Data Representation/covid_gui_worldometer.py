import tkinter as tk
import requests
from bs4 import BeautifulSoup

class CovidDataScraper:
    def __init__(self):
        self.url = "https://www.worldometers.info/coronavirus/"

    def fetch_data(self):
        # Send a GET request to the URL
        response = requests.get(self.url)
        
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find the table containing the COVID-19 statistics
            table = soup.find('table', id='main_table_countries_today')
            
            if table:
                # Extract table headers (column names)
                headers = [header.text.strip() for header in table.find_all('th')]
                
                # Extract table rows (country data)
                rows = []
                for row in table.find_all('tr')[1:]:
                    rows.append([data.text.strip() for data in row.find_all('td')])
                
                return headers, rows
            else:
                print("Table not found on the webpage.")
                return None
        else:
            print(f"Failed to fetch data from URL: {self.url}")
            return None

class CovidGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("COVID-19 Statistics")
        
        self.data_scraper = CovidDataScraper()
        
        self.label = tk.Label(root, text="COVID-19 Statistics", font=("Helvetica", 16))
        self.label.pack(pady=10)
        
        self.stats_text = tk.Text(root, height=20, width=100)
        self.stats_text.pack()
        
        self.update_stats()
    
    def update_stats(self):
        headers, rows = self.data_scraper.fetch_data()
        
        if headers and rows:
            # Create a formatted string for displaying in the text widget
            stats_str = ""
            for row in rows[:10]:  # Displaying the first 10 rows
                stats_str += "\t".join(row) + "\n"
            
            self.stats_text.delete("1.0", tk.END)  # Clear previous content
            self.stats_text.insert(tk.END, "\t".join(headers) + "\n")
            self.stats_text.insert(tk.END, stats_str)
        else:
            self.stats_text.delete("1.0", tk.END)
            self.stats_text.insert(tk.END, "Failed to fetch or parse data.")
        
        # Schedule the update_stats method to run again after 10 minutes (600000 milliseconds)
        self.root.after(600000, self.update_stats)

if __name__ == "__main__":
    root = tk.Tk()
    app = CovidGUI(root)
    root.mainloop()
