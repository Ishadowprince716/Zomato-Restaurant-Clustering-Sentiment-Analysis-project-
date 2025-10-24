
# Create comprehensive project documentation file
project_structure_md = '''# Zomato ML Clustering - Complete Project Structure

## 📁 Repository Structure

```
zomato-ml-clustering/
│
├── 📄 README.md                    # Main project documentation
├── 📄 LICENSE                      # MIT License
├── 📄 CONTRIBUTING.md              # Contribution guidelines
├── 📄 .gitignore                   # Git ignore rules
├── 📄 requirements.txt             # Python dependencies
├── 📄 setup.py                     # Package installation
├── 📄 Dockerfile                   # Docker configuration
├── 📄 .dockerignore                # Docker ignore rules
├── 📄 .env.example                 # Environment variables template
│
├── 📂 src/                         # Source code modules
│   ├── data_processing.py          # Data cleaning and preprocessing
│   ├── clustering.py               # Clustering algorithms
│   ├── sentiment_analysis.py       # Sentiment analysis
│   └── visualization.py            # Plotting utilities (optional)
│
├── 📂 notebooks/                   # Jupyter notebooks
│   ├── 01_EDA.ipynb               # Exploratory Data Analysis
│   ├── 02_preprocessing.ipynb      # Data preprocessing
│   ├── 03_clustering.ipynb         # Clustering analysis
│   ├── 04_sentiment.ipynb          # Sentiment analysis
│   └── 05_insights.ipynb           # Business insights
│
├── 📂 data/                        # Data directory
│   ├── 📂 raw/                     # Raw datasets
│   │   ├── .gitkeep
│   │   └── README.md               # Data description
│   ├── 📂 processed/               # Processed datasets
│   │   └── .gitkeep
│   └── 📂 sample/                  # Sample data for testing
│       └── sample_restaurants.csv
│
├── 📂 results/                     # Analysis results
│   ├── .gitkeep
│   ├── 📂 figures/                 # Generated plots
│   ├── 📂 models/                  # Saved models
│   └── 📂 reports/                 # Analysis reports
│
├── 📂 tests/                       # Unit tests (optional)
│   ├── __init__.py
│   ├── test_data_processing.py
│   ├── test_clustering.py
│   └── test_sentiment.py
│
├── 📂 streamlit_app/               # Streamlit application (alternative structure)
│   └── streamlit_app.py            # Main Streamlit app
│
└── 📂 docs/                        # Additional documentation
    ├── installation.md
    ├── usage_guide.md
    ├── api_reference.md
    └── deployment.md
```

## 🚀 Quick Start Guide

### 1. Clone the Repository

```bash
git clone https://github.com/Ishadowprince716/zomato-ml-clustering.git
cd zomato-ml-clustering
```

### 2. Set Up Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\\Scripts\\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Download NLTK Data (Required for Sentiment Analysis)

```python
import nltk
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
```

### 4. Set Up Environment Variables

```bash
# Copy example env file
cp .env.example .env

# Edit .env and add your API keys
# GOOGLE_API_KEY=your_gemini_api_key_here
```

### 5. Run the Application

```bash
# Run Streamlit app
streamlit run streamlit_app.py

# Or run with Docker
docker build -t zomato-ml-app .
docker run -p 8501:8501 zomato-ml-app
```

## 📊 Data Preparation

### Expected Data Format

**Restaurant Data (`restaurants.csv`):**
```csv
name,location,cost,cuisines,rating,timings
Restaurant A,Delhi,800,"North Indian, Mughlai",4.5,11:00-23:00
Restaurant B,Mumbai,500,"Chinese, Thai",4.2,12:00-22:00
```

**Review Data (`reviews.csv`):**
```csv
restaurant_id,reviewer,review,rating,time,pictures
1,John Doe,Amazing food and service!,5,2024-01-15,2
2,Jane Smith,Average experience,3,2024-01-16,0
```

### Sample Data

A sample dataset is available in `data/sample/` for testing purposes.

## 🔧 Module Usage

### Data Processing

```python
from src.data_processing import DataProcessor

# Initialize processor
processor = DataProcessor()

# Load data
df = processor.load_data('data/raw/restaurants.csv')

# Clean data
df = processor.handle_missing_values(df, strategy='mean')
df = processor.remove_duplicates(df)
df = processor.handle_outliers(df, columns=['cost', 'rating'])

# Encode and scale
df = processor.encode_categorical(df, columns=['cuisines'], method='label')
df = processor.scale_features(df, columns=['cost', 'rating'], method='standard')
```

### Clustering

```python
from src.clustering import RestaurantClustering

# Initialize clustering
clusterer = RestaurantClustering()

# Find optimal clusters
results = clusterer.find_optimal_clusters(X, max_clusters=10)
clusterer.plot_elbow_curve(results)

# Perform K-Means clustering
labels = clusterer.kmeans_clustering(X, n_clusters=4)

# Visualize clusters
clusterer.visualize_clusters_2d(X, df)

# Get cluster characteristics
cluster_stats = clusterer.get_cluster_characteristics(df, ['cost', 'rating'])
```

### Sentiment Analysis

```python
from src.sentiment_analysis import SentimentAnalyzer

# Initialize analyzer
analyzer = SentimentAnalyzer()

# Analyze reviews
results = analyzer.analyze_reviews_batch(reviews, method='vader')

# Get sentiment distribution
distribution, pct = analyzer.get_sentiment_distribution(results['sentiment'])

# Extract keywords
positive_keywords = analyzer.extract_keywords(positive_reviews, top_n=20)

# Plot sentiment
analyzer.plot_sentiment_distribution(results['sentiment'])
```

## 🐳 Docker Deployment

### Build Image

```bash
docker build -t zomato-ml-app:latest .
```

### Run Container

```bash
docker run -d -p 8501:8501 --name zomato-app zomato-ml-app:latest
```

### Docker Compose (Optional)

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8501:8501"
    volumes:
      - ./data:/app/data
      - ./results:/app/results
    environment:
      - GOOGLE_API_KEY=${GOOGLE_API_KEY}
```

Run with:
```bash
docker-compose up -d
```

## 🌐 Deployment Options

### Streamlit Cloud

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Select `streamlit_app.py` as the main file
5. Add secrets in Streamlit Cloud dashboard
6. Deploy!

### Heroku

```bash
# Install Heroku CLI
# Create Procfile
echo "web: streamlit run streamlit_app.py --server.port=$PORT" > Procfile

# Create runtime.txt
echo "python-3.9.16" > runtime.txt

# Deploy
heroku create zomato-ml-app
git push heroku main
```

### AWS EC2

1. Launch EC2 instance (Ubuntu)
2. Install Docker
3. Clone repository
4. Build and run Docker container
5. Configure security groups (port 8501)
6. Access via public IP

## 📝 Development Workflow

### Adding New Features

1. Create feature branch
   ```bash
   git checkout -b feature/new-feature
   ```

2. Make changes and test

3. Commit changes
   ```bash
   git add .
   git commit -m "Add: new feature description"
   ```

4. Push and create PR
   ```bash
   git push origin feature/new-feature
   ```

### Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest --cov=src tests/

# Run specific test
pytest tests/test_clustering.py
```

## 🎓 Jupyter Notebooks Guide

Navigate to notebooks and run in order:

1. **01_EDA.ipynb**: Initial data exploration
2. **02_preprocessing.ipynb**: Data cleaning and feature engineering
3. **03_clustering.ipynb**: Clustering analysis
4. **04_sentiment.ipynb**: Sentiment analysis
5. **05_insights.ipynb**: Business insights generation

## 📚 Additional Resources

### Documentation
- [Installation Guide](docs/installation.md)
- [Usage Guide](docs/usage_guide.md)
- [API Reference](docs/api_reference.md)
- [Deployment Guide](docs/deployment.md)

### External Resources
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [NLTK Documentation](https://www.nltk.org/)
- [Pandas Documentation](https://pandas.pydata.org/)

## 🤝 Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Rahul Singh Kushwah** - *Initial work* - [GitHub](https://github.com/Ishadowprince716)

## 🙏 Acknowledgments

- Zomato for inspiration
- Microsoft Azure for ML resources
- Open-source community
- GeeksforGeeks community

---

For questions or support, please open an issue or contact the maintainer.
'''

with open('PROJECT_STRUCTURE.md', 'w', encoding='utf-8') as f:
    f.write(project_structure_md)

print("✅ PROJECT_STRUCTURE.md created successfully!")
