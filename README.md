#  Sentiment Analysis Tool

A simple yet powerful Python application that analyzes the sentiment of text using Natural Language Processing (NLP) and displays results through an intuitive graphical user interface.

##  Overview

This project uses TextBlob to perform sentiment analysis on user-provided text and categorizes it as Positive, Negative, or Neutral. The application features a clean GUI built with Tkinter that makes sentiment analysis accessible to everyone.
Logic of the Program
<img width="715" height="540" alt="image" src="https://github.com/user-attachments/assets/6758d964-83b2-43a5-bdc5-3047c65e1e9c" />


##  Features

- **Real-time Sentiment Analysis**: Instantly analyze any text input
- **Visual Feedback**: Emoji-based sentiment representation 
- **Adjustable Sensitivity**: Customize threshold levels (0.1 - 0.9) for sentiment classification
- **Sentiment Score**: Displays precise polarity score (-1.0 to +1.0)
- **Color-Coded Results**: 
  - 🟢 Green text for Positive sentiment
  - 🔴 Red text for Negative sentiment
  - ⚫ Gray text for Neutral sentiment
- **User-Friendly Interface**: Clean, simple and basic GUI with scrollable text input
- **Keyboard Shortcut**: Press `Ctrl + Enter` for quick analysis

##  Technologies Used

- **Python 3.x**
- **TextBlob**: For sentiment analysis and NLP processing
- **Tkinter**: For GUI development
- **Dataclasses**: For structured data management

##  Installation

### Prerequisites

Make sure you have Python 3.7 or higher installed on your system.

### Step 1: Clone or Download the Repository

```bash
git clone https://github.com/yourusername/sentiment-analysis-tool.git
cd sentiment-analysis-tool
```

### Step 2: Install Required Dependencies

```bash
pip install textblob
```

### Step 3: Download TextBlob Corpora (First-time setup)

```bash
python -m textblob.download_corpora
```

##  Usage

### Running the Application

Navigate to the project directory and run:

```bash
python sentiment_gui.py
```

### How to Use

1. **Enter Text**: Type or paste your text into the input box
2. **Adjust Threshold** (Optional): Use the slider to set sensitivity
   - Lower threshold (0.1-0.3): More sensitive, broader categorization
   - Higher threshold (0.4-0.9): Less sensitive, stricter categorization
3. **Analyze**: Click "Analyze Sentiment" button or press `Ctrl + Enter`
4. **View Results**: See the emoji, category, and numerical score

### Example Inputs

**Positive Sentiment:**
```
"I absolutely love this product! It exceeded all my expectations."
```
<img width="558" height="557" alt="image" src="https://github.com/user-attachments/assets/6600fcf5-4776-486d-a462-7d0f7018507c" />

**Negative Sentiment:**
```
"This is terrible. I'm very disappointed with the quality."
```
<img width="555" height="556" alt="image" src="https://github.com/user-attachments/assets/757401dc-5064-4877-a09b-ecb401d36112" />


**Neutral Sentiment:**
```
"The package arrived on Tuesday. It contains three items."
```
<img width="561" height="559" alt="image" src="https://github.com/user-attachments/assets/3f61b3bc-a849-430d-ba91-5517bb97baf9" />


## 📊 Understanding Sentiment Scores

- **Score Range**: -1.0 (most negative) to +1.0 (most positive)
- **Positive**: Score ≥ threshold
- **Neutral**: Score between -threshold and threshold
- **Negative**: Score ≤ -threshold

Default threshold is set to 0.3, which balances sensitivity and accuracy.

##  Project Structure

```
sentiment-analysis-tool/
│
├── sentiment_gui.py          # Main application file with GUI
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies (optional)
```


##  Use Cases

- **Social Media Monitoring**: Analyze customer feedback and comments
- **Product Reviews**: Understand customer satisfaction levels
- **Email Classification**: Filter and prioritize messages
- **Content Moderation**: Detect potentially harmful or negative content
- **Market Research**: Analyze survey responses and feedback
- **Customer Support**: Prioritize urgent or dissatisfied customer messages

##  Customization

### Changing Default Threshold

In `gui.py`, modify line:
```python
self.threshold_var = tk.DoubleVar(value=0.3)  # Change 0.3 to your preferred value
```

### Modifying Emojis

In the `get_mood()` function:
```python
if sentiment >= friendly_threshold:
    return Mood("😊", sentiment)  # Change to any emoji you prefer
```

### Adjusting Window Size

```python
self.root.geometry("600x500")  # Modify width x height
```

##  Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'textblob'"
**Solution**: Install TextBlob
```bash
pip install textblob
```

### Issue: "LookupError: Resource punkt not found"
**Solution**: Download NLTK data
```bash
python -m textblob.download_corpora
```

### Issue: GUI doesn't appear or crashes
**Solution**: Ensure Tkinter is installed (usually comes with Python)
- On Ubuntu/Debian: `sudo apt-get install python3-tk`
- On macOS: Tkinter should be pre-installed
- On Windows: Reinstall Python with Tkinter option checked


## Future Enhancements

- [ ] Add support for multiple languages
- [ ] Save analysis history to CSV/JSON
- [ ] Batch processing for multiple texts
- [ ] Integration with social media APIs
- [ ] Export results as reports
- [ ] Advanced visualization with graphs
- [ ] Machine learning model training option

---

**Made By**
Raag Shri 
25BAI 10431
