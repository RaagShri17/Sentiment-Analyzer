import tkinter as tk
from logic import get_mood

window = tk.Tk()
window.title("Sentiment Analyzer")
window.geometry("450x380")

# title
tk.Label(window, text="Sentiment Analyzer", font=("Arial", 14)).pack(pady=15)

tk.Label(window, text="Enter text:").pack()

# textbox for input
textbox = tk.Text(window, width=40, height=8)
textbox.pack(pady=8)

# show emoji here
emoji_result = tk.Label(window, text="", font=("Arial", 40))
emoji_result.pack(pady=15)

# show positive/negative text
text_result = tk.Label(window, text="")
text_result.pack()

def analyze():
    txt = textbox.get("1.0", "end").strip()
    
    if txt == "":
        emoji_result.config(text="⚠️")
        text_result.config(text="write something first")
        return
    
    # get mood from logic file
    m = get_mood(txt, threshold=0.3)
    emoji_result.config(text=m.emoji)
    
    # check if positive or negative
    if m.sentiment > 0.3:
        text_result.config(text="positive", fg="green")
    elif m.sentiment < -0.3:
        text_result.config(text="negative", fg="red")
    else:
        text_result.config(text="neutral", fg="gray")

# button to run analysis
btn = tk.Button(window, text="Analyze", command=analyze)
btn.pack(pady=12)

window.mainloop()