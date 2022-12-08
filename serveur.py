
"""
    USER : @asanthakumaran 
    DATE : 19/10/2022
    LANGUAGE : PYTHON 3.9


    *** PYTHON SERVER ***

    CONSIGNE:
        * Fichier Python permettant de Lancer un serveur Localhost
        * Ici le port sera défini par défault sur : 8888
        * On ne peut pas executer deux tâches différente sur un même port

    IMPORTATION DE MODULE:

        * MODULE WEBBROWSER: 
            -> Module servant à afficher des pages web, dans le navigateur de son choix.
        * MODULE HTTP.SERVER:
            -> qui permet de gérer les requêtes HTTP
        * MODULE OS:
            ->

        + Pour voir des éventuels erreurs utiliser :
            -> import cgitb; cgitb.enable()

        + Pour pousser sur notre serveur python on peut utiliser :
            * import socketserver :
                -> qui permet de créer un serveur TCP // On utilisera pas ici dans ce cas. Nous voulons juste afficher notre template sur un serveur

            Exemple d'utilisation :
                -> with socketserver.TCPServer(("", PORT), Handler) as tcp_server:
"""


import webbrowser
import http.server
import os

PORT = 8888
server_address = ("", PORT)
URL = f"http://localhost:{PORT}/index.py"

os.chdir(os.path.dirname(__file__))

server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]
print("Serveur actif sur le port :", PORT)

httpd = server(server_address, handler)
webbrowser.open_new(URL)
httpd.serve_forever()


"""
Autre Possibilité de crée son propre serveur python :

    * UTILISATION DE MODULE :
        * BaseHTTPServer : 
        * CGIHTTPServer  :
    *

    * PROGRAMME PYTHON : 
        #!/usr/bin/python
        user : @akirasanthakumaran
        
        import BaseHTTPServer
        import CGIHTTPServer
        
        PORT = 8888
        server_address = ("", PORT)

        server = BaseHTTPServer.HTTPServer
        handler = CGIHTTPServer.CGIHTTPRequestHandler
        handler.cgi_directories = ["/"]
        print "Serveur actif sur le port :", PORT

        httpd = server(server_address, handler)
        httpd.serve_forever()
    *

UNE TROISIEME POSSIBILITE DE CREE SON SERVEUR :

    * UTILISATION DE MODULE:
        * http.serveur : 

    *

    * PROGRAMME PYTHON : 
        import http.server
        
        PORT = 8888
        server_address = ("", PORT)

        server = http.server.HTTPServer
        handler = http.server.CGIHTTPRequestHandler
        handler.cgi_directories = ["/"]
        print("Serveur actif sur le port :", PORT)

        httpd = server(server_address, handler)
        httpd.serve_forever()
    *

"""
