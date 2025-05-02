import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.cluster import KMeans

def plot_dados(dados):
    classes_unicas = dados["Classe"].unique()
    palette = sns.color_palette("bright", len(classes_unicas))
    cores = dict(zip(classes_unicas, palette))

    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=dados, x="X1", y="X2", hue="Classe", palette=cores, s=40)
    plt.title("Visualização por Classe")
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.legend().remove()
    plt.tight_layout()
    plt.show()

def kmeans(dados, k, seed, n_init):
    kmeans = KMeans(n_clusters=k, n_init=n_init, random_state=seed)
    dados["Cluster"] = kmeans.fit_predict(dados[["X1", "X2"]])
    dados["Cluster"] = dados["Cluster"].astype(str)

    clusters_unicos = dados["Cluster"].unique()
    palette = sns.color_palette("bright", len(clusters_unicos))
    cores_cluster = dict(zip(clusters_unicos, palette))

    silhouette(dados)

    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=dados, x="X1", y="X2", hue="Cluster", palette=cores_cluster, s=40)
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
                c='dimgray', s=80, edgecolors='black', marker='o', label='Centroides')
    plt.title(f"K-means com {k} clusters")
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.legend().remove()
    plt.tight_layout()
    plt.show()

def silhouette(dados):
    coordenadas = dados[['X1', 'X2']].values
    rotulos_clusters = dados['Cluster'].astype(int).values

    # Cálculo dos valores individuais
    valores_sil = silhouette_samples(coordenadas, rotulos_clusters)

    # Cria DataFrame
    tabela_silhouette = pd.DataFrame({
        'cluster': rotulos_clusters,
        'silhouette': valores_sil
    })

    media_geral = silhouette_score(coordenadas, rotulos_clusters)
    print(f"\nMédia geral do coeficiente de silhouette: {media_geral:.4f}")

    media_por_cluster = tabela_silhouette.groupby('cluster')['silhouette'].mean()
    print("\nMédia por cluster:")
    print(media_por_cluster.round(4).to_string())

def prepara_dados(dados):
    dados.columns = ["X1", "X2", "Classe"]
    dados["Classe"] = dados["Classe"].astype(str)

    return dados

dados = pd.read_csv("dados.csv", header=None)
dados = prepara_dados(dados)

dados2 = pd.read_csv("dados2.csv", header=None)
dados2 = prepara_dados(dados2)

# plot_dados(dados)
kmeans(dados, 15, 12345, 100)
kmeans(dados2, 31, 12345, 100)
