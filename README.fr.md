# MelAdvisor

MelAdvisor est une appli crée par Carla Marcos Vázquez, une lycéenne de IES Vaguada de la Palma (Salamanque) pour son projet de fin d'études du BIE (Bacalauréat de Recherche et d'Excellence).

L' objectif de l'appli est de classser de images de lésions cutanées pigmentées en deux groupes: naevus ou mélanome, à l'aide d'un réseau neuronal convolutif également créé par Carla.
D'autres types de lésions pourront ëtre ajoutés à la classification à l'avenir.

L' appli sera disponible sous forme d'APK sur ce Github, et pourrait faire son chemin vers le Google Store à un moment donné, mais son utilisation sur iOS n'est pas prévue avant un avenir lointain.

## Comment fonctionne MelAvisor ?
MelAvisor utilise un réseau neuronal convolutif (CNN) pour classer les lésions pigmentées en deux classes (pour l'instant) : le nævus (bénin) et le mélanome (malin). Un CNN est un algorithme d'apprentissage profond utilisé en conjonction avec un perceptron multicouche. Il est spécialisé dans la reconnaissance et la classification d'images. L'algorithme attribue des poids aux différentes parties de l'image, puis les compare aux poids appris, ce qui lui permet de déterminer quel type de modèle d'image (images utilisées pour l'apprentissage) ressemble le plus à celui qui est donné, puis de le classer dans ce groupe.

À l'avenir, des fonctionnalités nouvelles et améliorées seront ajoutées à MelAdvisor. Je laisserai ici de brèves explications sur chacune d'entre elles au fur et à mesure. Néanmoins, si vous avez des doutes sur quoi que ce soit concernant MelAdvisor, n'hésitez pas à me contacter.

## Guide d' installation (appareils Android uniquement)
Pour l'instant, l'application est encore en phase de développement. Une fois que je l'aurai jugée suffisamment bonne pour être publiée, j'expliquerai brièvement dans cette section comment la télécharger et l'installer sur votre appareil.

## Utilisation
MelAdvisor est un moyen simple de vérifier l'absence de mélanome dans les lésions pigmentées. La détection précoce de ce type de lésions malignes est cruciale, car les chances de survie à ce cancer s'amenuisent au fur et à mesure qu'il se développe. La simplicité d'utilisation de cette application permet à tout utilisateur, quel que soit son niveau de connaissances sur le sujet, de savoir avec un bon degré de certitude ce que sont ses lésions.

Cette application n'est pas, et ne sera jamais, quel que soit son niveau de précision, un substitut à l'avis d'un spécialiste qualifié. Si vous avez de sérieux doutes sur une lésion, pensez à consulter un dermatologue dès que possible. 

Je vous en prie, ne risquez pas votre vie parce qu'il était plus facile de prendre une photo avec mon application que d'aller voir un médecin et d'obtenir un deuxième avis, mieux informé, sur le sujet.

## Feuille de route
### Changements très probables
+Ajout d'une base de données locale : Cela permettra aux utilisateurs de suivre l'évolution de leurs lésions en prenant plusieurs photos à des dates différentes. Un fichier sera créé pour chaque nouvelle lésion, et dans ce fichier, plusieurs images de cette lésion seront converties en une simple ligne de temps. L'utilisateur devra préciser à quelle lésion appartiennent les nouvelles images après les avoir prises, mais il y aura un système de filtrage pour qu'il soit plus facile de trouver la lésion souhaitée. De cette façon, ils pourront savoir si leurs lésions grandissent ou non, si leur forme change...

J'ai également l'intention de faire en sorte que le fichier de chaque lésion puisse être facilement envoyé par e-mail aux professionnels de la santé dans un PDF soigné présentant les images, l'heure à laquelle elles ont été prises, les mesures de la lésion...

J'essaierai de faire une base de données locale (stockée dans l'appareil sur lequel l'application est utilisée et non sur un serveur externe) pour trois raisons principales :

1. La protection de la vie privée. Je ne veux pas que MelAdvisor surveille ses utilisateurs, et encore moins quelque chose d'aussi sensible que leur santé. Bien sûr, afin d'améliorer l'algorithme, j'inclurai une option pour nous envoyer des images de diagnostic, afin que nous puissions les utiliser dans une nouvelle version du réseau et améliorer la performance et la fiabilité de l'application. Mais cette option sera TOUJOURS facultative.

2. Utilisation hors ligne. En ayant toutes les informations stockées sur votre propre appareil, vous n'aurez besoin d'aucune connexion pour y accéder. Je souhaite que MelAdvisor soit entièrement hors ligne si possible (à l'exception de la fonction qui vous permet de rechercher le résultat sur Google au cas où vous voudriez plus d'informations, mais c'est mineur). De cette façon, plus de gens auront accès à l'application sans avoir à se soucier de la qualité de leur internet.

3. Le coût. Je n'ai pas les ressources nécessaires pour faire tourner un serveur 24 heures sur 24 et 7 jours sur 7. Je sais qu'il existe des services qui vous louent un serveur pour un peu plus de 2 euros par mois, mais comme je l'ai dit, la vie privée est l'une de mes principales préoccupations, et laisser les données de mes utilisateurs entre les mains de tiers va à l'encontre de mes principes et de ceux de MelAdvisor.

Bien sûr, il y a aussi des inconvénients :

1. Les données occuperont de l'espace sur votre appareil, et pourraient en occuper beaucoup si vous prenez beaucoup de photos de haute qualité etc....

2. Pour que cela fonctionne, MelAdvisor doit accéder au stockage interne de l'appareil. Je sais, c'est un peu gênant pour les amoureux de la vie privée comme moi, mais c'est la meilleure solution que j'ai trouvée pour mettre en œuvre ces nouvelles fonctionnalités, que je considère comme cruciales. Si l'un d'entre vous a une meilleure solution en tête, n'hésitez pas à m'en faire part. Si cela peut vous consoler, je peux vous assurer que je n'ai aucun intérêt pécuniaire dans la création de cette application. Il s'agit simplement d'un projet scolaire auquel j'ai pris goût et que je souhaite poursuivre pendant mon temps libre.

De plus, si vous souhaitez à tout moment supprimer vos données, il vous suffit d'aller dans le stockage de votre appareil et de supprimer les fichiers. Je vais également ajouter des boutons pour simplifier le processus à partir de l'application elle-même.

+Ajout d'un "Wiki" : je vais créer une barre inférieure où vous pourrez accéder à de nouvelles fonctionnalités, la première d'entre elles étant le Wiki. J'y expliquerai brièvement et simplement ce que sont les lésions pigmentaires, quels types existent et lesquels MelAdvisor peut reconnaître, je donnerai des conseils sur la façon de traiter chaque type de lésion... D'autre part, à chaque nouvelle mise à jour après celle-ci, je créerai une petite section dans le Wiki expliquant les nouveautés et les changements, afin de vous tenir toujours informés.

### J'essaierai de le faire, mais je ne peux pas assurer sa réalisation

+Analyse en direct : L'application sera capable d'analyser et de classer les blessures sur vidéo, en direct. Elle sera capable de classer plusieurs lésions en même temps et de créer un nouveau fichier pour chaque lésion (ou d'ajouter les nouvelles images à un fichier existant) simplement en cliquant sur la pigmentation.

Il s'agira d'une tâche complexe, mais je suis convaincue que, si je dispose de suffisamment de temps et de connaissances, j'y parviendrai.

### Très improbable

+Lancement de l'application pour iOS : Malheureusement, je ne possède pas de Mac et honnêtement, je ne pense pas qu'il soit judicieux d'en acheter un juste pour programmer cette application sur iOS. J'essaierais bien d'emprunter l'appareil d'un membre de ma famille, mais je ne pense pas pouvoir maintenir l'application dans l'état que je souhaite (puisque je ne peux pas emprunter leur appareil à chaque fois que j'ai une nouvelle idée ou que je trouve un petit correctif pour quelque chose). Donc, pour l'instant, MelAdvisor sera exclusif à Androird (désolée, chers utilisateurs d'Apple).

Cependant, il existe peut-être un moyen d'installer des APK sur un iPhone. J'essaierai d'enquêter sur ce point et de trouver un autre moyen de vous faire parvenir l'application.
