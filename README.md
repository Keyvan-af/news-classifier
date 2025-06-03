# News Classification System

A machine learning-powered web application that classifies Persian news articles from Tasnim News Agency into "Political" or "Sport" categories, with a Flask backend API and Blazor frontend.

## Features

- 🚀 Fast text classification using pre-trained machine learning model
- 🌐 Flask REST API backend with model serving
- 💻 Modern Blazor frontend with responsive design
- 📊 Trained on real Tasnim News Agency data
- 🔍 Simple and intuitive user interface

## Technology Stack

**Backend:**
- Python 3.8+
- Flask
- Scikit-learn
- NLTK/Persian NLP tools
- Joblib (for model serialization)

**Frontend:**
- ASP.NET Core Blazor
- C#
- HTML5/CSS3
- Bootstrap 5

## Setup Instructions

### Backend Setup

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Create and activate virtual environment (recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask API**:
   ```bash
   python app.py
   ```
   The API will run at `http://localhost:5000`

### Frontend Setup

1. **Prerequisites**:
   - Visual Studio 2022 (with ASP.NET and web development workload)
   - .NET 6.0 SDK or later

2. **Open the solution**:
   - Navigate to the frontend directory:
     ```bash
     cd frontend/NewsClassifier
     ```
   - Open `Blazer.sln` file with Visual Studio

3. **Install Blazor (if not already installed)**:
   - Through Visual Studio Installer → ASP.NET and web development workload
   - Or via .NET CLI:
     ```bash
     dotnet workload install wasm-tools
     ```

4. **Run the application**:
   - Press F5 in Visual Studio
   - The application will launch at `http://localhost:5001`

## Usage

1. Access the web application in your browser
2. Paste or type Persian news text in the text area
3. Click "Classify News" button
4. View the prediction result (Political or Sport)


## Future Improvements

### 1. Add More News Categories
- Include economy, technology, and entertainment news
- Collect more data for each category

### 2. Improve the Model
- Try different machine learning models
- Test Persian-specific language models
- Add better text cleaning for Persian

### 3. Enhance the Website
- Show prediction confidence percentage
- Add examples for each category
- Save previous classifications

### 4. Get More Data
- Crawl news from other Iranian websites
- Add older news articles
- Balance number of articles per category

### 5. Make It Faster
- Cache frequent predictions
- Optimize model loading
- Add quick classification for headlines