![Alt text](https://github.com/DamienZeh/soft-desk/blob/main/soft_desk/soft_desk/logo/logo.png)<br>

# API Soft-Desk

- Cette API permet de remonter et de suivre des problèmes technique.<br>
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
- Puis, l’installation  des packages présents dans le requirements.txt:<br> ``pip install -r requirements.txt``<br>
Allez dans le dossier : ``cd soft_desk\``, et créez un fichier **.env** : ``touch .env``.<br/>
Ouvrez **.env** avec un éditeur de texte.<br/>
Il va falloir créer une **SECRET_KEY** et un **DEBUG**. La clé peut être la valeur que vous souhaitez,<br/> et le DEBUG doit être à **True**.
Exemple:<br/>
``SECRET_KEY=la_clef_est_ce_que_vous_voulez``<br/>
``DEBUG=True``<br/>
Enregistrez le fichier, et fermez le.
<br/><br>

### Démarrage

Lancez le  **serveur local**( en étant dans **soft_desk** ), avec la commande « ``python manage.py runserver`` ».<br><br>

## Description de l'API
Cette API permet de:
- **De s'inscrire** et se **connecter**<br/>
Gestion d'un utilisateur.<br/><br/>

- **Gérer des projets**<br/>
Un utilisateur, connecté, peut créer un projet, le modifier, le supprimer, tant qu'il en est l'auteur.<br/>
Un projet doit avoir un titre, une description, et un type(s'il est front-end, back-end, android, ou iOS).<br/><br/>

- **Gérer les utilisateurs d'un projet**<br/>
L'auteur d'un projet, peut ajouter ou supprimer des contributeurs pour ce même projet.<br/> Eux, ne peuvent que le lire. Et personne, en dehors de l'auteur et des autres contributeurs,<br/>
 ne peut accéder aux données du projet. <br/><br/>

- **Gérer des problèmes**<br/>
Chaque contributeur peut ajouter un problème à un projet.<br/>
Il pourra aussi le modifier, supprimer, tant qu'il en est l'auteur.<br/> Les autres contributeurs, ne peuvent que le lire.<br/>
Un problème a titre, une description, une priorité(faible, moyen ou urgent),<br/>
et un status(à faire, en cours, ou terminé).<br/><br/>

- **Gérer les commentaires**<br/>
Par projet, on peut donc avoir des problèmes et chaque problème peut avoir des commentaires.<br/>
Chaque contributeur peut ajouter un commentaire à un problème.<br/>
Il pourra aussi le modifier, supprimer, tant qu'il en est l'auteur.<br/> Les autres contributeurs, ne peuvent que le lire.<br/>
Un commentaire est juste une description.<br/><br/>


## Endpoints de l'API
Toutes ces fonctions sont disponibles grâce à plusieurs points de terminaison d'API,<br/>
 affichés via Postman [**sur ce lien**](https://www.postman.com/damndamn29/workspace/softdesk/folder/19809103-bbbbfe8f-c09e-44d4-b4f5-2d71389235f3?ctx=documentation/)
.<br/>
 Ces 19 liens ont des exemples préremplis, d'id, étant liés à une database déjà créée, **db.sqlite3**.<br/>
 Si vous souhaitez les tester, après avoir obtenu votre premier Token, lors de la connexion(le deuxième endpoint),<br/> gardez le pour tous les autres endpoints suivants. Il est à placé dans le Bearer Token.<br/><br/>

 ## Administrateur
 Si l'utilisateur est un administrateur, il aura l'interface adequat,<br/>
 pour gérer l'ensemble du projet. Le lien est :
 http://127.0.0.1:8000/admin/


### Vérification du code
- Pour faire un contrôle du code avec **flake8** (avec max lenght à 79, sauf pour le settings.py), tapez :<br/>
``flake8 --max-line-length 79 --exclude=env --exclude=settings.py`` ;<br/><br/>

## Auteur

* **Damien Hernandez** _alias_ [DamienZeh](https://damienhernandez.fr/)








