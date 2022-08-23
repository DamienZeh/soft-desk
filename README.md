![Alt text](https://github.com/DamienZeh/soft-desk/blob/main/soft_desk/soft_desk/logo/logo.png)<br>

# API Soft-Desk

Cette API permet de remonter et de suivre des problèmes techniques.<br> Les utilisateurs, une fois connectés, peuvent:<br>
- Créer des projets
- Y ajouter des contributeurs
- Y créer des problèmes liés à ces projets(auteur et contributeurs)
- Et créer des commentaires en réponse à ces problèmes(auteur et contributeurs).<br>

Elle fonctionne sur un serveur local.<br><br>



## Téléchargement et installation 


- Avec votre terminal, allez dans le dossier ou vous souhaitez placer le projet.<br/> 
Exemple : ``cd C:\Users\damie\Documents\Python_Project``
- Copiez le projet : ``git clone https://github.com/DamienZeh/soft-desk.git``
- Puis, allez dans ce projet : ``cd soft-desk\``
- puis créez l’environnement virtuel avec  ``python -m venv env``<br/>
	_(‘env’ est le nom que j’ai sur mon environnement virtuel, il est aussi noté dans le gitignore.)_
- Puis activez le : ``.\env\Scripts\activate`` (pour windows)<br/>
ou ``source env\bin\activate`` (pour linux)<br/>
	_(Vous avez maintenant un ‘(env)’ d’affiché, l'environnement est activé)_<br>
cette commande devra être lancée à chaque redémarrage du terminal.
- Puis, l’installation  des packages présents dans le requirements.txt:<br> ``pip install -r requirements.txt``
<br/><br>




## Endpoints de l'API et documentation
Tous les points de terminaison de l'API et leurs modes d'emploi sont disponibles
 sur la [**documentation**](https://documenter.getpostman.com/view/19809103/VUqrNcdD),<br/> réalisée sur Postman .
 Ces 19 liens ont des exemples pré-remplis, d'id,<br/> étant liés à une database déjà créée, sur **db.sqlite3**.<br/>
<br/>

 ## Administrateur
 Si l'utilisateur est un administrateur, il aura l'interface adéquat pour gérer l'ensemble du projet.<br/>
 Lancez le serveur local( en étant dans le dossier soft_desk ),<br/>
avec la commande ``python manage.py runserver``.
 <br/> Le lien de l'interface admin est :
 http://127.0.0.1:8000/admin/


### Vérification du code
- Pour faire un contrôle du code avec **flake8** (avec max lenght à 79, sauf pour le settings.py), tapez :<br/>
``flake8 --max-line-length 79 --exclude=env,settings.py`` ;<br/><br/>

## Auteur

* **Damien Hernandez** _alias_ [DamienZeh](https://damienhernandez.fr/)








