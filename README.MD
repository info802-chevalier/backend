### Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/info802-chevalier/backend.git
   ```

2. Installez les dépendances :

   ```bash
   python install -r requirements.txt
   ```

3. Démarrez l'application :

   ```
   python app.py
   ```

4. L'application est disponible à l'adresse : [http://127.0.0.1:5000](http://127.0.0.1:5000)

### Variables d'environnement

Afin de configurer correctement l'application, vous devez définir plusieurs variables d'environnement pour accéder aux services externes. Ces variables doivent être définies dans votre environnement ou dans un fichier `.env` à la racine de votre projet. Voici les variables nécessaires à l'application :

#### OPEN ROUTE SERVICE

Ces clés d'API sont utilisées pour accéder aux services d'OpenRouteService, permettant de calculer des itinéraires et d'obtenir des informations géographiques.

- `OPEN_ROUTE_SERVICE_API_KEY_1` : **[Clé d'API pour le premier accès]**
- `OPEN_ROUTE_SERVICE_API_KEY_2` : **[Clé d'API pour un deuxième accès, si applicable]**
- `OPEN_ROUTE_SERVICE_API_URL` : URL de l'API (par défaut : `https://api.openrouteservice.org`)

#### CHARGE TRIP

Les clés et l'URL ci-dessous sont utilisées pour interagir avec l'API de ChargeTrip, permettant la gestion des bornes de recharge et des informations de trajet pour les véhicules électriques.

- `CHARGE_TRIP_API_URL` : URL de l'API (par défaut : `https://api.chargetrip.io/graphql`)
- `CHARGE_TRIP_X_CLIENT_ID_1` : **[ID client pour la première clé d'accès]**
- `CHARGE_TRIP_X_APP_ID_1` : **[ID d'application pour la première clé d'accès]**
- `CHARGE_TRIP_X_CLIENT_ID_2` : **[ID client pour la deuxième clé d'accès]**
- `CHARGE_TRIP_X_APP_ID_2` : **[ID d'application pour la deuxième clé d'accès]**

#### OPEN CHARGE MAP

Cette API permet d'accéder à des informations sur les bornes de recharge pour véhicules électriques via OpenChargeMap.

- `OPEN_CHARGE_MAP_API_URL` : URL de l'API (par défaut : `https://api.openchargemap.io/v3/poi`)
- `OPEN_CHARGE_MAP_API_KEY` : **[Clé d'API pour accéder à OpenChargeMap]**

### Exemple de fichier `.env`

Voici un exemple de fichier `.env` pour vous aider à définir les variables d'environnement :

```bash
## ---- OPENN ROUTE SERVICE ----
OPEN_ROUTE_SERVICE_API_KEY_1=your_key_1_here
OPEN_ROUTE_SERVICE_API_KEY_2=your_key_2_here
OPEN_ROUTE_SERVICE_API_URL=https://api.openrouteservice.org

## ---- CHARGE TRIP ----
CHARGE_TRIP_API_URL=https://api.chargetrip.io/graphql
## -
CHARGE_TRIP_X_CLIENT_ID_1=your_client_id_1_here
CHARGE_TRIP_X_APP_ID_1=your_app_id_1_here
## -
CHARGE_TRIP_X_CLIENT_ID_2=your_client_id_2_here
CHARGE_TRIP_X_APP_ID_2=your_app_id_2_here

## ---- OPEN CHARGE MAP ----
OPEN_CHARGE_MAP_API_URL=https://api.openchargemap.io/v3/poi
OPEN_CHARGE_MAP_API_KEY=your_api_key_here
```

### Deployment

Le projet est déployé avec [https://vercel.com/](Vercel)

- **URL** : [https://backend-tau-plum.vercel.app/](https://backend-tau-plum.vercel.app/)
- **Documentation** : [https://backend-tau-plum.vercel.app/api](https://backend-tau-plum.vercel.app/api)

### API

Cette API est construite avec **Flask** et **Flask-RESTful**, permettant de créer facilement des services web RESTful. Les points d'entrée sont définis dans un format JSON et peuvent être utilisés pour récupérer, ajouter, modifier ou supprimer des ressources.

### Features

- **Flask-RESTful** : Fournit des classes pour organiser les ressources, avec des méthodes HTTP comme `GET`, `POST`, `PUT`, `DELETE`, etc.
- **Flask-RESTful-Swagger** : Utilisé pour générer automatiquement la documentation de l'API au format Swagger, ce qui permet aux utilisateurs de consulter facilement les points d'entrée de l'API et de tester les différentes fonctionnalités directement depuis la documentation.
- **Gestion des erreurs** : Les erreurs sont capturées et renvoyées dans un format JSON avec un code d'état HTTP approprié.

### Swagger Documentation

La documentation interactive est générée à l'aide de **Flask-RESTful-Swagger**. Vous pouvez explorer et tester l'API directement depuis la page de documentation.

```

```
