# DataLake

Le fichier ChargementFichierCSV.ipynb, permet de charger tous les fichiers qui se trouvent dans l'url : https://www.ncei.noaa.gov/data/global-hourly/access/ 
Nous on a choisit de charger uniquemlent des données de certaines stations pour les années de 2020 et de 2021.
Y'a deux requêtes qui permettent de charger ces fichiers : 
      * Une requête en utilisant BeautifulSoup classique
      * Une requête en utilisant BeautifulSoup et un Thread
      
Toutes ces données de ces fichiers on les importera dans Hadoop (HDFS) en utilisaznt les commandes suivantes :
      * On les stockera dans le docker : docker cp sourceLocal namenode:destDocker
      * On ouvre le terminal du nameNode Hadoop, et on chargera ces données avec HDFS : hdfs dfs -put sourceDocker destHadoop
      * Ouis on ouvre un noteBook PySpark dans le même cluster, et on fera tout le traitement de données (fichier : Projet_DataLake_NOAA.ipynb)
      * On stockera le résultat dans un base données PostGreSQL 
      
