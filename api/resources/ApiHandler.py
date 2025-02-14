import requests

default_type = 'application/json'

class ApiHandler:
    ## Constructors
    def __init__(self):
        """
        Constructeur par défaut qui initialise les paramètres de connexion de l'API
        - url : URL de l'API
        - token : Token d'authentification
        - headers : En-t tes de r qu te
        """
        
        self.api_url = "http://localhost:5000"
        self.api_token = "token"
        self.api_headers = {
            'Content-Type': default_type,
            'Authorization': f'Bearer {self.api_token}',
            'Accept': default_type,
            'Access-Control-Allow-Origin': '*'
        }

    def __init__(self, url, token, headers):
        """
        Constructeur qui initialise les parametres de connexion de l'API
        - url : URL de l'API
        - token : Token d'authentification
        - headers : En-t tes de r qu te
        """
        self.api_url = url
        self.api_token = token
        self.api_headers = headers

    ## Setters
    def set_url(self, url):
        """
        Change l'URL de l'API.
        
        :param url: URL de l'API
        """
        self.api_url = url

    def set_token(self, token):
        """
        Change le token d'authentification.
        
        :param token: Token d'authentification
        """
        self.api_token = token

    def set_headers(self, headers):
        """
        Change les en-têtes de la requete.
        
        :param headers: En-tetes de la requete
        """
        self.api_headers = headers

    ## Methods
    def get(self, url):
        """
        Effectue une requete GET sur l'API.
        
        :param url: URL relative de la ressource souhaitee
        :return: Reponse de l'API
        """
        response = requests.get(self.api_url + url, headers=self.api_headers)
        return response
    
    def post(self, url, data):
        """
        Effectue une requête POST sur l'API.

        :param url: URL relative de la ressource souhaitée
        :param data: Données JSON à envoyer dans le corps de la requête
        :return: Réponse de l'API
        """
        response = requests.post(self.api_url + url, headers=self.api_headers, json=data)
        return response
    
    def put(self, url, data):
        """
        Effectue une requête PUT sur l'API.

        :param url: URL relative de la ressource souhaitée
        :param data: Données JSON à envoyer dans le corps de la requête
        :return: Réponse de l'API
        """
        response = requests.put(self.api_url + url, headers=self.api_headers, json=data)
        return response
    
    def delete(self, url):
        """
        Effectue une requête DELETE sur l'API.
        
        :param url: URL relative de la ressource souhaitée
        :return: Réponse de l'API
        """
        response = requests.delete(self.api_url + url, headers=self.api_headers)
        return response