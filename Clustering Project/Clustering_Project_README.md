
# Clustering Project 🧩

![Clustering Project](https://img.shields.io/badge/AI--ML%20Project-Clustering-green)  
_Clustering FIFA 23 Players Based on Performance, Physical Attributes & Financial Metrics_

Welcome to the **Clustering Project**! This project applies powerful clustering algorithms to group FIFA 23 players based on various features, such as skill levels, physical attributes, and financial information. The goal is to uncover hidden patterns and provide insights for player analysis and scouting.

---

## 🚀 Project Highlights

- **Algorithms Used**: KMeans, DBSCAN, and Hierarchical Clustering 🧠
- **Data Visualization**: Beautiful plots to visualize clusters 🎨
- **Key Metrics**: Performance, Physical Strength, Financial Values 💸
- **Interactive Exploration**: Analyze and adjust clustering parameters easily 🔧

---

## 📝 Dataset

This project uses the **FIFA 23 dataset** featuring detailed player statistics, including:

- **Performance Metrics**: `Overall`, `Potential`, `Pace Total`, `Shooting Total`, `Passing Total`, etc. 📊
- **Physical Attributes**: `Height`, `Weight`, `Strength`, `Stamina` 💪
- **Financial Metrics**: `Value (in Euro)`, `Wage (in Euro)` 💼

---

## 🛠️ Installation

### Clone the Repo

```bash
git clone https://github.com/adesh-pawar10/AI-ML-Projects.git
cd AI-ML-Projects/Clustering%20Project
```

### Set Up Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### Step 1: Run the Jupyter Notebook

```bash
jupyter notebook FIFA_Player_Clustering_Analysis.ipynb
```

### Step 2: Explore & Visualize

- Adjust the clustering parameters like number of clusters (KMeans), distance thresholds (DBSCAN), and visualize how players are grouped.
- Analyze the interactive plots showing clusters of players based on performance and physical attributes.

### Step 3: Interpret the Results

- Use the **Silhouette Score** to evaluate clustering quality 📈
- Examine how the clustering results differ across algorithms.

---

## 📊 Project Structure

```bash
Clustering Project/
├── data/                  # Raw and processed data files
├── notebooks/             # Jupyter Notebooks for analysis
├── src/                   # Code for data preprocessing & clustering
├── visuals/               # Cluster plots and visualizations
└── README.md              # Project documentation
```

---

## 📌 Results

The results show clear clusters based on players’ skillsets, financial value, and physical strength. Below are some insights:
- **Cluster 1**: High-performing players with high financial value 💰
- **Cluster 2**: Mid-level players with moderate potential 🔄
- **Cluster 3**: Young players with high potential but lower current performance 🚀

---

## 🤝 Contributing

Contributions are always welcome! Follow these steps to contribute:

1. **Fork the repository** 🔁
2. **Create a new branch**:  
   `git checkout -b feature/YourFeature`
3. **Make your changes** 🔧
4. **Commit your changes**:  
   `git commit -m 'Add new feature'`
5. **Push your branch**:  
   `git push origin feature/YourFeature`
6. **Open a Pull Request** 🌟

---

## 🔗 Useful Links

- [FIFA 23 Player Dataset](https://www.kaggle.com/datasets/poojap94/fifa-23-player-dataset)  
- [KMeans Algorithm Explanation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)  
- [DBSCAN Clustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html)  

---

## 🚀 Badges

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
